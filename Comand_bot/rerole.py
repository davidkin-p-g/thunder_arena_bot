# -*- coding: utf-8 -*-

import interactions
from bd_connection import execute_query
from message import change_message
import bot_info
from pluhers import check_role

from Comand_bot.add_error import add_error


async def rerole_comand(ctx: interactions.CommandContext, role_1: str, role_2: str, role_3: str, role_4: str, role_5: str):
    '''
    Изменение имени пользователя(Comand_bot/rerole.py). Передать парметры изначальной функции бота.

    :ivar interactions.CommandContext ctx: Контекст команды
    :ivar str role_?:  Измененые роли пользователя
    '''
    # Проверка на уникальность ролей  
    if not check_role(role_1, role_2, role_3, role_4, role_5):
        await ctx.send('Роли не могут повторяться', ephemeral=True)
        return
    # Получаем имеющиеся данные о пользователе по id
    argx = (int(ctx.user.id),)
    users = execute_query('check_user', argx)
    for user_iterator in users:
        user = user_iterator.fetchall()
    # Обрабаотываем ошибку
    if user == []:
        await ctx.send('Вы еще не зарегистрированы', ephemeral=True)
        return
    # Явно обзовем перемнные для лучшей читаемости
    user_name, rating, rating_value, ban = user[0][1], user[0][2], user[0][3], user[0][9]
    # Полученные пареметры
    argx = (int(ctx.user.id), user_name, rating, rating_value, role_1, role_2, role_3, role_4, role_5, ban)
    # Сейв в бд
    res = execute_query('edit_user', argx)
    if isinstance(res, str):
        # Логирование ошибки в базу
        await add_error(ctx, 'rerole', res, bot_info.Erorr_message_standart)
        return
    # Компановка сообщения
    message = change_message(ctx.author, user_name, rating, role_1, role_2, role_3, role_4, role_5, 'Выбор ролей изменен')
    await ctx.send(embeds=message, ephemeral=True)