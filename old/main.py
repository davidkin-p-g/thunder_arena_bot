import discord
import datetime
import json
import os
import traceback

from bot_info import TOKEN_Test as TOKEN
from Add_Player import Add_Player
from Team_Comp import Team_Comp
import bot_info

client = discord.Client()
# v. 0.1
# v. 0.2
# v. 0.3

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        if message.content == bot_info.Event_say_start:
            await message.add_reaction('\N{THUMBS UP SIGN}')
            # Фиксанул для того что бы потом удалить при следующем этапе
            st = open('bot_status.json', 'r', encoding='utf-8')
            status = json.load(st)
            status['message_start_id'] = message.id
            st.close()
            st = open('bot_status.json', 'w', encoding='utf-8')
            json.dump(status, st, ensure_ascii=False, indent=4)
            st.close()
        if message.content == bot_info.Event_say_end_reg:
            # Фиксанул для того что бы потом удалить при следующем этапе
            st = open('bot_status.json', 'r', encoding='utf-8')
            status = json.load(st)
            status['message_end_reg_id'] = message.id
            st.close()
            st = open('bot_status.json', 'w', encoding='utf-8')
            json.dump(status, st, ensure_ascii=False, indent=4)
            st.close()
        return
    # для определения id канала
    elif message.content.startswith('кто я'):
        print(message.channel.id)
    # Хелпа для регистрации
    elif message.content.startswith('$info') and message.channel.id == bot_info.Reg_server_id:
        await message.channel.send(bot_info.info_to_reg)
    # Удаления предыдущего сообщения при ивенте
    elif message.channel.id == bot_info.Event_server_id:
        msg = await message.channel.fetch_message(message.id)
        await msg.delete()
    # Выгрузить файл с парнями
    elif message.content.startswith(bot_info.Get_file) and message.channel.id == bot_info.Admin_server_id:
        file = open('file.txt', 'w')
        db = open('Data_Base.json', 'r')
        DataBase = json.load(db)
        db.close()
        t = 0
        for i in DataBase.values():
            file.write(f'{t}) {i[0]}\n\n')
            t += 1
        file.close()
        await message.channel.send(file=discord.File('file.txt'))
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt')
        os.remove(path)
    # Выгрузить файл с полными данными о парнях
    elif message.content.startswith(bot_info.Get_all_file) and message.channel.id == bot_info.Admin_server_id:
        await message.channel.send(file=discord.File("Data_base.json"))

    #Выдать бын на регистрацию в событии
    elif message.content.startswith(bot_info.Ban) and message.channel.id == bot_info.Admin_server_id:
        # Определяю имя которое попадает под бан
        Command = message.content.split(' ')
        if len(Command) == 2:
            Ban_name = Command[1]
            db = open('Data_Base.json', 'r')
            DataBase = json.load(db)
            db.close()
            flag_ban = 0
            for key, value in DataBase.items():
                # Ищу есть ли он в базе
                if value[0] == Ban_name:
                    bl = open('Black_list.json', 'r')
                    BlackList = json.load(bl)
                    bl.close()
                    BlackList[key] = value
                    # Загружаю парня в черный список
                    bl = open('Black_list.json', 'w')
                    json.dump(BlackList, bl, ensure_ascii=False, indent=4)
                    bl.close()
                    flag_ban = 1
            if flag_ban:
                await message.channel.send(f'`{Ban_name} найден и успешно записан в черный список.`')
            else:
                await message.channel.send(f'`Игрока с UserName {Ban_name} не сущестует, или была допущена ошибка при вводе команды.`')
        else:
            await message.channel.send(
                f'`Была допущена ошибка при вводе команды.`')


    # Убрать бан на события
    elif message.content.startswith(bot_info.Razban) and message.channel.id == bot_info.Admin_server_id:
        # Определяю имя которое попадает под разбан
        Ban_name = message.content.split(' ')[1]
        bl = open('Black_list.json', 'r')
        BlackList = json.load(bl)
        bl.close()
        flag_ban = 0
        for key, value in BlackList.items():
            # Ищу есть ли он в черном списке
            if value[0] == Ban_name:
                del BlackList[key]
                # Обновлю черный сисок
                bl = open('Black_list.json', 'w')
                json.dump(BlackList, bl, ensure_ascii=False, indent=4)
                bl.close()
                flag_ban = 1
                break
        if flag_ban:
            await message.channel.send(f'`{Ban_name} найден и успешно удален из черного списка.`')
        else:
            await message.channel.send(
                f'`Игрока с UserName {Ban_name} нет в черном списке, или была допущена ошибка при вводе команды.`')

    # Создает События
    elif message.content.startswith(bot_info.Start_event) and message.channel.id == bot_info.Admin_server_id:
        # Проверяем наличие события
        st = open('bot_status.json', 'r', encoding='utf-8')
        status = json.load(st)
        if status['event'] == 0:
            # Создаем базу для события
            dt_start = str(datetime.datetime.now().isoformat('_', 'minutes'))
            dt_start = dt_start.replace(':', '_')
            dt_start = dt_start.replace('-', '_')
            dt_start = dt_start.replace('.', '_')
            f = open(f'Event_{dt_start}.json', 'w+', encoding='utf-8')
            event = {}
            json.dump(event, f, ensure_ascii=False, indent=4)
            f.close()
            # Запывывает базу для текущего события
            status['event_name'] = f'Event_{dt_start}.json'
            # Отмечаем начало события
            status['event'] = 1
            st.close()
            # Записывает в Бд
            st = open('bot_status.json', 'w', encoding='utf-8')
            json.dump(status, st, ensure_ascii=False, indent=4)
            st.close()
            # Отправляем сообщение о начале события в канал для события
            Event_channel = client.get_channel(bot_info.Event_server_id)
            await Event_channel.send(bot_info.Event_say_start)
        else:
            await message.channel.send('Событие уже запущено')

    # Завершает регистрацию на событие
    elif message.content.startswith(bot_info.End_reg_event) and message.channel.id == bot_info.Admin_server_id:
        # Проверяем наличие события
        st = open('bot_status.json', 'r', encoding='utf-8')
        status = json.load(st)
        if status['event'] == 1:
            # Отмечаем начало события
            status['event'] = 2
            Event_channel = client.get_channel(bot_info.Event_server_id)
            msg2 = await Event_channel.fetch_message(status['message_start_id'])
            await msg2.delete()
            st.close()
            # Записывает в Бд
            st = open('bot_status.json', 'w', encoding='utf-8')
            json.dump(status, st, ensure_ascii=False, indent=4)
            st.close()
            #Закидываем команды в чат
            st = open('bot_status.json', 'r', encoding='utf-8')
            status = json.load(st)
            st.close()
            Team_Comp(status['event_name'])
            tm = open('Team_Comp.json', 'r', encoding='utf-8')
            team = json.load(tm)
            for key, value in team.items():
                mess = f'   {key} \n'
                for i in value:
                    mess += f'{i[0]} Роль: {i[6]} \n'
                await Event_channel.send(f'''```{mess}```''')

            st = open('bot_status.json', 'r', encoding='utf-8')
            status = json.load(st)
            for i in status['zapas']:
                await Event_channel.send(f'''``` Игрок {i[1][0]} отправляется в запас```''')
            st.close()
            # Отправляем сообщение о окончании регистрации на события в канал для события
            Event_channel = client.get_channel(bot_info.Event_server_id)
            await Event_channel.send(bot_info.Event_say_end_reg)
        else:
            await message.channel.send('Событие еще не запущено')

    # Заканчивает событие
    elif message.content.startswith(bot_info.End_event) and message.channel.id == bot_info.Admin_server_id:
        # Проверяем наличие события
        st = open('bot_status.json', 'r', encoding='utf-8')
        status = json.load(st)
        if status['event'] == 2:
            # Отмечаем конец события
            status['event'] = 0
            # Удаляем сообщения о прохождении события
            Event_channel = client.get_channel(bot_info.Event_server_id)
            msg1 = await Event_channel.fetch_message(status['message_end_reg_id'])
            await msg1.delete()
            status['message_end_reg_id'] = ''
            status['message_start_id'] = ''
            st.close()
            # Записывает в Бд
            st = open('bot_status.json', 'w', encoding='utf-8')
            json.dump(status, st, ensure_ascii=False, indent=4)
            st.close()
            # Добавляем челикам игры в основной пул игроков
            db = open('Data_Base.json', 'r')
            DataBase = json.load(db)
            db.close()
            st = open('bot_status.json', 'r', encoding='utf-8')
            status = json.load(st)
            st.close()
            ev = open(status['event_name'], 'r', encoding='utf-8')
            event = json.load(ev)
            ev.close()
            for key in event.keys():
                DataBase[key][4] += 1
            db = open('Data_Base.json', 'w')
            json.dump(DataBase, db, ensure_ascii=False, indent=4)
            db.close()
            # Отправляем сообщение о окончании регистрации на события в канал для события
            Event_channel = client.get_channel(bot_info.Event_server_id)
            await Event_channel.send(bot_info.Event_say_end_event)
        else:
            await message.channel.send('Событие еще не запущено')
    # Общая регистрация
    elif message.channel.id == bot_info.Reg_server_id:  
        try:
            # Разбил на строки данных
            bot_info.Info_to_Prayer_arr = message.content.split('\n')
            bot_info.Info_to_Prayer_arr_to_Add = bot_info.Info_to_Prayer_arr.copy()
            # Разбил рейтинг на составляющие
            Rating_Player = bot_info.Info_to_Prayer_arr[1].split(' ')
            # Проверка на соответсвие UserName
            bot_info.flag_UserName = 1
            db = open('Data_Base.json', 'r')
            DataBase = json.load(db)
            db.close()
            for key, value in DataBase.items():
                if bot_info.Info_to_Prayer_arr[0] == value[0]:
                    if int(key) != int(message.author.id):
                        bot_info.flag_UserName = 0
            # Проверка на соответсвие рейтинга
            if Rating_Player[0] == bot_info.Rating_master:
                bot_info.flag_Rating_main = 1
                bot_info.flag_Rating_additional = 1
            else:
                if len(Rating_Player) == 2:
                    for i in bot_info.Rating_main:
                        # print(Rating_Player)
                        # print(Rating_Player[2])
                        if Rating_Player[0] == i:
                            bot_info.flag_Rating_main = 1
                    for i in bot_info.Rating_additional:
                        if Rating_Player[1] == i:
                            bot_info.flag_Rating_additional = 1
            # Разбил роли на составляющие
            Role_Player = bot_info.Info_to_Prayer_arr[2].split(' ')
            Role_Player_Arr = []

            # Проверка соответствия роли
            for r in Role_Player:
                if r in bot_info.Role[0]:
                    bot_info.flag_Role_top = 1
                    Role_Player_Arr.append('Топ')
                if r in bot_info.Role[1]:
                    bot_info.flag_Role_mid = 1
                    Role_Player_Arr.append('Мид')
                if r in bot_info.Role[2]:
                    bot_info.flag_Role_les = 1
                    Role_Player_Arr.append('Лес')
                if r in bot_info.Role[3]:
                    bot_info.flag_Role_adc = 1
                    Role_Player_Arr.append('Бот')
                if r in bot_info.Role[4]:
                    bot_info.flag_Role_sup = 1
                    Role_Player_Arr.append('Саппорт')
                if bot_info.flag_Role_top == 1 and bot_info.flag_Role_mid == 1 and bot_info.flag_Role_les == 1 \
                        and bot_info.flag_Role_adc == 1 and bot_info.flag_Role_sup == 1:
                    bot_info.Info_to_Prayer_arr_to_Add[2] = Role_Player_Arr

            if bot_info.flag_UserName:
                bot_info.Info_to_Prayer_arr[0] = f'+ UserName: {bot_info.Info_to_Prayer_arr[0]}'
            else:
                bot_info.Info_to_Prayer_arr[0] = f'- UserName: {bot_info.Info_to_Prayer_arr[0]}'

            if bot_info.flag_Rating_main and bot_info.flag_Rating_additional:
                bot_info.Info_to_Prayer_arr[1] = f'+ Rating: {bot_info.Info_to_Prayer_arr[1]}'
            else:
                bot_info.Info_to_Prayer_arr[1] = f'- Rating: {bot_info.Info_to_Prayer_arr[1]}'

            if bot_info.flag_Role_top and bot_info.flag_Role_mid and bot_info.flag_Role_les and bot_info.flag_Role_adc and bot_info.flag_Role_sup:
                bot_info.Info_to_Prayer_arr[2] = bot_info.Info_to_Prayer_arr[2].replace(' ', '->')
                bot_info.Info_to_Prayer_arr[2] = f'+ Role: {bot_info.Info_to_Prayer_arr[2]}'
            else:
                bot_info.Info_to_Prayer_arr[2] = f'- Role: {bot_info.Info_to_Prayer_arr[2]}'
            if bot_info.flag_Rating_main and bot_info.flag_Rating_additional and bot_info.flag_UserName \
                    and bot_info.flag_Role_top and bot_info.flag_Role_mid and bot_info.flag_Role_les \
                    and bot_info.flag_Role_adc and bot_info.flag_Role_sup:

                # Добавление В Список
                result = Add_Player(bot_info.Info_to_Prayer_arr_to_Add, message)

                if result:
                    bot_info.Info_to_Prayer_arr[2] += '\n Вы удачно зарегестрированы. Ждите распределения по командам.'
                else:
                    bot_info.Info_to_Prayer_arr[
                        2] += '\n Возникли ошибки при загрузке в базу данных. Сообщите администрации.'
            else:
                bot_info.Info_to_Prayer_arr[2] += '\n Возникли ошибки при заполнении полей. Повторите попытку.'

            # Обнуление флагов
            bot_info.flag_Rating_main = 0
            bot_info.flag_Rating_additional = 0
            bot_info.flag_UserName = 0
            bot_info.flag_Role_top = 0
            bot_info.flag_Role_mid = 0
            bot_info.flag_Role_les = 0
            bot_info.flag_Role_adc = 0
            bot_info.flag_Role_sup = 0

            await message.channel.send(f'''```diff
{bot_info.Info_to_Prayer_arr[0]}
{bot_info.Info_to_Prayer_arr[1]}
{bot_info.Info_to_Prayer_arr[2]}```''')

        except Exception:
            traceback.print_exc()
            await message.channel.send('```Произошла ошибка. Пожалуйста Зарегистрируйтесь корректно.```')

    # Канал для спама и получения информации о себе
    #message.channel.id == bot_info.Spam_server_id and
    elif message.content == bot_info.For_me:
        db = open('Data_Base.json', 'r')
        DataBase = json.load(db)
        db.close()
        if str(message.author.id) in DataBase:
            authorization = 'Авторизированый пользователь.'
            UserName = DataBase[str(message.author.id)][0]
            Rating = DataBase[str(message.author.id)][1]
            Role = ''
            for i in DataBase[str(message.author.id)][2]:
                if i == DataBase[str(message.author.id)][2][0]:
                    Role += str(i)
                else:
                    Role += f'->{str(i)}'
            Count = DataBase[str(message.author.id)][4]
            # Проверяем на наличие в черном списке что бы рассказать
            bl = open('Black_list.json', 'r')
            BlackList = json.load(bl)
            bl.close()
            if str(message.author.id) in BlackList:
                await message.channel.send(f'''```diff
        {str(message.author)}
{authorization}
Зарегистрированный UserName: {UserName}.
Зарегистрированный рейтинг: {Rating}.
Выбор ролей: {Role}.
Колличество сыгранных игр на платформе: {Count}.
-Вы находитесь в черном списке на регистрацию в событии.```''')
            else:
                st = open('bot_status.json', 'r', encoding='utf-8')
                status = json.load(st)
                st.close()
                if status['event'] == 1 or status['event'] == 2:
                    # Смотри участвует ли он в текущем событии
                    ev = open(status['event_name'], 'r', encoding='utf-8')
                    event = json.load(ev)
                    ev.close()
                    if str(message.author.id) in event:
                        await message.channel.send(f'''```diff
        {str(message.author)}
{authorization}
Зарегистрированный UserName: {UserName}.
Зарегистрированный рейтинг: {Rating}.
Выбор ролей: {Role}.
Колличество сыгранных игр на платформе: {Count}.
+Вы участвуете в текущем событии.```''')
                    # Не участвует
                    else:
                        await message.channel.send(f'''```diff
        {str(message.author)}
{authorization}
Зарегистрированный UserName: {UserName}.
Зарегистрированный рейтинг: {Rating}.
Выбор ролей: {Role}.
Колличество сыгранных игр на платформе: {Count}.
-Вы не участвуете в текущем событии.```''')
                # Нет события
                else:
                    await message.channel.send(f'''```md
            {str(message.author)} 
{authorization}
Зарегистрированный UserName: {UserName}.
Зарегистрированный рейтинг: {Rating}.
Выбор ролей: {Role}.
Колличество сыгранных игр на платформе: {Count}.
#           Сейчас событий нет.```''')
        # Не зарегистрирован
        else:
            await message.channel.send('''```Вы еще не зарагистрированы.```''')


