# -*- coding: utf-8 -*-

import interactions
from bd_connection import execute_query
from message import startevent_message
import bot_info

from Comand_bot.button import *

from Comand_bot.add_error import add_error


async def button_start_dm_mess_comand(ctx: interactions.CommandContext, bot):
    '''
    Кнопка рассылки личных сообщений о скором начале(Comand_bot/button_start_dm_mess.py). Передать парметры изначальной функции бота.

    :ivar interactions.CommandContext ctx: Контекст команды
    :ivar interactions.Client bot: Основной клиент запуска бота
    '''
    permissions = str(ctx.member.permissions).split('|')
    permissions_administrator = False
    for permissions_iterator in permissions:
        if permissions_iterator == 'ADMINISTRATOR':
            permissions_administrator = True
    if not permissions_administrator:
        await ctx.send('Вы не администратор', ephemeral=True)
        return
    # Получаем параметры События
    argx = (int(ctx.message.id),)
    res = execute_query('check_event', argx)
    # Проверка на бдшную ошибку
    if isinstance(res, str):
            # Логирование ошибки в базу
            await add_error(ctx, 'button_start_dm_mess', res, bot_info.Erorr_message_standart)
            return
    # Вытаскиваем инфу о событии
    for res_iterator in res:
        event = res_iterator.fetchall()
    if event == []:
        # Логирование ошибки в базу
        await add_error(ctx, 'button_start_dm_mess', 'Несуществующий евент', bot_info.Erorr_message_standart)
        return
    # Полученные пареметры
    event_type, event_name, event_description, event_date_start = event[0][3], event[0][4], event[0][5], event[0][2]
    dm_flag = 1
    message = startevent_message(event_type, event_name, event_description, event_date_start, dm_flag)

    # Отправить рассыку
    # Полученные пареметры
    argx = (int(ctx.message.id),)
    # Сейв в бд
    res = execute_query('all_user_to_event_new', argx)
    if isinstance(res, str):
        # Логирование ошибки в базу
        await add_error(ctx, 'button_start_dm_mess', res, bot_info.Erorr_message_standart)
        return
        
    for user_to_events in res:
        user_to_event = user_to_events.fetchall()
    # Отправляем личное сообщение каждому пользователю в личку
    for user in user_to_event:
        member = interactions.Member(**await bot._http.get_member(member_id=int(user[0]), guild_id=int(ctx.guild_id)), _client=bot._http)
        await member.send(f'Началась провека готовности участников в событии {user[1]}. \nПожалуйста, зайдите в голосовой канал события для проверки. \nПредупреждение: В случае вашего отсутствия в канале, вероятность отправиться в запас увеличится.')

    await ctx.message.edit(embeds=message, components=row0_5)