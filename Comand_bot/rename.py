# -*- coding: utf-8 -*-

import interactions
from bd_connection import execute_query
from message import change_message
import bot_info
from logging import Logger

from Comand_bot.add_error import add_error



async def rename_comand(ctx: interactions.CommandContext, user_name: str, logger_comand: Logger):
    '''
    Изменение имени пользователя(Comand_bot/rename.py). Передать парметры изначальной функции бота.

    :ivar interactions.CommandContext ctx: Контекст команды
    :ivar str user_name: Измененное имя
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
    
    # Явно обзовем перемнные для лучшей читаемости
    rating, rating_value, role_1, role_2, role_3, role_4, role_5, ban = user[0][2], user[0][3],user[0][4], user[0][5], user[0][6], user[0][7],user[0][8],user[0][9]
    # Полученные пареметры
    argx = (int(ctx.user.id), user_name, rating, rating_value, role_1, role_2, role_3, role_4, role_5, ban)
    # Сейв в бд
    res = execute_query('edit_user', argx)
    # Проверка  на ошибку
    if isinstance(res, str):
        # Логирование ошибки в базу
        await add_error(ctx, 'rename', res, bot_info.Erorr_message_standart)
        return
    logger_comand.debug('Сохранили в базе')
    # Компановка сообщения
    message = change_message(ctx.author, user_name, rating,  role_1, role_2, role_3, role_4, role_5, 'UserName изменено')
    logger_comand.debug('Отправляем сообщение')
    await ctx.send(embeds=message, ephemeral=True)