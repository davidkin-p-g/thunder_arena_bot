# -*- coding: utf-8 -*-

import interactions
from bd_connection import execute_query
from message import me_message
import bot_info
from logging import Logger

from Comand_bot.add_error import add_error


async def me_comand(ctx: interactions.CommandContext, logger_comand: Logger):
    '''
    Информация о себе(Comand_bot/me.py). Передать парметры изначальной функции бота.

    :ivar interactions.CommandContext ctx: Контекст команды
    :ivar Logger logger_comand: Класс логера обрабочика
    '''
    # Проверка на канал использования
    # Получаем имеющиеся данные о пользователе по id
    argx = (int(ctx.user.id),)
    users = execute_query('check_user_to_me_new', argx)
    # Обрабаотываем ошибку
    if isinstance(users, str):
        # Логирование ошибки в базу
        await add_error(ctx, 'me', users, bot_info.Erorr_message_standart)
        return
    for user_iterator in users:
        user = user_iterator.fetchall()
    # Обрабаотываем ошибку
    if user == []:
        await ctx.send('Вы еще не зарегистрированы', ephemeral=True)
        return
    logger_comand.debug('Проверен пользователь')
    # Компановка сообщения
    message = me_message(user)
    logger_comand.debug('Отправляем сообщение')

    await ctx.send(embeds=message)