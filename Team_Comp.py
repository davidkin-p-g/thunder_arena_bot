# -*- coding: utf-8 -*-
import json
import random
import time
import copy

from bd_connection import execute_query
# 2 бот 
from discordpy import check_memeber_voice

def team_comp_def(user_to_event, missing_memeber):
    # fh = open(db_name, 'r', encoding='utf-8')  # Заменить на db_name
    # DataBase = json.load(fh)
    # fh.close()
    # Запихиваем данные в dict
    DataBase = {}
    for user in user_to_event:
        DataBase[user[0]] = [user[2], user[3], [user[4],user[5],user[6],user[7],user[8]], user[0]]
    # Определяем количесво команд
    #print(DataBase)
    Comand = len(DataBase) // 10
    Comand = Comand * 2
    Zapas = len(DataBase) % 10
    #print(f'Количесво команд: {Comand}')
    #print(f'Участноков в запасе: {Zapas}')
    Zapas_Name = []
    Base = DataBase.copy()
    # Добавление в запас опоздавших игроков
    # Если опоздавших БОЛЬШЕ чем нужно запасных
    if len(missing_memeber) > Zapas:
        for i in range(Zapas):
            k = random.choice(list(missing_memeber))
            name = Base[k]
            #print(f'Игрок {name[0]} с ключем {k}  и ролью {name[2][0]} отпраляется в запас.')
            Zapas_Name.append([k, name])
            del Base[k]
    # Если опоздавших МЕНЬШЕ ИЛИ РАВНО чем нужно запасных
    else:
        for i in missing_memeber:
            name = Base[i]
            #print(f'Игрок {name[0]} с ключем {i}  и ролью {name[2][0]} отпраляется в запас.')
            Zapas_Name.append([i, name])
            del Base[i]
        others_count = Zapas - len(missing_memeber)
        for i in range(others_count):
            k = random.choice(list(Base.keys()))
            name = Base[k]
            #print(f'Игрок {name[0]} с ключем {k}  и ролью {name[2][0]} отпраляется в запас.')
            Zapas_Name.append([k, name])
            del Base[k]
        
    # # Найдем невезучих запасников
    # for i in range(Zapas):
    #     k = random.choice(list(Base.keys()))
    #     name = Base[k]
    #     print(f'Игрок {name[0]} с ключем {k}  и ролью {name[2][0]} отпраляется в запас.')
    #     Zapas_Name.append([k, name])
    #     del Base[k]


    # Удалим их
    # for i in Zapas_Name:
    #     del Base[i[0]]
    role_to_num = {
        'Топ': 0,
        'Мид': 1,
        'Лес': 2,
        'Бот': 3,
        'Саппорт': 4,
    }
    # Разкидаем участников ао коробкам
    Korobki = [[[] for j in range(5)] for i in range(5)]
    k = 0
    #print(Base)
    for key, value in Base.items():
        j = 0
        for i in value[2]:
            Korobki[j][role_to_num[i]].append(key)
            k += 1
            j += 1

    role_comp = {
        'Топ': [],
        'Мид': [],
        'Лес': [],
        'Бот': [],
        'Саппорт': [],

    }
    role_comp_id = {
        'Топ': [],
        'Мид': [],
        'Лес': [],
        'Бот': [],
        'Саппорт': [],

    }
    Role = ['Топ', 'Мид', 'Лес', 'Бот', 'Саппорт']
    # i - рейтинг роли
    # j - поль
    for r in Role:
        i = 0
        while len(role_comp[r]) < Comand:
            while len(Korobki[i][role_to_num[r]]) > 0 and len(role_comp[r]) < Comand:
                player = random.choice(Korobki[i][role_to_num[r]])
                Base[player].append(r)
                role_comp[r].append(Base[player])
                role_comp_id[r].append(player)
                # Удаляю отовлюду
                for z in Korobki:
                    for x in z:
                        for c in x:
                            if c == player:
                                x.remove(c)
            i += 1

    #print(role_comp)
    # Определяем числовой коэффициент ранга
    Role_strong = {
        'Железо': 0,
        'Бронза': 400,
        'Серебро': 800,
        'Золото': 1200,
        'Платина': 1600,
        'Алмаз': 2000
    }
    reiting_player = 0
    # Поменял на циферки
    for j in role_comp.values():
        for i in j:
            if i[1] == 'Мастер+':
                i[1] = 2500
            else:
                role_name_arr = i[1].split(' ')
                role_name = role_name_arr[0]
                role_num = role_name_arr[1]
                i[1] = Role_strong[role_name] + (4 - int(role_num)) * 100
            reiting_player += i[1]

    # for key, i in role_comp.items():
    #     print(key, i)
    #print('Средний рейтинг игрока:')
    # if Comand != 0:
    #     # print(Comand)
    #     print(reiting_player / (Comand * 5))
    # else:
    #     print("Команд не собрано")

    # print('Средний рейтинг команды:')
    # if Comand != 0:
    #     print(reiting_player / Comand)
    # else:
    #     print("Команд не собрано")

    if Comand != 0:
        Sr_reit_team = reiting_player / Comand
    else:
        Sr_reit_team = 0
    role_comp_save = {}
    role_comp_save = copy.deepcopy(role_comp)

    timeout = 2
    reit = 0
    team_comp = {}
    while len(team_comp) != Comand:
        # Обновляем данные для попытки
        role_comp = copy.deepcopy(role_comp_save)
        team_comp = {}
        team_name = 1
        flag = 1
        timeout_start = time.time()
        # print(flag)
        # print(role_comp['Топ'])
        # print(role_comp_save['Топ'])
        while len(team_comp) < Comand:
            reit = 0
            while not (Sr_reit_team - 0.1 * Sr_reit_team < reit < Sr_reit_team + 0.1 * Sr_reit_team):
                # print(time.time(), timeout_start + timeout)
                # Генерю команду
                reit = 0
                top = (random.choice(role_comp['Топ']))
                mid = (random.choice(role_comp['Мид']))
                les = (random.choice(role_comp['Лес']))
                bot = (random.choice(role_comp['Бот']))
                sup = (random.choice(role_comp['Саппорт']))
                reit = top[1] + mid[1] + bot[1] + les[1] + sup[1]
                # print(reit)
                if time.time() > timeout_start + timeout:
                    flag = 0
                    break
            # Записываю команду
            if flag:
                team_comp[f'Команда {team_name}'] = [top, mid, bot, les, sup]
                #print(f'Команда {team_name} - {reit} сформирована')
                team_name += 1
                # Удаляю участников и пула
                # for i in role_comp['Топ']:
                #     print(i, top)
                #     if i == top:
                #         print('Есть блядь')
                role_comp['Топ'].remove(top)
                role_comp['Мид'].remove(mid)
                role_comp['Лес'].remove(les)
                role_comp['Бот'].remove(bot)
                role_comp['Саппорт'].remove(sup)
            if time.time() > timeout_start + timeout:
                print(1)
                break

    print("Zapas")
    print(Zapas_Name)
    print('Raspredelene')
    print(team_comp)
    return(Zapas_Name, team_comp, Comand)

