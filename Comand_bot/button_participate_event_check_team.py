# -*- coding: utf-8 -*-

import interactions
from bd_connection import execute_query
from message import users_to_event_team_message
import bot_info


from Comand_bot.add_error import add_error


async def button_participate_event_check_team_comand(ctx: interactions.CommandContext):
    '''
    Кнопка просмотра команд(Comand_bot/button_participate_event_check_team.py). Передать парметры изначальной функции бота.

    :ivar interactions.CommandContext ctx: Контекст команды
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
    # Полученные пареметры
    argx = (int(ctx.message.id),)
    # Сейв в бд
    res = execute_query('all_user_to_event_team_new', argx)
    if isinstance(res, str):
        # Логирование ошибки в базу
        await add_error(ctx, 'button_participate_event_check_team', res, bot_info.Erorr_message_standart)
        return 
    for user_to_events in res:
        user_to_event = user_to_events.fetchall()
    # Провека прав мембера
    # Полюбому можно лучге но я не справился
    permissions = str(ctx.member.permissions).split('|')
    permissions_administrator = False
    for permissions_iterator in permissions:
        if permissions_iterator == 'ADMINISTRATOR':
            permissions_administrator = True
    embed = users_to_event_team_message(user_to_event, permissions_administrator)
    await ctx.send(embeds=embed, ephemeral=True)