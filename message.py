# -*- coding: utf-8 -*-
from dataclasses import fields
import interactions
from bot_info import Url_thunder_bot_image

# Изменение имени
def change_message(author, user_name, rank, role_1, role_2, role_3, role_4, role_5, comand):
    embed = interactions.Embed(
            color=0x1100fa,
            title=f"{comand}",
            description=f"Инициатор Запроса: {str(author)}",
            footer= interactions.EmbedFooter(text="По всем вопросам обращаться к администрации\nПишем ботов. По вопросам @Suglinca#6900"),
            fields=[
                interactions.EmbedField(
                name="UserName:",
                value=f"{user_name}",
                inline=True,
                ),
                interactions.EmbedField(
                    name="Рейтинг:",
                    value=f"{rank}",
                    inline=True,
                ),
                interactions.EmbedField(
                    name="Выбор ролей:",
                    value=f"{role_1}->{role_2}->{role_3}->{role_4}->{role_5}",
                    inline=False,
                )
            ],
    )
    message = embed
    return message
# ME
def me_message(user_events):
    fields_embed=[
                interactions.EmbedField(
                name="UserName:",
                value=f"{user_events[0][1]}",
                inline=True,
                ),
                interactions.EmbedField(
                    name="Рейтинг:",
                    value=f"{user_events[0][2]}({user_events[0][3]})",
                    inline=True,
                ),
                interactions.EmbedField(
                    name="Выбор ролей:",
                    value=f"{user_events[0][4]}->{user_events[0][5]}->{user_events[0][6]}->{user_events[0][7]}->{user_events[0][8]}",
                    inline=False,
                )
            ]
    if user_events[0][10] is None:
        field1 = interactions.EmbedField(
                    name="Всего игр:",
                    value=f"0",
                    inline=False,
                )
        field2 = interactions.EmbedField(
                    name="Актуальные события:",
                    value=f"Вы не участвуете ни в одном событии",
                    inline=False,
                )
    else:    
        len = 0
        event = ''
        for user_event in user_events:
            len += 1
            if user_event[14] == 1: # регистрация
                if user_event[15] < 0: # время прошло 
                    event = event + f' **Событие** {user_event[11]} Проходит регистрация.\n Уже скоро начало будьте готовы\n\n'
                else:
                    day = user_event[15]//86400
                    ost = user_event[15]%86400
                    hour = ost//3600
                    ost = ost%3600
                    min = ost//60
                    sec = ost%60
                    event = event + f' **Событие** {user_event[11]} Проходит регистрация.\nДо начала {day} день {hour} час {min} минут {sec} секунд\n\n'
            elif user_event[14] == 2: # игра идет
                if user_event[15] is None:
                    event = event + f' **Событие** {user_event[11]} УЖЕ ИДЕТ.\n Вы в запасе.\n\n'
                else:
                    event = event + f' **Событие** {user_event[11]} УЖЕ ИДЕТ.\n Ваша команда {user_event[12]}  роль {user_event[13]}.\n\n'
        if event == '':
            event = 'Вы не участвуете ни в одном событии'
        field1 = interactions.EmbedField(
                    name="Всего игр:",
                    value=f"{len}",
                    inline=False,
                )
        field2 = interactions.EmbedField(
                    name="Актуальные события:",
                    value=f"{event}",
                    inline=False,
                )
    # Поле с баном
    field3 = interactions.EmbedField(
                    name="Вы били забанены.",
                    value=f"Причина: {user_event[17]}",
                    inline=False,
                )
    fields_embed.append(field1)
    fields_embed.append(field2)
    if user_event[16] == 1:
        fields_embed.append(field3)
    embed = interactions.Embed(
            color=0x344059,
            title=f"ME",
            description=f"Инициатор Запроса: {user_events[0][9]}",
            footer= interactions.EmbedFooter(text="По всем вопросам обращаться к администрации\nПишем ботов. По вопросам @Suglinca#6900"),
            fields=fields_embed
    )
    message = embed
    return message

