# -*- coding: utf-8 -*-

import interactions
from bd_connection import execute_query
import bot_info
from logging import Logger

from Comand_bot.add_error import add_error


async def button_leave_event_comand(ctx: interactions.CommandContext, logger_comand: Logger):
    '''
    Кнопка уйти из события(Comand_bot/button_leave_event.py). Передать парметры изначальной функции бота.

    :ivar interactions.CommandContext ctx: Контекст команды
    :ivar Logger logger_comand: Клас логера обрабочика
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
    logger_comand.debug('Проверили пользователя')

    # Полученные пареметры
    argx = (int(ctx.message.id), int(ctx.user.id))
    # Сейв в бд
    res = execute_query('delete_user_to_event', argx)
    if isinstance(res, str):
        # Добавлять новые обнаруденые баги через if else
        if res == "error '1644 (45000): Еще не зарегестрирован' occurred":
                await ctx.send('Вы еще не зарегестрированы в этом событии', ephemeral=True)
            # Добавлять новые обнаруденые баги
        else:
            # Логирование ошибки в базу
            await add_error(ctx, 'button_leave_event', res, bot_info.Erorr_message_standart)
        return
    logger_comand.debug('Удалил пользователя из базы события')

    # Узнаем название события
    argx = (int(ctx.message.id),)
    res = execute_query('check_event', argx)
    if isinstance(res, str):
        await add_error(ctx, 'button_leave_event', res, bot_info.Erorr_message_standart)
        return
    # Вытаскиваем инфу о событии
    for res_iterator in res:
        event = res_iterator.fetchall()
    await ctx.author.remove_role(event[0][7], ctx.guild_id)
    logger_comand.debug('Забрали роль участника события')
    
    await ctx.send('Вы больше не зарегистрированы в этом событии', ephemeral=True)