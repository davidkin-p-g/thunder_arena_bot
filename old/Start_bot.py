import discord
from discord.ext import commands
import datetime
import json
import os
import traceback

from bot_info import TOKEN_Test as TOKEN
from Add_Player import Add_Player
from Team_Comp import Team_Comp
import bot_info


##########
# Переделываю под нормалоьные команды
# Вместо @client.event -> @bot.command
description = '''Демонстрация.'''

intents = discord.Intents.default()
#intents.members = True
#intents.message_content = True

bot = commands.Bot(command_prefix='/', description=description, intents=intents)
###########

#client = discord.Client()
# v. 0.1
# v. 0.2
# v. 0.3
# v. 2.0
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.

if __name__ == '__main__':
    bot.run(TOKEN)
    