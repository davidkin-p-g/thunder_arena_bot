import interactions
from bd_connection import execute_query
from message import ban_message
from message import unban_message
import bot_info
from logging import Logger

from Comand_bot.add_error import add_error


async def ban_member_comand(ctx: interactions.CommandContext, discord_name: str, reason: str, logger_comand: Logger, ban):
    '''
    Бан/Разбан пользователя(Comand_bot/ban_member.py). Передать парметры изначальной функции бота.

    :ivar interactions.CommandContext ctx: Контекст команды
    :ivar str discord_name: Discord name пользователя
    :ivar str reason: Причина бана
    :ivar Logger logger_comand: Класс логера обрабочика
    '''
    logger_comand.debug('Изменяем параметр бана в базе')
    # Полученные пареметры
    argx = (discord_name, reason, ban)
    # Сейв в бд
    res = execute_query('edit_ban', argx)
    # Проверка  на ошибку
    if isinstance(res, str):
        if res == "error '1644 (45000): Нет такого пользователя' occurred":
                await ctx.send('Такого пользователя не существует (Возможно он сменил ник тогда беда)', ephemeral=True)
                return
        # Логирование ошибки в базу
        await add_error(ctx, 'ban_member', res, bot_info.Erorr_message_standart)
        return
    logger_comand.debug('Сохранили в базе')
    # Компановка сообщения
    if ban == 1:
        message = ban_message(ctx.author, discord_name, reason)
    else:
        message = unban_message(ctx.author, discord_name, reason)
    logger_comand.debug('Отправляем сообщение')
    await ctx.send(embeds=message, ephemeral=True)