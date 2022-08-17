import json
import random
import time
import copy


def Team_Comp(db_name):
    fh = open(db_name, 'r', encoding='utf-8')  # Заменить на db_name
    DataBase = json.load(fh)
    fh.close()

    # Определяем количесво команд
    Comand = len(DataBase) // 10
    Comand = Comand * 2
    Zapas = len(DataBase) % 10
    print(f'Количесво команд: {Comand}')
    print(f'Участноков в запасе: {Zapas}')
    Zapas_Name = []
    Base = DataBase.copy()

    # Найдем невезучих запасников
    for i in range(Zapas):
        k = random.choice(list(Base.keys()))
        name = Base[k]
        print(f'Игрок {name[0]} с ключем {k}  и ролью {name[2][0]} отпраляется в запас.')
        Zapas_Name.append([k, name])
        del Base[k]
    st = open('bot_status.json', 'r', encoding='utf-8')
    status = json.load(st)
    status['zapas'] = Zapas_Name
    st.close()

    st = open('bot_status.json', 'w', encoding='utf-8')
    json.dump(status, st, ensure_ascii=False, indent=4)
    st.close()

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
    print(Base)
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

    # for key, i in role_comp.items():
    #     print(key, i)
    # ev = open('Test_comand.json', 'w', encoding='utf-8')
    # json.dump(role_comp, ev, ensure_ascii=False, indent=4)
    # ev.close()
    print(role_comp)
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
    print('Средний рейтинг игрока:')
    if Comand != 0:
        # print(Comand)
        print(reiting_player / (Comand * 5))
    else:
        print("Команд не собрано")

    print('Средний рейтинг команды:')
    if Comand != 0:
        print(reiting_player / Comand)
    else:
        print("Команд не собрано")

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
                print(f'Команда {team_name} - {reit} сформирована')
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

    #team_comp['zapas'] = Zapas_Name
    ev = open('Team_Comp.json', 'w', encoding='utf-8')
    json.dump(team_comp, ev, ensure_ascii=False, indent=4)
    ev.close()


# Запасные игроки нету
# st = open('bot_status.json', 'r', encoding='utf-8')
# status = json.load(st)
# Team_Comp(status['event_name'])
# st.close()