# -*- coding: utf-8 -*-
import json
from bd_connection import execute_query

def old_to_new_bd():
    with open(r'/home/d/davidkue/davidkue.beget.tech/Data_Base.json', encoding="cp1251") as bd: # Поставить ссылку на бд
        users = json.load(bd)
    #user = json.dumps(templates, ensure_ascii=False)
    raiting_value_list = {
    "Железо 4":0,
    "Железо 3":100,
    "Железо 2":200,
    "Железо 1":300,
    "Бронза 4":400,
    "Бронза 3":500,
    "Бронза 2":600,
    "Бронза 1":700,
    "Серебро 4":800,
    "Серебро 3":900,
    "Серебро 2":1000,
    "Серебро 1":1100,
    "Серебро 1 ":1100, # Убрать
    "Золото 4":1200,
    "Золото 3":1300,
    "Золото 2":1400,
    "Золото 1":1500,
    "Платина 4":1600,
    "Платина 3":1700,
    "Платина 2":1800,
    "Платина 1":1900,
    "Алмаз 4":2000,
    "Алмаз 3":2100,
    "Алмаз 2":2200,
    "Алмаз 1":2300,
    "Мастер+":2500
    }
    for user_id, user in users.items():
        user_name = user[3].split('#')[0]
        argx = (user_id, user[0], user[1], raiting_value_list[user[1]], user[2][0], user[2][1], user[2][2], user[2][3], user[2][4], user_name)
        res = execute_query('add_user', argx)
        # Провека на ответ базы
        if isinstance(res, str):
            print(res)
    return

old_to_new_bd()