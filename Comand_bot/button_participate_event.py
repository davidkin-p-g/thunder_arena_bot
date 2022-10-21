# -*- coding: utf-8 -*-

import interactions
from bd_connection import execute_query
import bot_info
from logging import Logger

from Comand_bot.add_error import add_error


async def button_participate_event_comand(ctx: interactions.CommandContext, logger_comand: Logger):
    '''
    Кнопка участия в событии(Comand_bot/button_participate_event.py). Передать парметры изначальной функции бота.

    :ivar interactions.CommandContext ctx: Контекст команды
    :ivar Logger logger_comand: Класс логера обрабочика
    '''
    # Получаем имеющиеся данные о пользователе по id
    argx = (int(ctx.user.id),)
    users = execute_query('check_user', argx)
    for user_iterator in users:
        user = user_iterator.fetchall()
    # Обрабаотываем ошибку
    if user == []:
        await ctx.send('Вы еще не зарегистрированы', ephemeral=True)
        return
    logger_comand.debug('Проверен пользователь')

    # Проверяем на изменение Discord имени
    if ctx.author.name != user[0][10]:
        # Полученные пареметры
        argx = (int(ctx.user.id), ctx.author.name)
        # Сейв в бд
        res = execute_query('edit_user_discord_name', argx)
        if isinstance(res, str):
             # Логирование ошибки в базу
            await add_error(ctx, 'edit_user_discord_name', res, 'Недавно ваш UserName в Discord был изменен, но данное изменение не было учтено. Пожалуйста обратитесь к администрации для выяснения причин.')
    logger_comand.debug('Проверили на изменение имени Discord')

    # Полученные пареметры
    argx = (int(ctx.message.id), int(ctx.user.id))
    # Сейв в бд
    res = execute_query('add_user_to_event', argx)
    if isinstance(res, str):
        # Добавлять новые обнаруденые баги через if else
        if res == "error '1644 (45000): Уже зарегестрирован' occurred":
                await ctx.send('Вы уже зарегестрированы в этом событии', ephemeral=True)
            # Добавлять новые обнаруденые баги
        else:
             # Логирование ошибки в базу
            await add_error(ctx, 'button_participate_event', res, bot_info.Erorr_message_standart)
        return
    logger_comand.debug('Добавили пользователя в событие')

    # Узнаем название события
    argx = (int(ctx.message.id),)
    res = execute_query('check_event', argx)
    if isinstance(res, str):
        # Логирование ошибки в базу
        await add_error(ctx, 'button_participate_event', res, bot_info.Erorr_message_standart)
        return
    # Вытаскиваем инфу о событии
    for res_iterator in res:
        event = res_iterator.fetchall()
    # Добавляем роль события
    await ctx.author.add_role(event[0][7], ctx.guild_id)
    logger_comand.debug('Добавили пользователю роль')

    await ctx.send('Вы зарегистрировались на событие', ephemeral=True)