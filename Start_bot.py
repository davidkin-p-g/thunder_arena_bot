# -*- coding: utf-8 -*-
from queue import Empty
from re import I
from time import sleep
import interactions


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

from bot_info import TOKEN_test as TOKEN
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

bot = interactions.Client(token=TOKEN)
# Кнопки меню участников

# Команда Регистрации нового пользователя
@bot.command(
    name="registration",
    description='''Регистрация нового пользователя системы.''',
    options=[
        interactions.Option(
            name='user_name',
            description = 'Имя пользователя на RU сервере с которым вы будете учавствовать в соревнованиях',
            type=interactions.OptionType.STRING,
            required=True
        ),
         interactions.Option(
            name='role_1',
            description = 'Роль №1 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
         interactions.Option(
            name='role_2',
            description = 'Роль №2 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
         interactions.Option(
            name='role_3',
            description = 'Роль №3 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
         interactions.Option(
            name='role_4',
            description = 'Роль №4 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
         interactions.Option(
            name='role_5',
            description = 'Роль №5 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
         interactions.Option(
            name='rating',
            description = 'Ваш нынешний уровень игры.',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Железо 4", value="Железо 4:0"),
                interactions.Choice(name="Железо 3", value="Железо 3:100"),
                interactions.Choice(name="Железо 2", value="Железо 2:200"),
                interactions.Choice(name="Железо 1", value="Железо 1:300"),
                interactions.Choice(name="Бронза 4", value="Бронза 4:400"),
                interactions.Choice(name="Бронза 3", value="Бронза 3:500"),
                interactions.Choice(name="Бронза 2", value="Бронза 2:600"),
                interactions.Choice(name="Бронза 1", value="Бронза 1:700"),
                interactions.Choice(name="Серебро 4", value="Серебро 4:800"),
                interactions.Choice(name="Серебро 3", value="Серебро 3:900"),
                interactions.Choice(name="Серебро 2", value="Серебро 2:1000"),
                interactions.Choice(name="Серебро 1", value="Серебро 1:1100"),
                interactions.Choice(name="Золото 4", value="Золото 4:1200"),
                interactions.Choice(name="Золото 3", value="Золото 3:1300"),
                interactions.Choice(name="Золото 2", value="Золото 2:1400"),
                interactions.Choice(name="Золото 1", value="Золото 1:1500"),
                interactions.Choice(name="Платина 4", value="Платина 4:1600"),
                interactions.Choice(name="Платина 3", value="Платина 3:1700"),
                interactions.Choice(name="Платина 2", value="Платина 2:1800"),
                interactions.Choice(name="Платина 1", value="Платина 1:1900"),
                interactions.Choice(name="Алмаз 4", value="Алмаз 4:2000"),
                interactions.Choice(name="Алмаз 3", value="Алмаз 3:2100"),
                interactions.Choice(name="Алмаз 2", value="Алмаз 2:2200"),
                interactions.Choice(name="Алмаз 1", value="Алмаз 1:2300"),
                interactions.Choice(name="Мастер+", value="Мастер+:2500"),
                ]
        )
    ]
)
async def registration_new(ctx, user_name, role_1, role_2, role_3, role_4, role_5, rating):
    try:
        # Проверка на канал использования
        if ctx.channel_id != bot_info.Event_server_id:
            # Проверка ролей
            if not check_role(role_1, role_2, role_3, role_4, role_5):
                await ctx.send('Роли не могут повторяться', ephemeral=True)
            else:
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
                        await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
                        # Логирование ошибки в базу
                        argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'registration', res)
                        execute_query('add_error', argx)
                        print(res)      
                else:
                    # Выдадим роль Учатника
                    await ctx.author.add_role(bot_info.role_id, ctx.guild_id)
                    # Компановка сообщения
                    message = change_message(ctx.author, user_name, rating, role_1, role_2, role_3, role_4, role_5, 'Новый пользователь')
                    await ctx.send(embeds=message, ephemeral=True)
        else:
            await ctx.send('В этом канале нельзя произвести регистрацию', ephemeral=True)
    except Exception as ex:
        await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
        # Логирование ошибки в базу
        argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'registration', str(ex))
        execute_query('add_error', argx)
        print(ex)


# Команда изменения Ника пользователя
@bot.command(
    name="rename",
    description='''Изменение имени пользователя на RU сервере.''',
    options=[
        interactions.Option(
            name='user_name',
            description = 'Новое имя пользователя на RU сервере с которым вы будете учавствовать в соревнованиях',
            type=interactions.OptionType.STRING,
            required=True
        ),
    ]
)
async def rename(ctx: interactions.CommandContext, user_name):
    try:
        # Проверка на канал использования
        if ctx.channel_id != bot_info.Event_server_id:
            # Получаем имеющиеся данные о пользователе по id
            argx = (int(ctx.user.id),)
            users = execute_query('check_user', argx)
            for user_iterator in users:
                user = user_iterator.fetchall()
            # Обрабаотываем ошибку
            if user == []:
                await ctx.send('Вы еще не зарегистрированы', ephemeral=True)
            else:
                # Явно обзовем перемнные для лучшей читаемости
                rating, rating_value, role_1, role_2, role_3, role_4, role_5, ban = user[0][2], user[0][3],user[0][4], user[0][5], user[0][6], user[0][7],user[0][8],user[0][9]
                # Полученные пареметры
                argx = (int(ctx.user.id), user_name, rating, rating_value, role_1, role_2, role_3, role_4, role_5, ban)
                # Сейв в бд
                res = execute_query('edit_user', argx)
                if isinstance(res, str):
                    # Добавлять новые обнаруденые баги через if else
                    await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
                    # Логирование ошибки в базу
                    argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'rename', res)
                    execute_query('add_error', argx)  
                    print(res)      
                else:
                    # Компановка сообщения
                    message = change_message(ctx.author, user_name, rating,  role_1, role_2, role_3, role_4, role_5, 'UserName изменено')
                    await ctx.send(embeds=message, ephemeral=True)
        else:
            await ctx.send('В этом канале нельзя произвести изменение имени', ephemeral=True)
    except Exception as ex:
        await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
        # Логирование ошибки в базу
        argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'rename', str(ex))
        execute_query('add_error', argx)
        print(ex)