def add_info_db(zapas_id, team_comps, id_event):
    db_er = False
    for user_id in zapas_id:
        argx = (user_id, id_event)
        res = execute_query('edit_reserve_user_to_event', argx)
        # Провека на ответ базы
        if isinstance(res, str):
            db_er = res
            #print(res)
            return res
    for user_id, value in team_comps.items():
        argx = (user_id, id_event, value[0], value[1])
        res = execute_query('edit_team_role_user_to_event', argx)
        # Провека на ответ базы
        if isinstance(res, str):
            db_er = res
            #print(res)
            return res  

    if isinstance(db_er, str):
        return db_er
    return True


def all_team_comp(user_to_event, permissions_administrator, id_event, client):
    # Запуск сторонего бота для провекри пользователей
    missing_memeber = check_memeber_voice(user_to_event, client)
    zapas_name, team_comps, comand_count = team_comp_def(user_to_event, missing_memeber)
    zapas_id = []
    for zapas in zapas_name:
        zapas_id.append(zapas[0])
    player_list = {}
    for team, users_team in team_comps.items():
        for user in users_team:
            player_list[user[3]] = [team, user[4]]
    print(f'zapas\n{zapas_id}')
    print(f'ychasniki\n{player_list}')

    res = add_info_db(zapas_id, player_list, id_event)
    if isinstance(res, str):
            return res
    return comand_count