# Создание события
def startevent_message(event_type, event_name, event_description, event_date_start, dm_flag=0):
    date_time = str(event_date_start).split(' ')
    date = date_time[0]
    time = date_time[1]
    month = date.split('-')[2]
    day = date.split('-')[1]
    hour = time.split(':')[0]
    minute = time.split(':')[1]
    if dm_flag == 0:
        field = fields=[
                interactions.EmbedField(
                name="Время начала",
                value=f"{month}.{day}/{hour}:{minute}",
                inline=True,
                )
            ]
    else:
        field = [
                interactions.EmbedField(
                name="Проверка на готовность",
                value="На данные момент обьявлена проверка на готовность. Всем учасникам необходимо собраться в голсовом канале события",
                inline=True,
                ),
                interactions.EmbedField(
                name="Время начала",
                value=f"{month}.{day}/{hour}:{minute}",
                inline=True,
                ),
            ]
    embed = interactions.Embed(
            thumbnail=interactions.EmbedImageStruct(url=Url_thunder_bot_image),
            color=0x344059,
            title=f"Событие {event_type} {event_name}", #Проверка на готовность всем учасникам собраться в голосовом канале события
            description=f"{event_description}",
            footer= interactions.EmbedFooter(text="По всем вопросам обращаться к администрации\nПишем ботов. По вопросам @Suglinca#6900"),
            fields=field
    )
    message = embed
    return message

# Событие началось
def startevent_go_message(event_type, event_name, event_description):
    embed = interactions.Embed(
            thumbnail=interactions.EmbedImageStruct(url=Url_thunder_bot_image),
            color=0x4F638C,
            title=f"Событие {event_type} {event_name} |УЖЕ НАЧАЛОСЬ| ",
            description=f"{event_description}",
            footer= interactions.EmbedFooter(text="По всем вопросам обращаться к администрации\nПишем ботов. По вопросам @Suglinca#6900"),
            fields=[
                interactions.EmbedField(
                name="Время начала",
                value=f"Сейчас",
                inline=True,
                ),
                interactions.EmbedField(
                name="Посмотреть игры можно на Twitch",
                value=f"https://www.twitch.tv/thunderarena",
                inline=True,
                )
            ],
    )
    message = embed
    return message

# Событие закончилось
def startevent_end_message(event_type, event_name, event_description):
    embed = interactions.Embed(
            thumbnail=interactions.EmbedImageStruct(url=Url_thunder_bot_image),
            color=0xC1C7D9,
            title=f"Событие {event_type} {event_name} |К сожалению завершено| ",
            description=f"{event_description}",
            footer= interactions.EmbedFooter(text="По всем вопросам обращаться к администрации\nПишем ботов. По вопросам @Suglinca#6900"),
            fields=[
                interactions.EmbedField(
                name="Время начала",
                value=f"Событие завершено",
                inline=True,
                ),
                interactions.EmbedField(
                name="Посмотреть повтор можно на Twitch",
                value=f"https://www.twitch.tv/thunderarena",
                inline=True,
                )
            ],
    )
    message = embed
    return message

# Список участников
def users_to_event_message(user_to_event, admin= False):
    event_name = user_to_event[0][1]
    users_count = len(user_to_event)
    fields_embed = []
    users_block_count = 5
    for i in range(0,users_count,users_block_count):
        field = interactions.EmbedField(
            name="-------------------------------",
            inline=False,
            )
        val = ''
        for j in range(users_block_count):
            if i +j < users_count:
                if admin:
                    val = val + f"**{user_to_event[i+j][2]}**   {user_to_event[i+j][3]}||{user_to_event[i+j][4]}/{user_to_event[i+j][5]}/{user_to_event[i+j][6]}/{user_to_event[i+j][7]}/{user_to_event[i+j][8]}||\n"
                else:
                    val = val + f"**{user_to_event[i+j][2]}**\n"
        field.value = val
        fields_embed.append(field)

    embed = interactions.Embed(
            color=0x1100fa,
            title=f"Список участников в событии {event_name} (Не является распределением по командам, оно будет позже)",
            description=f"На данный момент участников: {users_count}",
            footer= interactions.EmbedFooter(text="По всем вопросам обращаться к администрации.\nСписок может быть не полным если количество участников больше 125.\nПишем ботов. По вопросам @Suglinca#6900"),
            fields=fields_embed,
    )
    message = embed
    return message