# Команда изменения Рейтинга пользователя
@bot.command(
    name="rerating",
    description='''Изменение Рейтинга.''',
    options=[
        interactions.Option(
            name='rating',
            description = 'Ваш нынешний уровень игры.',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Железо 4", value="Железо 4:0"),
                interactions.Choice(name="Железо 3", value="Железо 3:100"),
                interactions.Choice(name="Железо 2", value="Железо 2:200"),
                interactions.Choice(name="Железо 1", value="Железо 1:300"),
                interactions.Choice(name="Бронза 4", value="Бронза 4:400"),
                interactions.Choice(name="Бронза 3", value="Бронза 3:500"),
                interactions.Choice(name="Бронза 2", value="Бронза 2:600"),
                interactions.Choice(name="Бронза 1", value="Бронза 1:700"),
                interactions.Choice(name="Серебро 4", value="Серебро 4:800"),
                interactions.Choice(name="Серебро 3", value="Серебро 3:900"),
                interactions.Choice(name="Серебро 2", value="Серебро 2:1000"),
                interactions.Choice(name="Серебро 1", value="Серебро 1:1100"),
                interactions.Choice(name="Золото 4", value="Золото 4:1200"),
                interactions.Choice(name="Золото 3", value="Золото 3:1300"),
                interactions.Choice(name="Золото 2", value="Золото 2:1400"),
                interactions.Choice(name="Золото 1", value="Золото 1:1500"),
                interactions.Choice(name="Платина 4", value="Платина 4:1600"),
                interactions.Choice(name="Платина 3", value="Платина 3:1700"),
                interactions.Choice(name="Платина 2", value="Платина 2:1800"),
                interactions.Choice(name="Платина 1", value="Платина 1:1900"),
                interactions.Choice(name="Алмаз 4", value="Алмаз 4:2000"),
                interactions.Choice(name="Алмаз 3", value="Алмаз 3:2100"),
                interactions.Choice(name="Алмаз 2", value="Алмаз 2:2200"),
                interactions.Choice(name="Алмаз 1", value="Алмаз 1:2300"),
                interactions.Choice(name="Мастер+", value="Мастер+:2500"),
                ]
        )
    ]
)
async def rerating(ctx: interactions.CommandContext, rating):
    try:
        # Проверка на канал использования
        if ctx.channel_id != bot_info.Event_server_id:
            # Деление на рейтинг и его числовой жквивалент
            rating_player = rating.split(':')
            # Получаем имеющиеся данные о пользователе по id
            argx = (int(ctx.user.id),)
            users = execute_query('check_user', argx)
            for user_iterator in users:
                user = user_iterator.fetchall()
            # Обрабаотываем ошибку
            if user == []:
                await ctx.send('Вы еще не зарегистрированы', ephemeral=True)
            else:
                # Явно обзовем перемнные для лучшей читаемости
                user_name, rating, rating_value, role_1, role_2, role_3, role_4, role_5, ban = user[0][1], rating_player[0], int(rating_player[1]),user[0][4], user[0][5], user[0][6], user[0][7],user[0][8],user[0][9]
                # Полученные пареметры
                argx = (int(ctx.user.id), user_name, rating, rating_value, role_1, role_2, role_3, role_4, role_5, ban)
                # Сейв в бд
                res = execute_query('edit_user', argx)
                if isinstance(res, str):
                    # Добавлять новые обнаруденые баги через if else
                    await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
                    # Логирование ошибки в базу
                    argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'rerating', res)
                    execute_query('add_error', argx)  
                    print(res)      
                else:
                    # Компановка сообщения
                    message = change_message(ctx.author, user_name, rating,  role_1, role_2, role_3, role_4, role_5, 'Рейтинг Изменен')
                    await ctx.send(embeds=message, ephemeral=True)
        else:
            await ctx.send('В этом канале нельзя произвести изменение рейтинга', ephemeral=True)
    except Exception as ex:
        await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
        # Логирование ошибки в базу
        argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'rerating', str(ex))
        execute_query('add_error', argx)
        print(ex)

