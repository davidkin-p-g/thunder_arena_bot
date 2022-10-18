# -*- coding: utf-8 -*-

import interactions
from bd_connection import execute_query
from message import startevent_message
import bot_info

from Comand_bot.button import *
from Comand_bot.add_error import add_error


async def startevent_comand(ctx: interactions.CommandContext, event_type: str, event_name: str, event_description: str, event_date_start: str):
    '''
    Запуск нового события(Comand_bot/me.py). Передать парметры изначальной функции бота.

    :ivar interactions.CommandContext ctx: Контекст команды
    :ivar str event_type: Тип события
    :ivar str event_name: Названия события
    :ivar str event_description: Описание события
    :ivar str event_date_start: Дата Начала события DateTime тип базы данных
    '''

    # Так как я не могу получить нормальный id сообщения до его отправки 
    # а хочеться сразу несколько событий запускать я пердпринял радикальное действо
    # и отправляю сообщение а уже потом пишу в базу

    # Компановка сообщения
    message = startevent_message(event_type, event_name, event_description, event_date_start)
    await ctx.send(embeds=message, components=row)
    # Добавляю роль для события
    role = await ctx.guild.create_role(name=event_name)
    # Добавляю каналы для события parent_id
    # Категория
    category = await ctx.guild.create_channel(name=event_name, type=interactions.ChannelType(4))
    permission = [
        interactions.Overwrite(
            id=int(role.id),
            allow=(0x0000000000000400+0x0000000000000800+0x0000000000004000+0x0000000000008000+0x0000000000040000)
        ),
        interactions.Overwrite(
            id=int(bot_info.everyone_id),
            deny=(0x0000000000000400)
        )
    ]
    # Каналы прикреполенные к категории с привязкой прав
    text_channel = await ctx.guild.create_channel(name=event_name, type=interactions.ChannelType(0), permission_overwrites=permission,parent_id=int(category.id))
    voice_channel = await ctx.guild.create_channel(name=event_name, type=interactions.ChannelType(2), permission_overwrites=permission,parent_id=int(category.id))
    # Полученные пареметры
    argx = (int(ctx.message.id), event_type, event_name, event_description, event_date_start, int(role.id), int(text_channel.id), int(voice_channel.id), int(category.id))
    # Сейв в бд
    res = execute_query('add_event', argx)
    if isinstance(res, str):
         # Логирование ошибки в базу
        await add_error(ctx, 'startevent', res, bot_info.Erorr_message_standart)
        return