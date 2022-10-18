# -*- coding: utf-8 -*-

from bd_connection import execute_query
import interactions

async def add_error(ctx: interactions.CommandContext, comand: str, exception: str, message: str ):
    '''
    :ivar interactions.CommandContext ctx: Контекст команды вызова
    :ivar str comand: Команда вызова
    :ivar str exception: Ошибка
    :ivar str message: Ответ пользователю
    '''
    argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), comand, exception)
    execute_query('add_error', argx)      
    await ctx.send(message, ephemeral=True)