# Команда изменения Роли пользователя
@bot.command(
    name="rerole",
    description='''Изменение расстановки ролей.''',
    options=[
        interactions.Option(
            name='role_1',
            description = 'Роль №1 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
         interactions.Option(
            name='role_2',
            description = 'Роль №2 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
         interactions.Option(
            name='role_3',
            description = 'Роль №3 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
         interactions.Option(
            name='role_4',
            description = 'Роль №4 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
         interactions.Option(
            name='role_5',
            description = 'Роль №5 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
    ]
)
async def rerole(ctx: interactions.CommandContext, role_1, role_2, role_3, role_4, role_5):
    try:
        # Проверка на канал использования
        if ctx.channel_id != bot_info.Event_server_id:
            if not check_role(role_1, role_2, role_3, role_4, role_5):
                await ctx.send('Роли не могут повторяться', ephemeral=True)
            else:
                # Получаем имеющиеся данные о пользователе по id
                argx = (int(ctx.user.id),)
                users = execute_query('check_user', argx)
                for user_iterator in users:
                    user = user_iterator.fetchall()
                # Обрабаотываем ошибку
                if user == []:
                    await ctx.send('Вы еще не зарегистрированы', ephemeral=True)
                else:
                    # Явно обзовем перемнные для лучшей читаемости
                    user_name, rating, rating_value, ban = user[0][1], user[0][2], user[0][3], user[0][9]
                    # Полученные пареметры
                    argx = (int(ctx.user.id), user_name, rating, rating_value, role_1, role_2, role_3, role_4, role_5, ban)
                    # Сейв в бд
                    res = execute_query('edit_user', argx)
                    if isinstance(res, str):
                        # Добавлять новые обнаруденые баги через if else
                        await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
                        # Логирование ошибки в базу
                        argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'rerole', res)
                        execute_query('add_error', argx)  
                        print(res)      
                    else:
                        # Компановка сообщения
                        message = change_message(ctx.author, user_name, rating, role_1, role_2, role_3, role_4, role_5, 'Выбор ролей изменен')
                        await ctx.send(embeds=message, ephemeral=True)
        else:
            await ctx.send('В этом канале нельзя произвести изменение ролей', ephemeral=True)
    except Exception as ex:
        await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
        # Логирование ошибки в базу
        argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'rerole', str(ex))
        execute_query('add_error', argx)
        print(ex)

#ME
@bot.command(
    name="me",
    description='''Информация о себе''',
)
async def me(ctx: interactions.CommandContext):
    try:
        # Проверка на канал использования
        if ctx.channel_id != bot_info.Event_server_id:
            # Получаем имеющиеся данные о пользователе по id
            argx = (int(ctx.user.id),)
            users = execute_query('check_user_to_me', argx)
            # Обрабаотываем ошибку
            if isinstance(users, str):
                # Добавлять новые обнаруденые баги через if else
                await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
                # Логирование ошибки в базу
                argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'me', users)
                execute_query('add_error', argx)  
                print(users)
                return
            for user_iterator in users:
                user = user_iterator.fetchall()
            # Обрабаотываем ошибку
            if user == []:
                await ctx.send('Вы еще не зарегистрированы', ephemeral=True)
            else:
                # Компановка сообщения
                message = me_message(user)
                await ctx.send(embeds=message)
        else:
            await ctx.send('В этом канале нельзя использовать me', ephemeral=True)
    except Exception as ex:
        await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
        # Логирование ошибки в базу
        argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'me', str(ex))
        execute_query('add_error', argx)
        print(ex)

@bot.command(
    name = 'startevent',
    description= '''Запустить новое событие.
    Канал использования admin.''',
    default_member_permissions= interactions.Permissions.ADMINISTRATOR,
    options=[
    interactions.Option(
        name='event_type',
        description = 'Тип события',
        type=interactions.OptionType.STRING,
        required=True,
        choices=[
            interactions.Choice(name="Потасовка", value="Потасовка"),
            interactions.Choice(name="Командный", value="Командный"),
        ]
    ),
    interactions.Option(
            name='event_name',
            description = 'Название события',
            type=interactions.OptionType.STRING,
            required=True,
        ),
    interactions.Option(
            name='event_description',
            description = 'Описание события',
            type=interactions.OptionType.STRING,
            required=True,
        ),
    interactions.Option(
            name='event_date_start',
            description = 'Время старта события. Формат времени: YYYY-MM-DD hh:mm:ss',
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
    
)
async def startevent(ctx: interactions.CommandContext, event_type, event_name, event_description, event_date_start):
    try:
        # Проверка на канал использования
        if ctx.channel_id == bot_info.Event_server_id:
            # Так как я не могу получить нормальный id сообщения до его отправки 
            # а хочеться сразу несколько событий запускать я пердпринял радикальное действо
            # и отправляю сообщение а уже потом пишу в базу

            # Компановка сообщения
            message = startevent_message(event_type, event_name, event_description, event_date_start)
            await ctx.send(embeds=message, components=row)
            #raise Exception("Some exception")
            # Полученные пареметры
            argx = (int(ctx.message.id), event_type, event_name, event_description, event_date_start)
            # Сейв в бд
            res = execute_query('add_event', argx)
            if isinstance(res, str):
                # Добавлять новые обнаруденые баги через if else
                await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
                # Логирование ошибки в базу
                argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'startevent', res)
                execute_query('add_error', argx)  
                print(res)
        else:
            await ctx.send('В этом канале нельзя запустить событие', ephemeral=True)
    except Exception as ex:
        await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
        # Логирование ошибки в базу
        argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'startevent', str(ex))
        execute_query('add_error', argx)
        print(ex)

# Обработка кнопок события
# Учавствовать
@bot.component("participate_event")
async def button_participate_event(ctx: interactions.CommandContext):
    try:
        # Получаем имеющиеся данные о пользователе по id
        argx = (int(ctx.user.id),)
        users = execute_query('check_user', argx)
        for user_iterator in users:
            user = user_iterator.fetchall()
        # Обрабаотываем ошибку
        if user == []:
            await ctx.send('Вы еще не зарегистрированы', ephemeral=True)
        else:
            # Проверяем на изменение Discord имени
            if ctx.author.name != user[0][10]:
                # Полученные пареметры
                argx = (int(ctx.user.id), ctx.author.name)
                # Сейв в бд
                res = execute_query('edit_user_discord_name', argx)
                if isinstance(res, str):
                    # Добавлять новые обнаруденые баги через if else
                    await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
                    # Логирование ошибки в базу
                    argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'edit_user_discord_name', res)
                    execute_query('add_error', argx)  
                    print(res) 
            # Полученные пареметры
            argx = (int(ctx.message.id), int(ctx.user.id))
            # Сейв в бд
            res = execute_query('add_user_to_event', argx)
            if isinstance(res, str):
                # Добавлять новые обнаруденые баги через if else
                if res == "error '1644 (45000): Уже зарегестрирован' occurred":
                        await ctx.send('Вы уже зарегестрированы в этом событии', ephemeral=True)
                    # Добавлять новые обнаруденые баги
                else:
                    await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
                    # Логирование ошибки в базу
                    argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'participate_event', res)
                    execute_query('add_error', argx)    
            else:
                await ctx.send('Вы зарегистрировались на событие', ephemeral=True)
    except Exception as ex:
        await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
        # Логирование ошибки в базу
        argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'participate_event', str(ex))
        execute_query('add_error', argx)
        print(ex)

