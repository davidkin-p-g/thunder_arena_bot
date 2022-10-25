# -*- coding: utf-8 -*-

import interactions
from bd_connection import execute_query
from message import startevent_end_message
import bot_info
from logging import Logger

from Comand_bot.button import *

from Comand_bot.add_error import add_error


async def button_end_event_comand(ctx: interactions.CommandContext, bot, logger_comand: Logger):
    '''
    Кнопка окончания события(Comand_bot/button_end_event.py). Передать парметры изначальной функции бота.

    :ivar interactions.CommandContext ctx: Контекст команды
    :ivar interactions.Client bot: Основной клиент запуска бота
    :ivar Logger logger_comand: Клас логера обрабочика
    '''
    # Провека прав мембера
    # Полюбому можно лучге но я не справился
    permissions = str(ctx.member.permissions).split('|')
    permissions_administrator = False
    for permissions_iterator in permissions:
        if permissions_iterator == 'ADMINISTRATOR':
            permissions_administrator = True
    if not permissions_administrator:
        await ctx.send('Вы не администратор', ephemeral=True)
        return
    logger_comand.debug('Роль пользователя проверена')

    # Получаем параметры События
    argx = (int(ctx.message.id),)
    res = execute_query('check_event', argx)
    # Проверка на бдшную ошибку
    if isinstance(res, str):
            # Логирование ошибки в базу
            await add_error(ctx, 'button_end_event', res, bot_info.Erorr_message_standart)
            return
    # Вытаскиваем инфу о событии
    for res_iterator in res:
        event = res_iterator.fetchall()
    if event == []:
        # Логирование ошибки в базу
        await add_error(ctx, 'button_end_event', 'Несуществующий евент', bot_info.Erorr_message_standart)
        return
    logger_comand.debug('Получили событие')

    # Изменяем статус события
    # Полученные пареметры
    id_event, date_start, type, event_name, status = int(ctx.message.id), event[0][2], event[0][3], event[0][4], 0
    argx = (id_event, date_start, type, event_name, status)
    # Сейв в бд
    res = execute_query('edit_event', argx)
    if isinstance(res, str):
        # Логирование ошибки в базу
        await add_error(ctx, 'button_end_event', res, bot_info.Erorr_message_standart)
        return
    logger_comand.debug('Изменили стату события')

    # Удалем все созданные роли и каналы
    # получаем guild
    guild = interactions.Guild(**await bot._http.get_guild(guild_id=ctx.guild_id), _client=bot._http)
    # Все созданные роли и каналы
    id_event_role = event[0][7]
    id_event_text_channel = event[0][8]
    id_event_voice_channel = event[0][9]
    id_event_category_channel = event[0][10]
    id_role_team_arr = event[0][11].split('|')
    id_channel_team_arr = event[0][12].split('|')

    # Для командных
    try:
        for role in id_role_team_arr:
            if role != '':
                await guild.delete_role(int(role))
        for channel in id_channel_team_arr:
            if channel != '':
                await guild.delete_channel(int(channel))
        # Удаление
        await guild.delete_role(int(id_event_role))
        await guild.delete_channel(int(id_event_text_channel))
        await guild.delete_channel(int(id_event_voice_channel))
        await guild.delete_channel(int(id_event_category_channel))

        logger_comand.debug('Удалили созданые роли и каналы')

        type, event_name, event_description = event[0][3], event[0][4], event[0][5]
        embed = startevent_end_message(type, event_name, event_description)
        logger_comand.debug('Отправляем сообщение')
        await ctx.message.edit(embeds=embed, components=row2)
    except Exception as ex:
        
        logger_comand.warning(f'Во время удаления ролей и каналов произошла ошибка.\n Exception: {ex}')
        await ctx.send('Во время удаления ролей и каналов произошла ошибка. Проверьте фактическое удаление каналов и ролей данного события', ephemeral=True)
        type, event_name, event_description = event[0][3], event[0][4], event[0][5]
        embed = startevent_end_message(type, event_name, event_description)

        logger_comand.debug('Отправляем сообщение')
        await ctx.message.edit(embeds=embed, components=row2)
        return
    