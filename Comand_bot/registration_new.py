# -*- coding: utf-8 -*-

import interactions
from bd_connection import execute_query
from message import change_message
import bot_info
from pluhers import check_role

from Comand_bot.add_error import add_error

async def registration_new_comand(ctx: interactions.CommandContext, user_name: str, role_1: str, role_2: str, role_3: str, role_4: str, role_5: str, rating: str):
    '''
    Регистрация пользователя(Comand_bot/registration_new.py). Передать парметры изначальной функции бота.

    :ivar interactions.CommandContext ctx: Контекст команды
    :ivar str user_name: Имя пользователя
    :ivar str role_?: Роли пользователя
    :ivar str rating: Рейтинг пользователя
    '''

    # Проверка ролей
    if not check_role(role_1, role_2, role_3, role_4, role_5):
        await ctx.send('Роли не могут повторяться', ephemeral=True)
        return
    # Деление на рейтинг и его числовой эквивалент
    rating_player = rating.split(':')
    # Явно обзовем перемнные для лучшей читаемости
    rating = rating_player[0]
    rating_value = int(rating_player[1])
    # Полученные пареметры
    argx = (int(ctx.user.id), user_name, rating, rating_value,  role_1, role_2, role_3, role_4, role_5, str(ctx.author))
    # Сейв в бд
    res = execute_query('add_user', argx)
    # Провека на ответ базы
    if isinstance(res, str):
        error =  res.split(' ')[1]
        if error == ''''1062''':
            await ctx.send('Вы уже зарегистрированы', ephemeral=True)
        # Добавлять новые обнаруденые баги
        else:
            # Логирование ошибки в базу
            await add_error(ctx, 'registration', res, bot_info.Erorr_message_standart)
        return
    # Выдадим роль Учатника
    await ctx.author.add_role(bot_info.role_id, ctx.guild_id)
    # Компановка сообщения
    message = change_message(ctx.author, user_name, rating, role_1, role_2, role_3, role_4, role_5, 'Новый пользователь')
    await ctx.send(embeds=message, ephemeral=True)