#Кто учавствует
@bot.component("participate_event_check")
async def button_check(ctx: interactions.CommandContext):
    try:
        # Получаем имеющиеся данные о пользователе по id
        argx = (int(ctx.user.id),)
        users = execute_query('check_user', argx)
        for user_iterator in users:
            user = user_iterator.fetchall()
        # Обрабаотываем ошибку
        if user == []:
            await ctx.send('Вы еще не зарегистрированы', ephemeral=True)
        else:
            # Полученные пареметры
            argx = (int(ctx.message.id),)
            # Сейв в бд
            res = execute_query('all_user_to_event', argx)
            if isinstance(res, str):
                # Добавлять новые обнаруденые баги через if else
                await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
                # Логирование ошибки в базу
                argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'participate_event_check', res)
                execute_query('add_error', argx)  
                print(res)      
            else:
                for user_to_events in res:
                    user_to_event = user_to_events.fetchall()
                # Провека прав мембера
                # Полюбому можно лучге но я не справился
                permissions = str(ctx.member.permissions).split('|')
                permissions_administrator = False
                for permissions_iterator in permissions:
                    if permissions_iterator == 'ADMINISTRATOR':
                        permissions_administrator = True
                embed = users_to_event_message(user_to_event, permissions_administrator)
                await ctx.send(embeds=embed, ephemeral=True)
    except IndexError:
        await ctx.send('Нет участников. Стань первым))', ephemeral=True)
    except Exception as ex:
        await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
        # Логирование ошибки в базу
        argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'participate_event_check', str(ex))
        execute_query('add_error', argx)
        print(ex)