@client.event
# Принять участие в событии
async def on_raw_reaction_add(payload):
    if client.user.id != payload.member.id:
        # Проверяем что эмоция нажата на правильно сообщении
        st = open('bot_status.json', 'r', encoding='utf-8')
        status = json.load(st)
        st.close()
        if payload.message_id == status['message_start_id'] and payload.emoji.name == bot_info.emoji:
            # Проверяем на наличие в черном списке
            bl = open('Black_list.json', 'r')
            BlackList = json.load(bl)
            bl.close()
            # Удаляем его реакцию
            if str(payload.user_id) in BlackList:
                user = payload.member
                messageid = payload.message_id
                message = await client.get_channel(payload.channel_id).fetch_message(messageid)
                for reaction in message.reactions:
                    await reaction.remove(user)

            else:
                # Ищем совпадения в базе данных
                db = open('Data_Base.json', 'r')
                DataBase = json.load(db)
                db.close()
                if str(payload.user_id) in DataBase:
                    # Достаем базу в память
                    ev = open(status['event_name'], 'r', encoding='utf-8')
                    event = json.load(ev)
                    ev.close()

                    # Записываем человечка в базу События
                    ev = open(status['event_name'], 'w', encoding='utf-8')
                    event[str(payload.user_id)] = DataBase[str(payload.user_id)]
                    json.dump(event, ev, ensure_ascii=False, indent=4)
                    ev.close()


@client.event
# Отказаться от участия в событии
async def on_raw_reaction_remove(payload):
    # Проверяем что не бот удаляет реакцию
    print(client.user.id ,payload)
    if client.user != payload.member:
        # Проверяем что эмоция убарана с правильного сообщения
        st = open('bot_status.json', 'r', encoding='utf-8')
        status = json.load(st)
        st.close()
        if payload.message_id == status['message_start_id'] and payload.emoji.name == bot_info.emoji:
            db = open('Data_Base.json', 'r')
            DataBase = json.load(db)
            db.close()
            if str(payload.user_id) in DataBase:
                # Достаем базу в память
                ev = open(status['event_name'], 'r', encoding='utf-8')
                event = json.load(ev)
                ev.close()

                # Выписываем человечка из базы События
                ev = open(status['event_name'], 'w', encoding='utf-8')
                if str(payload.user_id) in event:
                    del event[str(payload.user_id)]
                json.dump(event, ev, ensure_ascii=False, indent=4)
                ev.close()

client.run(TOKEN)
