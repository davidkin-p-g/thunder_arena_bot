# -*- coding: utf-8 -*-

from distutils.log import error
import interactions
from bd_connection import execute_query
from message import startevent_go_message
import bot_info
from logging import Logger
from Team_Comp import all_team_comp

from Comand_bot.button import *

from Comand_bot.add_error import add_error


async def button_start_event_comand(ctx: interactions.CommandContext, bot, client, logger_comand: Logger):
    '''
    Кнопка начала события(Comand_bot/button_start_event.py). Передать парметры изначальной функции бота.

    :ivar interactions.CommandContext ctx: Контекст команды
    :ivar interactions.Client bot: Основной клиент запуска бота
    :ivar discord.Client client: дополнительный клиент запуска бота
    :ivar Logger logger_comand: Класс логера обрабочика
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
    logger_comand.debug('Проверили роль пользователя')

    # Получаем параметры События
    argx = (int(ctx.message.id),)
    res = execute_query('check_event', argx)
    # Проверка на бдшную ошибку
    if isinstance(res, str):
        # Логирование ошибки в базу
        await add_error(ctx, 'button_start_event', res, bot_info.Erorr_message_standart)
        return
    # Вытаскиваем инфу о событии
    for res_iterator in res:
        event = res_iterator.fetchall()
    if event == []:
        # Логирование ошибки в базу
        await add_error(ctx, 'button_start_event', 'Несуществующий евент', bot_info.Erorr_message_standart)
        return
    logger_comand.debug('Получили инофрмацию о событии')

    # Изменяем статус события
    # Полученные пареметры
    id_event, date_start, type, event_name, status = int(ctx.message.id), event[0][2], event[0][3], event[0][4], 2
    argx = (id_event, date_start, type, event_name, status)
    # Сейв в бд
    res = execute_query('edit_event', argx)
    if isinstance(res, str):
        # Логирование ошибки в базу
        await add_error(ctx, 'button_start_event', res, bot_info.Erorr_message_standart)
        return
    logger_comand.debug('Изменили стату события')

    # Полученные пареметры
    argx = (int(ctx.message.id),)
    # Сейв в бд
    res = execute_query('all_user_to_event_new', argx)
    if isinstance(res, str):
        # Логирование ошибки в базу
        await add_error(ctx, 'button_start_event', res, bot_info.Erorr_message_standart)
        return   
    for user_to_events in res:
        user_to_event = user_to_events.fetchall()
    
    #------------------------------
    # Проверить на пустоту масива участников 
    #------------------------------
    logger_comand.debug('Получили пользователей учавствующий в событии')

    # Провека прав мембера
    # Полюбому можно лучге но я не справился
    permissions = str(ctx.member.permissions).split('|')
    permissions_administrator = False
    for permissions_iterator in permissions:
        if permissions_iterator == 'ADMINISTRATOR':
            permissions_administrator = True

    # Формирование команд + проверка войса
    comand_count, error = all_team_comp(user_to_event, permissions_administrator, int(ctx.message.id), client, logger_comand)
    if error != '':
        await ctx.send(error, ephemeral=True)
    # /Формирование команд
    logger_comand.debug('Сформировали команды')
    
    # Получаем всех участников
    # Полученные пареметры
    argx = (int(ctx.message.id),)
    # Сейв в бд
    res = execute_query('all_user_to_event_team_new', argx)
    if isinstance(res, str):
        # Логирование ошибки в базу
        await add_error(ctx, 'button_start_event', res, bot_info.Erorr_message_standart)
        return

    for user_to_events in res:
        user_to_event = user_to_events.fetchall()

    #Генерим каналы и роли для команд и запасных
    try:
        id_channel_team_arr = ''
        id_role_team_arr = ''
        for channel in range(comand_count+1):
            if channel == 0:
                name = 'Запасные'
            else:
                name = f'Команда {channel}'
            role = await ctx.guild.create_role(name=f'{event_name} {name}')
            permission = [
                interactions.Overwrite(
                    id=int(role.id),
                    allow=(0x0000000000000400+0x0000000000000800+0x0000000000004000+0x0000000000008000+0x0000000000040000)
                ),
                interactions.Overwrite(
                    id=int(bot_info.everyone_id),
                    deny=(0x0000000000000400)
                )
            ]
            # Каналы прикреполенные к категории с привязкой прав
            category_id = event[0][10]
            text_channel = await ctx.guild.create_channel(name=name, type=interactions.ChannelType(0), permission_overwrites=permission,parent_id=int(category_id))
            voice_channel = await ctx.guild.create_channel(name=name, type=interactions.ChannelType(2), permission_overwrites=permission,parent_id=int(category_id))
            # Для записи в бд
            id_channel_team_arr = id_channel_team_arr + f'{int(text_channel.id)}|' + f'{int(voice_channel.id)}|'
            id_role_team_arr = id_role_team_arr + f'{int(role.id)}|'
            # присвоим игрокам соответствующие роли
            for user in user_to_event:
                if user[3] == f'Команда {channel}':
                    member = interactions.Member(**await bot._http.get_member(member_id=int(user[0]), guild_id=ctx.guild_id), _client=bot._http)
                    await member.add_role(int(role.id), ctx.guild_id)
                elif user[3] is None:
                    member = interactions.Member(**await bot._http.get_member(member_id=int(user[0]), guild_id=ctx.guild_id), _client=bot._http)
                    await member.add_role(int(role.id), ctx.guild_id)
            # Отправление всех id комнат и ролей в бд
            argx = (int(ctx.message.id),id_role_team_arr, id_channel_team_arr)
            # Сейв в бд
            res = execute_query('add_arr_id_to_event', argx)
            if isinstance(res, str):
                # Добавлять новые обнаруденые баги через if else
                # Логирование ошибки в базу
                argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'start_event загрузка всех id каналов в бд', res)
                execute_query('add_error', argx)  
                print(res)
                await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
                return
        logger_comand.debug('Создали роли и каналы для команд и раздали роли пользователям')

        # Генерим сообщение
        type, event_name, event_description = event[0][3], event[0][4], event[0][5]
        embed = startevent_go_message(type, event_name, event_description)

        logger_comand.debug('Отпраляем сообщение')
        await ctx.message.edit(embeds=embed, components=row1)

    except Exception as ex:
        logger_comand.warning(f'Во время генерации ролей и каналов произошла ошибка.\n Exception: {ex}')

        # Генерим сообщение
        type, event_name, event_description = event[0][3], event[0][4], event[0][5]
        embed = startevent_go_message(type, event_name, event_description)
        logger_comand.debug('Отпраляем сообщение')

        await ctx.message.edit(embeds=embed, components=row1)
        await ctx.send('Во время генерации ролей и каналов произошла ошибка. Команды и роли были созданы не правильно. Работа бота не нарушена за усключением ролей и каналов для участников.', ephemeral=True)