# Уйти
@bot.component("leave_event")
async def button_leave(ctx: interactions.CommandContext):
    try:
        # Получаем имеющиеся данные о пользователе по id
        argx = (int(ctx.user.id),)
        users = execute_query('check_user', argx)
        for user_iterator in users:
            user = user_iterator.fetchall()
        # Обрабаотываем ошибку
        if user == []:
            await ctx.send('Вы еще не зарегистрированы', ephemeral=True)
        else:
            # Полученные пареметры
            argx = (int(ctx.message.id), int(ctx.user.id))
            # Сейв в бд
            res = execute_query('delete_user_to_event', argx)
            if isinstance(res, str):
                # Добавлять новые обнаруденые баги через if else
                if res == "error '1644 (45000): Еще не зарегестрирован' occurred":
                        await ctx.send('Вы еще не зарегестрированы в этом событии', ephemeral=True)
                    # Добавлять новые обнаруденые баги
                else:
                    await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
                    # Логирование ошибки в базу
                    argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'leave_event', res)
                    execute_query('add_error', argx)  
                    print(res)      
            else:
                await ctx.send('Вы больше не зарегистрированы в этом событии', ephemeral=True)
    except Exception as ex:
        await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
        # Логирование ошибки в базу
        argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'leave_event', str(ex))
        execute_query('add_error', argx)
        print(ex)    

