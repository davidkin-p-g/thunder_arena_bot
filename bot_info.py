# -*- coding: utf-8 -*-



# public
TOKEN = 'OTk3MzE2NzMzNDk0ODg2NDMw.GCjcCY.MMhs-Ll8OhNn_FPER19k5sqjchosmX9q5lLpoM'
Url_thunder_bot_image = 'https://sun9-6.userapi.com/impg/VPL_ZewamRIpXzObdc6HkH9IrGqj1Qhwi4TFVA/tPz0kugQiQg.jpg?size=512x512&quality=95&sign=e28c07277daf159b451d0259091fb419&type=album'
role_id = 1024764824594415726
# # Конфиг базы
config = 'config.ini'
# Конфиг базы для работы с винды
#config = 'config_c4_db_debag.ini'
# Конфиг базы для работы с винды на своем базе
# config = 'config_debag.ini'
# Каналы для общей регистрации и проведения Событий
Reg_server_id = 930458995427270657
Event_server_id = 930459052906020896
Admin_server_id = 930459142961901598
Spam_server_id = 930459221508636712
everyone_id = 785864773887590420
log_channel_id = 930459142961901598
admin_dm_id = 298472656401989634
category_id = 785895738755907595


# # debug
# TOKEN= 'MTAxODI5NTYyODczODA3MjYzNA.Gqza5J.yA5JMJUK76p6DSSWTol46n4UEcXnDwgKewy1A4'
# Url_thunder_bot_image = 'https://sun9-61.userapi.com/impg/bzqNypaABZu6Mkmv4yo4Jhj2F9_8da6POPA4NA/CNwgzxZvv-A.jpg?size=511x511&quality=95&sign=bae5394587e5004fdf39074bb60c4646&type=album'
# role_id = 1020109545147727882
# # Конфиг базы
# # config = 'config_debag.ini'
# #Конфиг базы для бд на хоста
# config = 'config_c4_db_debag.ini'
# Reg_server_id = 929829439158747156
# Event_server_id = 930167181818343465
# Admin_server_id = 930179006903484456
# Spam_server_id = 930227903520706580
# everyone_id = 663569174831824948
# log_channel_id = 929829439158747156
# admin_dm_id = 178963010751168512
# category_id = 1034222694473932810


Info_to_Prayer_arr = []
Info_to_Prayer_arr_to_Add = []

Erorr_message_standart = 'ОЙОЙОЙ-АЙАЙАЙ Что то погло не так но не переживай, просто попробуй снова и если это не помогло расскажи администрации они мнея пнут.'

#Общий словать количесва использований использования
# [Всего использований, Использований во время последней выгрузки, Название метода]
comand_dict = {
    'registration':[0, 0, 'Регистрация'],
    'rename':[0, 0, 'Изминение Имени'],
    'rerating':[0, 0, 'Изменение рейтинга'],
    'rerole':[0, 0, 'Изменение роли'],
    'me':[0, 0, 'Узнать о себе'],
    'startevent':[0, 0, 'Запуск события'],
    'participate_event':[0, 0, 'Учавствовать в событии'],
    'participate_event_check':[0, 0, 'Проверка пользователей в событии'],
    'leave_event':[0, 0, 'Уйти с события'],
    'start_dm_mess':[0, 0, 'Разослать сообщение о начале события'],
    'start_event':[0, 0, 'Запустить событие'],
    'end_event':[0, 0, 'Закончить событие'],
    'participate_event_check_team':[0, 0, 'Проверка команд в событии'],
    'send_log':[0, 0, 'Вывод лога в дискорд'],
    'ban_member':[0, 0, 'Баны'], 
    'unban_member':[0, 0, 'РазБаны'], 
    'error':[0, 0, 'Ошибки']
}

# ЭТО ЛЕГЕНТААААААААААА
# member = interactions.Member(**await bot._http.get_member(member_id=int(users[0][0]), guild_id=663569174831824948), _client=bot._http)
# ЭТО ЛЕГЕНТААААААААААА



