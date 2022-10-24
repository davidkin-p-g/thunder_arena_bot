# -*- coding: utf-8 -*-

import interactions
from interactions.ext.files import command_send
import discord
from threading import Thread, Event

from time import sleep
import asyncio

from Comand_bot.registration_new import registration_new_comand

from bd_connection import execute_query
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
from Command_options import *

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
from Comand_bot.send_log import send_log_comand

#Файлы обрабочика ошибок
from Comand_bot.add_error import add_error
from Comand_bot.add_error import add_error_for_working_bot

#Логер
from log_start import create_config_log
from schedule_start import schedule_start

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
        logger_bot_component_start.info(f'Зпущен компонент id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
        bot_info.comand_dict['registration'][0]  += 1
        # Функционал команды
        await registration_new_comand(ctx, user_name, role_1, role_2, role_3, role_4, role_5, rating, logger_comand)
        logger_bot_component_end.info(f'Компонент успешно завершен id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
        #добавлиение количества использований
    except Exception as ex:
        logger_bot_component_end.error(f'ER Компонент завершен с ошибкой id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)} \n Exception: {ex}')
        bot_info.comand_dict['error'][0]  += 1
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
        logger_bot_component_start.info(f'Зпущен компонент id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
        bot_info.comand_dict['rename'][0]  += 1
        # Функционал команды
        await rename_comand(ctx, user_name, logger_comand, bot)
        logger_bot_component_end.info(f'Компонент успешно завершен id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
    except Exception as ex:
        logger_bot_component_end.error(f'ER Компонент завершен с ошибкой id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)} \n Exception: {ex}')
        bot_info.comand_dict['error'][0]  += 1
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
        logger_bot_component_start.info(f'Зпущен компонент id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
        bot_info.comand_dict['rerating'][0]  += 1
        # Функционал команды
        await rerating_comand(ctx, rating, logger_comand)
        logger_bot_component_end.info(f'Компонент успешно завершен id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
    except Exception as ex:
        logger_bot_component_end.error(f'ER Компонент завершен с ошибкой id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)} \n Exception: {ex}')
        bot_info.comand_dict['error'][0]  += 1
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
        logger_bot_component_start.info(f'Зпущен компонент id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
        bot_info.comand_dict['rerole'][0]  += 1
        # Функционал команды
        await rerole_comand(ctx, role_1, role_2, role_3, role_4, role_5, logger_comand)
        logger_bot_component_end.info(f'Компонент успешно завершен id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
    except Exception as ex:
        logger_bot_component_end.error(f'ER Компонент завершен с ошибкой id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)} \n Exception: {ex}')
        bot_info.comand_dict['error'][0]  += 1
        # Логирование ошибки в базу
        await add_error(ctx, 'rerole', str(ex), bot_info.Erorr_message_standart)


#ME
@bot.command(
    name="me",
    description='''Информация о себе''',
)
async def me(ctx: interactions.CommandContext):
    try:
        logger_bot_component_start.info(f'Зпущен компонент id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
        bot_info.comand_dict['me'][0]  += 1
        # Функционал команды
        await me_comand(ctx, logger_comand)
        logger_bot_component_end.info(f'Компонент успешно завершен id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
    except Exception as ex:
        logger_bot_component_end.error(f'ER Компонент завершен с ошибкой id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)} \n Exception: {ex}')
        bot_info.comand_dict['error'][0]  += 1
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
        logger_bot_component_start.info(f'Зпущен компонент id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
        bot_info.comand_dict['startevent'][0]  += 1
         # Функционал команды
        await startevent_comand(ctx, event_type, event_name, event_description, event_date_start, logger_comand)
        logger_bot_component_end.info(f'Компонент успешно завершен id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
    except Exception as ex:
        logger_bot_component_end.error(f'ER Компонент завершен с ошибкой id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)} \n Exception: {ex}')
        bot_info.comand_dict['error'][0]  += 1
         # Логирование ошибки в базу
        await add_error(ctx, 'startevent', str(ex), bot_info.Erorr_message_standart)


# Обработка кнопок события
# Учавствовать
@bot.component("participate_event")
async def button_participate_event(ctx: interactions.CommandContext):
    try:
        logger_bot_component_start.info(f'Зпущен компонент id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
        bot_info.comand_dict['participate_event'][0]  += 1
        # Функционал команды
        await button_participate_event_comand(ctx, logger_comand)
        logger_bot_component_end.info(f'Компонент успешно завершен id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
    except Exception as ex:
        logger_bot_component_end.error(f'ER Компонент завершен с ошибкой id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)} \n Exception: {ex}')
        bot_info.comand_dict['error'][0]  += 1
         # Логирование ошибки в базу
        await add_error(ctx, 'participate_event', str(ex), bot_info.Erorr_message_standart)
        

#Кто учавствует
@bot.component("participate_event_check")
async def button_participate_event_check(ctx: interactions.CommandContext):
    try:
        logger_bot_component_start.info(f'Зпущен компонент id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
        bot_info.comand_dict['participate_event_check'][0]  += 1
        # Функционал команды
        await button_participate_event_check_comand(ctx, logger_comand)
        logger_bot_component_end.info(f'Компонент успешно завершен id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
    except IndexError:
        await ctx.send('Нет участников. Стань первым))', ephemeral=True)
        logger_bot_component_end.info(f'Компонент успешно завершен id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
    except Exception as ex:
        logger_bot_component_end.error(f'ER Компонент завершен с ошибкой id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)} \n Exception: {ex}')
        bot_info.comand_dict['error'][0]  += 1
        # Логирование ошибки в базу
        await add_error(ctx, 'participate_event_check', str(ex), bot_info.Erorr_message_standart)


# Уйти
@bot.component("leave_event")
async def button_leave_event(ctx: interactions.CommandContext):
    try:
        logger_bot_component_start.info(f'Зпущен компонент id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
        bot_info.comand_dict['leave_event'][0]  += 1
        # Функционал команды
        await button_leave_event_comand(ctx, logger_comand)
        logger_bot_component_end.info(f'Компонент успешно завершен id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
    except Exception as ex:
        logger_bot_component_end.error(f'ER Компонент завершен с ошибкой id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)} \n Exception: {ex}')
        bot_info.comand_dict['error'][0]  += 1
        # Логирование ошибки в базу
        await add_error(ctx, 'leave_event', str(ex), bot_info.Erorr_message_standart)


#  Рассылка личных сообщений
@bot.component("start_dm_mess")
async def button_start_dm_mess(ctx: interactions.CommandContext):
    try:
        logger_bot_component_start.info(f'Зпущен компонент id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
        bot_info.comand_dict['start_dm_mess'][0]  += 1
        # Функционал команды
        await button_start_dm_mess_comand(ctx, bot, logger_comand)
        logger_bot_component_end.info(f'Компонент успешно завершен id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
    except Exception as ex:
        logger_bot_component_end.error(f'ER Компонент завершен с ошибкой id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)} \n Exception: {ex}')
        bot_info.comand_dict['error'][0]  += 1
        # Логирование ошибки в базу
        await add_error(ctx, 'start_dm_mess', str(ex), bot_info.Erorr_message_standart)
       

# Запустить
@bot.component("start_event")
async def button_start_event(ctx: interactions.CommandContext):
    try:
        logger_bot_component_start.info(f'Зпущен компонент id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
        bot_info.comand_dict['start_event'][0]  += 1
        # Функционал команды
        await button_start_event_comand(ctx, bot, client, logger_comand)
        logger_bot_component_end.info(f'Компонент успешно завершен id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
    except Exception as ex:
        logger_bot_component_end.error(f'ER Компонент завершен с ошибкой id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)} \n Exception: {ex}')
        bot_info.comand_dict['error'][0]  += 1
        # Логирование ошибки в базу
        await add_error(ctx, 'start_event', str(ex), bot_info.Erorr_message_standart)
       

# Завершить
@bot.component("end_event")
async def button_end_event(ctx: interactions.CommandContext):
    try:
        logger_bot_component_start.info(f'Зпущен компонент id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
        bot_info.comand_dict['end_event'][0]  += 1
        # Функционал команды
        await button_end_event_comand(ctx, bot, logger_comand)
        logger_bot_component_end.info(f'Компонент успешно завершен id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
    except Exception as ex:
        logger_bot_component_end.error(f'ER Компонент завершен с ошибкой id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)} \n Exception: {ex}')
        bot_info.comand_dict['error'][0]  += 1
        # Логирование ошибки в базу
        await add_error(ctx, 'end_event', str(ex), bot_info.Erorr_message_standart)
       

# Список команд
@bot.component("participate_event_check_team")
async def button_participate_event_check_team(ctx: interactions.CommandContext):
    try:
        logger_bot_component_start.info(f'Зпущен компонент id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
        bot_info.comand_dict['participate_event_check_team'][0]  += 1
        # Функционал команды
        await button_participate_event_check_team_comand(ctx, logger_comand)
        logger_bot_component_end.info(f'Компонент успешно завершен id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
    except IndexError:
        await ctx.send('К сожалению на этом турнире нет участников)', ephemeral=True)
        logger_bot_component_end.info(f'Компонент успешно завершен id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
    except Exception as ex:
        logger_bot_component_end.error(f'ER Компонент завершен с ошибкой id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)} \n Exception: {ex}')
        bot_info.comand_dict['error'][0]  += 1
        # Логирование ошибки в базу
        await add_error(ctx, 'participate_event_check_team', str(ex), bot_info.Erorr_message_standart)
       
# Админский блок
@bot.command(
    name = 'send_log',
    description= 'Админская команда для выдачи лога по необходимости',
    default_member_permissions= interactions.Permissions.ADMINISTRATOR
)
async def send_log(ctx: interactions.CommandContext):

    try:
        logger_bot_component_start.info(f'Зпущен компонент id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
        bot_info.comand_dict['send_log'][0]  += 1
        # Функционал команды
        await send_log_comand(ctx, logger_comand)
        logger_bot_component_end.info(f'Компонент успешно завершен id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)}')
    except Exception as ex:
        logger_bot_component_end.error(f'ER Компонент завершен с ошибкой id_user: {int(ctx.user.id)}, discord_name: {str(ctx.member)} \n Exception: {ex}')
        bot_info.comand_dict['error'][0]  += 1
        # Логирование ошибки в базу
        await add_error(ctx, 'send_log', str(ex), bot_info.Erorr_message_standart)




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
    # Подключаем Log
    logger_bot_component_start, logger_bot_component_end, logger_comand, logger_bot = create_config_log()
    i = 0
    while i < 5:
        try:
            i += 1
            logger_bot.info('Бот запущен')
            # Запускаем одновременно 2 обрабочика событий с разный библиотек
            loop = asyncio.get_event_loop()

            # асинхронно запущенные таски кажеться ))
            task1 = loop.create_task(client.start(bot_info.TOKEN))
            task2 = loop.create_task(bot._ready())
            task3 = loop.create_task(schedule_start(bot=bot))
            
            # Кажеться обьединяет их и дает им работать одновременно
            gathered = asyncio.gather(task1, task2, task3)
            loop.run_until_complete(gathered)

        except Exception as ex:
            logger_bot.error(f'ER_0 Произошла ошибка в работе бота, итерация {i} \n Exception: {ex}')
            add_error_for_working_bot(0, i, 'Bot', 'Start_bot', str(ex))