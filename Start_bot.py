# -*- coding: utf-8 -*-
from time import sleep
import asyncio
import interactions
import discord
from Comand_bot.registration_new import registration_new_comand

from bd_connection import execute_query
from Team_Comp import all_team_comp
# Сайт основной библы
#https://discord-py-slash-command.readthedocs.io/en/latest/
# Работа с базой
#https://www.internet-technologies.ru/articles/posobie-po-mysql-na-python.html
# Может тут базу
#https://selectel.ru/
# Тут написано как
#https://selectel.ru/blog/tutorials/mysql-insert-how-to-add-data-to-a-table/
# Работа с войс каналами 
#https://github.com/interactions-py/voice

from bot_info import TOKEN
# from Add_Player import Add_Player
# from Team_Comp import Team_Comp
import bot_info
from pluhers import check_role
from message import startevent_message
from message import change_message
from message import users_to_event_message
from message import startevent_go_message
from message import startevent_end_message
from message import users_to_event_team_message
from message import me_message
from Command_options import *
# 2 бот 
from discordpy import check_memeber_voice

# Фйлы команд
from Comand_bot.rename import rename_comand
from Comand_bot.registration_new import registration_new_comand
from Comand_bot.rerating import rerating_comand
from Comand_bot.rerole import rerole_comand
from Comand_bot.me import me_comand
from Comand_bot.startevent import startevent_comand
from Comand_bot.button_participate_event import button_participate_event_comand
from Comand_bot.button_participate_event_check import button_participate_event_check_comand
from Comand_bot.button_leave_event import button_leave_event_comand
from Comand_bot.button_start_dm_mess import button_start_dm_mess_comand
from Comand_bot.button_start_event import button_start_event_comand
from Comand_bot.button_end_event import button_end_event_comand
from Comand_bot.button_participate_event_check_team import button_participate_event_check_team_comand


from Comand_bot.add_error import add_error

# interactions
bot = interactions.Client(token=TOKEN)
#discord py
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Команда Регистрации нового пользователя
@bot.command(
    name="registration",
    description='''Регистрация нового пользователя системы.''',
    options=options_registration_new
)
async def registration_new(ctx, user_name, role_1, role_2, role_3, role_4, role_5, rating):
    try:
       await registration_new_comand(ctx, user_name, role_1, role_2, role_3, role_4, role_5, rating)
    except Exception as ex:
        # Логирование ошибки в базу
       await add_error(ctx, 'registration', str(ex), bot_info.Erorr_message_standart)


# Команда изменения Ника пользователя
@bot.command(
    name="rename",
    description='''Изменение имени пользователя на RU сервере.''',
    options=options_rename
)
async def rename(ctx: interactions.CommandContext, user_name):
    try:
        # Функционал команды
        await rename_comand(ctx, user_name)
    except Exception as ex:
        # Логирование ошибки в базу
        await add_error(ctx, 'rename', str(ex), bot_info.Erorr_message_standart)


# Команда изменения Рейтинга пользователя
@bot.command(
    name="rerating",
    description='''Изменение Рейтинга.''',
    options=options_rating
)
async def rerating(ctx: interactions.CommandContext, rating):
    try:
        # Функционал команды
        await rerating_comand(ctx, rating)
    except Exception as ex:
        # Логирование ошибки в базу
        await add_error(ctx, 'rerating', str(ex), bot_info.Erorr_message_standart)


# Команда изменения Роли пользователя
@bot.command(
    name="rerole",
    description='''Изменение расстановки ролей.''',
    options=options_rerole
)
async def rerole(ctx: interactions.CommandContext, role_1, role_2, role_3, role_4, role_5):
    try:
        # Функционал команды
        await rerole_comand(ctx, role_1, role_2, role_3, role_4, role_5)
    except Exception as ex:
        # Логирование ошибки в базу
        await add_error(ctx, 'rerole', str(ex), bot_info.Erorr_message_standart)


#ME
@bot.command(
    name="me",
    description='''Информация о себе''',
)
async def me(ctx: interactions.CommandContext):
    try:
        # Функционал команды
        await me_comand(ctx)
    except Exception as ex:
         # Логирование ошибки в базу
        await add_error(ctx, 'me', str(ex), bot_info.Erorr_message_standart)


@bot.command(
    name = 'startevent',
    description= '''Запустить новое событие.
    Канал использования admin.''',
    default_member_permissions= interactions.Permissions.ADMINISTRATOR,
    options=options_start_event
    
)
async def startevent(ctx: interactions.CommandContext, event_type, event_name, event_description, event_date_start):
    try:
         # Функционал команды
        await startevent_comand(ctx, event_type, event_name, event_description, event_date_start)
    except Exception as ex:
         # Логирование ошибки в базу
        await add_error(ctx, 'startevent', str(ex), bot_info.Erorr_message_standart)


