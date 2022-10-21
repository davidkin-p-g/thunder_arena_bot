# -*- coding: utf-8 -*-

import interactions
from bd_connection import execute_query
from message import users_to_event_message
import bot_info
from logging import Logger

from Comand_bot.add_error import add_error


async def button_participate_event_check_comand(ctx: interactions.CommandContext, logger_comand: Logger):
    '''
    Кнопка кто учавствует(Comand_bot/button_participate_event_check.py). Передать парметры изначальной функции бота.

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
    logger_comand.debug('Проверен пользователь')

    # Полученные пареметры
    argx = (int(ctx.message.id),)
    # Сейв в бд
    res = execute_query('all_user_to_event_new', argx)
    if isinstance(res, str):
        # Логирование ошибки в базу
        await add_error(ctx, 'button_participate_event_check', res, bot_info.Erorr_message_standart)
        return
    for user_to_events in res:
        user_to_event = user_to_events.fetchall()
    logger_comand.debug('получены пользователи события')

    # Провека прав мембера разное сообщение в зависимости от прав
    # Полюбому можно лучге но я не справился
    permissions = str(ctx.member.permissions).split('|')
    permissions_administrator = False
    for permissions_iterator in permissions:
        if permissions_iterator == 'ADMINISTRATOR':
            permissions_administrator = True
    embed = users_to_event_message(user_to_event, permissions_administrator)
    logger_comand.debug('Отправялем сообщение')

    await ctx.send(embeds=embed, ephemeral=True)