# Запустить
@bot.component("start_event")
async def button_start_event(ctx: interactions.CommandContext):
    try:
        # Провека прав мембера
        # Полюбому можно лучге но я не справился
        permissions = str(ctx.member.permissions).split('|')
        permissions_administrator = False
        for permissions_iterator in permissions:
            if permissions_iterator == 'ADMINISTRATOR':
                permissions_administrator = True
        if not permissions_administrator:
            await ctx.send('Вы не администратор', ephemeral=True)
            return
        # Получаем параметры События
        argx = (int(ctx.message.id),)
        res = execute_query('check_event', argx)
        # Проверка на бдшную ошибку
        if isinstance(res, str):
                # Добавлять новые обнаруденые баги через if else
                await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
                # Логирование ошибки в базу
                argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'start_event', res)
                execute_query('add_error', argx)  
                print(res)
                return
        # Вытаскиваем инфу о событии
        for res_iterator in res:
            event = res_iterator.fetchall()
        if event == []:
            await ctx.send('Такого События не сушествует(что невозможно, как это вообще произошло ?? Кому то придеться работать ))', ephemeral=True)
            # Логирование ошибки в базу
            argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'start_event', 'Несуществующий эвент')
            execute_query('add_error', argx)  
            print(res)
            return
        # Проверка статуса события
        if event[0][6] == 0:
             await ctx.send('Событие уже закончилось', ephemeral=True)
             return
        if event[0][6] == 2:
             await ctx.send('Событие уже запущено', ephemeral=True)
             return
        # Изменяем статус события
        # Полученные пареметры
        id_event, date_start, type, event_name, status = int(ctx.message.id), event[0][2], event[0][3], event[0][4], 2
        argx = (id_event, date_start, type, event_name, status)
        # Сейв в бд
        res = execute_query('edit_event', argx)
        if isinstance(res, str):
            # Добавлять новые обнаруденые баги через if else
            await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
            # Логирование ошибки в базу
            argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'start_event', res)
            execute_query('add_error', argx)  
            print(res)      
        else:
            # Полученные пареметры
            argx = (int(ctx.message.id),)
            # Сейв в бд
            res = execute_query('all_user_to_event', argx)
            if isinstance(res, str):
                # Добавлять новые обнаруденые баги через if else
                await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
                # Логирование ошибки в базу
                argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'start_event', res)
                execute_query('add_error', argx)  
                print(res)      
            else:
                for user_to_events in res:
                    user_to_event = user_to_events.fetchall()
                # Провека прав мембера
                # Полюбому можно лучге но я не справился
                permissions = str(ctx.member.permissions).split('|')
                permissions_administrator = False
                for permissions_iterator in permissions:
                    if permissions_iterator == 'ADMINISTRATOR':
                        permissions_administrator = True
                all_team_comp(user_to_event, permissions_administrator, int(ctx.message.id))
                if isinstance(res, str):
                    # Добавлять новые обнаруденые баги через if else
                    await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
                    # Логирование ошибки в базу
                    argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'start_event', res)
                    execute_query('add_error', argx)  
                    print(res)
                    return
                type, event_name, event_description = event[0][3], event[0][4], event[0][5]
                embed = startevent_go_message(type, event_name, event_description)
                await ctx.message.edit(embeds=embed, components=row1)
    except Exception as ex:
        await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
        # Логирование ошибки в базу
        argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'start_event', str(ex))
        execute_query('add_error', argx)
        print(ex)   

# Завершить
@bot.component("end_event")
async def button_end_event(ctx: interactions.CommandContext):
    try:
        # Провека прав мембера
        # Полюбому можно лучге но я не справился
        permissions = str(ctx.member.permissions).split('|')
        permissions_administrator = False
        for permissions_iterator in permissions:
            if permissions_iterator == 'ADMINISTRATOR':
                permissions_administrator = True
        if not permissions_administrator:
            await ctx.send('Вы не администратор', ephemeral=True)
            return
        # Получаем параметры События
        argx = (int(ctx.message.id),)
        res = execute_query('check_event', argx)
        # Проверка на бдшную ошибку
        if isinstance(res, str):
                # Добавлять новые обнаруденые баги через if else
                await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
                # Логирование ошибки в базу
                argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'end_event', res)
                execute_query('add_error', argx)  
                print(res)
                return
        # Вытаскиваем инфу о событии
        for res_iterator in res:
            event = res_iterator.fetchall()
        if event == []:
            await ctx.send('Такого События не сушествует(что невозможно, как это вообще произошло ?? Кому то придеться работать ))', ephemeral=True)
            # Логирование ошибки в базу
            argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'end_event', 'Несуществующий эвент')
            execute_query('add_error', argx)  
            print(res)
            return
        # Проверка статуса события
        if event[0][6] == 0:
             await ctx.send('Событие уже закончилось', ephemeral=True)
             return
        if event[0][6] == 1:
             await ctx.send('Событие еще не началось', ephemeral=True)
             return
        # Изменяем статус события
        # Полученные пареметры
        id_event, date_start, type, event_name, status = int(ctx.message.id), event[0][2], event[0][3], event[0][4], 0
        argx = (id_event, date_start, type, event_name, status)
        # Сейв в бд
        res = execute_query('edit_event', argx)
        if isinstance(res, str):
            # Добавлять новые обнаруденые баги через if else
            await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
            # Логирование ошибки в базу
            argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'end_event', res)
            execute_query('add_error', argx)  
            print(res)      
        else:          
            type, event_name, event_description = event[0][3], event[0][4], event[0][5]
            embed = startevent_end_message(type, event_name, event_description)
            await ctx.message.edit(embeds=embed, components=row2)
    except Exception as ex:
        await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
        # Логирование ошибки в базу
        argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'end_event', str(ex))
        execute_query('add_error', argx)
        print(ex)

