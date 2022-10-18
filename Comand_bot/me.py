# -*- coding: utf-8 -*-

import interactions
from bd_connection import execute_query
from message import me_message
import bot_info

from Comand_bot.add_error import add_error


async def me_comand(ctx: interactions.CommandContext):
    '''
    Информация о себе(Comand_bot/me.py). Передать парметры изначальной функции бота.

    :ivar interactions.CommandContext ctx: Контекст команды
    '''
    # Проверка на канал использования
    # Получаем имеющиеся данные о пользователе по id
    argx = (int(ctx.user.id),)
    users = execute_query('check_user_to_me_new', argx)
    # Обрабаотываем ошибку
    if isinstance(users, str):
        # Логирование ошибки в базу
        await add_error(ctx, 'rerole', users, bot_info.Erorr_message_standart)
        return
    for user_iterator in users:
        user = user_iterator.fetchall()
    # Обрабаотываем ошибку
    if user == []:
        await ctx.send('Вы еще не зарегистрированы', ephemeral=True)
        return
    # Компановка сообщения
    message = me_message(user)
    await ctx.send(embeds=message)