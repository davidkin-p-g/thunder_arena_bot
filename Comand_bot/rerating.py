# -*- coding: utf-8 -*-

import interactions
from bd_connection import execute_query
from message import change_message
import bot_info

from Comand_bot.add_error import add_error


async def rerating_comand(ctx: interactions.CommandContext, rating: str):
    '''
    Изменение имени пользователя(Comand_bot/rerating.py). Передать парметры изначальной функции бота.

    :ivar interactions.CommandContext ctx: Контекст команды
    :ivar str rating: Измененный рейтинг
    '''
    # Деление на рейтинг и его числовой эквивалент
    rating_player = rating.split(':')
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
    user_name, rating, rating_value, role_1, role_2, role_3, role_4, role_5, ban = user[0][1], rating_player[0], int(rating_player[1]),user[0][4], user[0][5], user[0][6], user[0][7],user[0][8],user[0][9]
    # Полученные пареметры
    argx = (int(ctx.user.id), user_name, rating, rating_value, role_1, role_2, role_3, role_4, role_5, ban)
    # Сейв в бд
    res = execute_query('edit_user', argx)
    if isinstance(res, str):
        # Логирование ошибки в базу
        await add_error(ctx, 'rerating', res, bot_info.Erorr_message_standart)
        return
    # Компановка сообщения
    message = change_message(ctx.author, user_name, rating,  role_1, role_2, role_3, role_4, role_5, 'Рейтинг Изменен')
    await ctx.send(embeds=message, ephemeral=True)