# Список команд
@bot.component("participate_event_check_team")
async def button_check_team(ctx: interactions.CommandContext):
    try:
        # Получаем имеющиеся данные о пользователе по id
        argx = (int(ctx.user.id),)
        users = execute_query('check_user', argx)
        for user_iterator in users:
            user = user_iterator.fetchall()
        # Обрабаотываем ошибку
        if user == []:
            await ctx.send('Вы еще не зарегистрированы', ephemeral=True)
        else:
            # Полученные пареметры
            argx = (int(ctx.message.id),)
            # Сейв в бд
            res = execute_query('all_user_to_event_team', argx)
            if isinstance(res, str):
                # Добавлять новые обнаруденые баги через if else
                await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
                # Логирование ошибки в базу
                argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'participate_event_check', res)
                execute_query('add_error', argx)  
                print(res)      
            else:
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
    except IndexError:
        await ctx.send('К сожалению на этом турнире нет участников)', ephemeral=True)
    except Exception as ex:
        await ctx.send('Произошла непредвиденная ошибка пожалуйста сообщите администрации', ephemeral=True)
        # Логирование ошибки в базу
        argx = (int(ctx.user.id), str(ctx.channel), str(ctx.member), 'participate_event_check', str(ex))
        execute_query('add_error', argx)
        print(ex)
#Админский блок сервисная часть

# Баны пользователей может еще сколько игр сыграл
@bot.command(
    name = 'check_channel',
    description= 'Админская команда для определения id канала',
    default_member_permissions= interactions.Permissions.ADMINISTRATOR

)
async def check_channel(ctx: interactions.CommandContext):
    
    await ctx.send(str(ctx.channel_id))


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
            member = interactions.Member(**await bot._http.get_member(member_id=int(user[0]), guild_id=663569174831824948), _client=bot._http)
            # ЭТО ЛЕГЕНТААААААААААА
            await member.add_role(bot_info.role_id, ctx.guild_id)
            await ctx.send(f'{i} {user[1]} присвоена роль', ephemeral=True)
        except:
            await ctx.send(f'{i} {user[1]} не найден', ephemeral=True)
        sleep(2)
        i+=1
    await ctx.send('Мы закончили ))', ephemeral=True)

    await ctx.send(member.id, ephemeral=True)
    # for user in users:
    #     await ctx.send(f'{i} {user[0]}', ephemeral=True)
    #     sleep(1)
    #     i+=1
    interactions.api.http.member.MemberRequest
    interactions.Member

# Кнокпи для события
button_participate_event = interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Участвовать",
    custom_id="participate_event",
)

button_participate_event_disabled= interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Участвовать",
    custom_id="participate_event_disabled",
    disabled=True
)

button_participate_event_check= interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Список участников",
    custom_id="participate_event_check",
)

button_participate_event_check_team= interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Список Команд",
    custom_id="participate_event_check_team",
)

button_leave_event= interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Уйти",
    custom_id="leave_event",
)

button_leave_event_disabled= interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Уйти",
    custom_id="leave_event_disabled",
    disabled=True
)

button_start_event= interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Запустить",
    custom_id="start_event",
)

button_end_event= interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Завершить",
    custom_id="end_event",
)
button_end_event_disabled= interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Завершено",
    custom_id="end_event_disabled",
    disabled=True
)


row = interactions.ActionRow(
    components=[button_participate_event, button_participate_event_check, button_leave_event, button_start_event]
)
row1 = interactions.ActionRow(
    components=[button_participate_event_disabled, button_participate_event_check_team, button_leave_event_disabled, button_end_event]
)
row2 = interactions.ActionRow(
    components=[button_participate_event_disabled, button_participate_event_check_team, button_leave_event_disabled, button_end_event_disabled]
)

if __name__ == '__main__':
    bot.start()