# Список команд
def users_to_event_team_message(user_to_event, admin= False):
    event_name = user_to_event[0][1]
    users_count = len(user_to_event)
    fields_embed = []
    users_team_start = 0
    users_block_count = 5

    field = interactions.EmbedField(
            name="Запасные",
            inline=False,
            )
    val = ''

    while user_to_event[users_team_start][3] is None:
        if admin:
            val = val + f"**{user_to_event[users_team_start][12]}** **{user_to_event[users_team_start][2]}** {user_to_event[users_team_start][4]}({user_to_event[users_team_start][5]}) ||{user_to_event[users_team_start][7]}/{user_to_event[users_team_start][8]}/{user_to_event[users_team_start][9]}/{user_to_event[users_team_start][10]}/{user_to_event[users_team_start][11]}||\n"
        else:
            val = val + f"**{user_to_event[users_team_start][2]}**\n"
        users_team_start += 1
        if users_team_start >= users_count:
            break
    if val == '':
        val = 'Запасных нет'
    field.value = val
    fields_embed.append(field)
        
    for i in range(users_team_start, users_count, users_block_count):
        field = interactions.EmbedField(
            name=f"{user_to_event[i][3]}",
            inline=False,
            )
        val = ''
        for j in range(users_block_count):
            if i +j < users_count:
                if admin:
                    val = val + f"**{user_to_event[i+j][12]}** **{user_to_event[i+j][2]}**   {user_to_event[i+j][4]}({user_to_event[i+j][5]}) {user_to_event[i+j][6]}\n"
                else:
                    val = val + f"**{user_to_event[i+j][12]}** **{user_to_event[i+j][2]}** {user_to_event[i+j][6]}\n"
        field.value = val
        fields_embed.append(field)

    embed = interactions.Embed(
            color=0x1100fa,
            title=f"Список Команд в событии {event_name}",
            description=f"Всего участников: {users_count}",
            footer= interactions.EmbedFooter(text="По всем вопросам обращаться к администрации.\nСписок может быть не полным если количество участников больше 125.\nПишем ботов. По вопросам @Suglinca#6900"),
            fields=fields_embed,
    )
    message = embed
    return message

# Ban
def ban_message(author, discord_name, reason):
    embed = interactions.Embed(
            color=0xff0000,
            title=f"Пользователь получил БАН",
            footer= interactions.EmbedFooter(text="По всем вопросам обращаться к администрации\nПишем ботов. По вопросам @Suglinca#6900"),
            fields=[
                interactions.EmbedField(
                name="Пользователь",
                value=f"{discord_name}",
                inline=True,
                ),
                interactions.EmbedField(
                name="Причина",
                value=f"{reason}",
                inline=True,
                ),
                interactions.EmbedField(
                name="Инициатор",
                value=f"{author}",
                inline=True,
                )
            ],
    )
    message = embed
    return message

# Ban
def unban_message(author, discord_name, reason):
    embed = interactions.Embed(
            color=0x11ff00,
            title=f"Пользователь получил РАЗБАН",
            footer= interactions.EmbedFooter(text="По всем вопросам обращаться к администрации\nПишем ботов. По вопросам @Suglinca#6900"),
            fields=[
                interactions.EmbedField(
                name="Пользователь",
                value=f"{discord_name}",
                inline=True,
                ),
                interactions.EmbedField(
                name="Причина",
                value=f"{reason}",
                inline=True,
                ),
                interactions.EmbedField(
                name="Инициатор",
                value=f"{author}",
                inline=True,
                )
            ],
    )
    message = embed
    return message