# Обработка кнопок события
# Учавствовать
@bot.component("participate_event")
async def button_participate_event(ctx: interactions.CommandContext):
    try:
        # Функционал команды
        await button_participate_event_comand(ctx)
    except Exception as ex:
         # Логирование ошибки в базу
        await add_error(ctx, 'participate_event', str(ex), bot_info.Erorr_message_standart)
        

#Кто учавствует
@bot.component("participate_event_check")
async def button_participate_event_check(ctx: interactions.CommandContext):
    try:
        # Функционал команды
        await button_participate_event_check_comand(ctx)
    except IndexError:
        await ctx.send('Нет участников. Стань первым))', ephemeral=True)
    except Exception as ex:
        # Логирование ошибки в базу
        await add_error(ctx, 'participate_event_check', str(ex), bot_info.Erorr_message_standart)


# Уйти
@bot.component("leave_event")
async def button_leave_event(ctx: interactions.CommandContext):
    try:
        # Функционал команды
        await button_leave_event_comand(ctx)
    except Exception as ex:
        # Логирование ошибки в базу
        await add_error(ctx, 'leave_event', str(ex), bot_info.Erorr_message_standart)


#  Рассылка личных сообщений
@bot.component("start_dm_mess")
async def button_start_dm_mess(ctx: interactions.CommandContext):
    try:
        # Функционал команды
        await button_start_dm_mess_comand(ctx, bot)
    except Exception as ex:
        # Логирование ошибки в базу
        await add_error(ctx, 'start_dm_mess', str(ex), bot_info.Erorr_message_standart)
       

# Запустить
@bot.component("start_event")
async def button_start_event(ctx: interactions.CommandContext):
    try:
        # Функционал команды
        await button_start_event_comand(ctx, bot, client)
    except Exception as ex:
        # Логирование ошибки в базу
        await add_error(ctx, 'start_event', str(ex), bot_info.Erorr_message_standart)
       

# Завершить
@bot.component("end_event")
async def button_end_event(ctx: interactions.CommandContext):
    try:
       # Функционал команды
        await button_end_event_comand(ctx, bot)
    except Exception as ex:
        # Логирование ошибки в базу
        await add_error(ctx, 'end_event', str(ex), bot_info.Erorr_message_standart)
       

# Список команд
@bot.component("participate_event_check_team")
async def button_participate_event_check_team(ctx: interactions.CommandContext):
    try:
        # Функционал команды
        await button_participate_event_check_team_comand(ctx)
    except IndexError:
        await ctx.send('К сожалению на этом турнире нет участников)', ephemeral=True)
    except Exception as ex:
        # Логирование ошибки в базу
        await add_error(ctx, 'participate_event_check_team', str(ex), bot_info.Erorr_message_standart)
       
#Админский блок сервисная часть

# Баны пользователей может еще сколько игр сыграл
@bot.command(
    name = 'check_channel',
    description= 'Админская команда для определения id канала',
    default_member_permissions= interactions.Permissions.ADMINISTRATOR

)
async def check_channel(ctx: interactions.CommandContext):
    
    await ctx.send(str(ctx.channel_id))


# Временный блок
@bot.command(
    name = 'add_member_role',
    description= 'Админская команда для выдачи всем участникам зареганым в боте роли',
    default_member_permissions= interactions.Permissions.ADMINISTRATOR

)
async def add_member_role(ctx: interactions.CommandContext):
    # Получаем users
    res = execute_query('all_users')
    for userss in res:
        users = userss.fetchall()
    i = 1
    for user in users:
        try:
            # ЭТО ЛЕГЕНТААААААААААА
            member = interactions.Member(**await bot._http.get_member(member_id=int(user[0]), guild_id=int(ctx.guild_id)), _client=bot._http)
            # ЭТО ЛЕГЕНТААААААААААА
            await member.add_role(bot_info.role_id, ctx.guild_id)
            await ctx.send(f'{i} {user[1]} присвоена роль', ephemeral=True)
        except:
            await ctx.send(f'{i} {user[1]} не найден', ephemeral=True)
        sleep(2)
        i+=1
    await ctx.send('Мы закончили ))', ephemeral=True)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

if __name__ == '__main__':
    # Запускаем одновременно 2 обрабочика событий с разный библиотек
    loop = asyncio.get_event_loop()

    # асинхронно запущенные таски кажеться ))
    task2 = loop.create_task(client.start(bot_info.TOKEN))
    task1 = loop.create_task(bot._ready())
    
    
    # Кажеться обьединяет их и дает им работать одновременно
    gathered = asyncio.gather(task1, task2)
    loop.run_until_complete(gathered)
