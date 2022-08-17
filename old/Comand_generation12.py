import json
import random

DataBase = {}
fh = open('Data_Base.json', 'r')
DataBase = json.load(fh)
fh.close()

# Определяем количесво команд
Comand = len(DataBase) // 10
Comand = Comand * 2
Zapas = len(DataBase) % 10
print(f'Количесво команд: {Comand}')
print(f'Участноков в запасе: {Zapas}')
Zapas_Name = []

# Найдем невезучих запасников
for i in range(Zapas):
    k = random.choice(list(DataBase.keys()))
    name = DataBase[k]
    print(f'Игрок {name[0]} с ключем {k}  и ролью {name[2][0]} отпраляется в запас.')
    Zapas_Name.append([k, name])


Base = DataBase.copy()
for i in Zapas_Name:
    print(i[0])
    del Base[i[0]]
# Делим по 1 ролям
Top = []
Mid = []
Les = []
Bot = []
Sup = []

Top_dict = {}
Mid_dict = {}
Les_dict = {}
Bot_dict = {}
Sup_dict = {}
for key, value in Base.items():
    if value[2][0] == 'Топ':
        Top.append([value[0], value[1], value[2]])
        Top_dict['Топ'] = Top

    if value[2][0] == 'Мид':
        Mid.append([value[0], value[1], value[2]])
        Mid_dict['Мид'] = Mid

    if value[2][0] == 'Лес':
        Les.append([value[0], value[1], value[2]])
        Les_dict['Лес'] = Les

    if value[2][0] == 'Бот':
        Bot.append([value[0], value[1], value[2]])
        Bot_dict['Бот'] = Bot

    if value[2][0] == 'Саппорт':
        Sup.append([value[0], value[1], value[2]])
        Sup_dict['Саппорт'] = Sup

print(f'Всего {len(Top)} Топеров: {Top}')
print(f'Всего {len(Mid)} Мидеров: {Mid}')
print(f'Всего {len(Les)} Лесников: {Les}')
print(f'Всего {len(Bot)} Стрелков: {Bot}')
print(f'Всего {len(Sup)} Саппортов: {Sup}')

Player_dict = {
    'Топ': Top,
    'Мид': Mid,
    'Лес': Les,
    'Бот': Bot,
    'Саппорт': Sup,
}


Player = [Top, Mid, Les, Bot, Sup]
# Узнать сколько не хватет
Count = []
Cny = {}
Cny1 = []
rrt = {
    0: 'Топ',
    1: 'Мид',
    2: 'Лес',
    3: 'Бот',
    4: 'Саппорт'
}
oio = 0
for i in Player:
    if len(i) < Comand:
        Count.append(Comand - len(i))
    if len(i) > Comand:
        Cny[rrt[oio]] = len(i) - Comand
        Cny1.append(rrt[oio])
    oio += 1

print(Count)
print(Cny)
Izlichek = {}
Nedostatok = {}

for key, role in Player_dict.items():
    print(role)
    if len(role) > Comand:
        Izlichek[key] = role
    if len(role) < Comand:
        Nedostatok[key] = role

print(Izlichek)
print(Nedostatok)

# Izlichek_comp = []
#
# for p in Izlichek:
#     for i in p:
#
#         Izlichek_comp.append(i)
#
# print(Izlichek_comp)

# тут фор для 1 2 3 выбраной роли
new_role = []
raspr = []
ty = 0
for k in Nedostatok.keys():
    for ky, gh in Izlichek.items():
        for i in gh:
            if i[2][1] == k:
                raspr.append(i)
        #нельзя больше чем есть для роли
        if Count[ty] <= len(raspr):
            if Count[ty] <= Cny[ky]:
                new_role = random.sample(raspr, Cny[ky])
                for g in new_role:
                    print(f'добавил {g} на {k}')
                    Player_dict[k].append(g)
                    for hj in Player_dict.keys():
                        if hj == g[2][0] and hj != k:
                            Player_dict[hj].remove(g)
                            print(1)
                            print(Izlichek[ky])
            else:
                new_role = random.sample(raspr, Count[ty])
                for g in new_role:
                    print(f'добавилfd {g} на {k}')
                    Player_dict[k].append(g)
                    for hj in Player_dict.keys():
                        if hj == g[2][0] and hj != k:
                            Player_dict[hj].remove(g)
                            #Izlichek[ky].remove(g)

        else:
            new_role = raspr
            for g in new_role:
                Player_dict[k].append(g)
                for hj in Player_dict.keys():
                    if hj == g[2][0]:
                        Player_dict[hj].remove(g)
                        #Izlichek[ky].remove(g)
    ty += 1


for i in Player_dict.values():
    print(len(i))
ev = open('Test_comand.json', 'w')
json.dump(Player_dict, ev, ensure_ascii=False, indent=4)
ev.close()

# # Определяем числовой коэффициент ранга
# Role_strong = {
#     'Железо': 0,
#     'Бронза': 400,
#     'Серебро': 800,
#     'Золото': 1200,
#     'Платина': 1600,
#     'Алмаз': 2000
# }
#
# # Рассчитываем числовой рейтинг игроков
# for t in Top:
#     role_name_arr = t[1].split(' ')
#     role_name = role_name_arr[0]
#     role_num = role_name_arr[1]
#     t[1] = Role_strong[role_name] + (4 - int(role_num))*100
#
# for t in Mid:
#     role_name_arr = t[1].split(' ')
#     role_name = role_name_arr[0]
#     role_num = role_name_arr[1]
#     t[1] = Role_strong[role_name] + (4 - int(role_num))*100
#
# for t in Les:
#     role_name_arr = t[1].split(' ')
#     role_name = role_name_arr[0]
#     role_num = role_name_arr[1]
#     t[1] = Role_strong[role_name] + (4 - int(role_num))*100
#
# for t in Bot:
#     role_name_arr = t[1].split(' ')
#     role_name = role_name_arr[0]
#     role_num = role_name_arr[1]
#     t[1] = Role_strong[role_name] + (4 - int(role_num))*100
#
# for t in Sup:
#     role_name_arr = t[1].split(' ')
#     role_name = role_name_arr[0]
#     role_num = role_name_arr[1]
#     t[1] = Role_strong[role_name] + (4 - int(role_num))*100
#
# # print(f'Всего {len(Top)} Топеров: {Top}')
# # print(f'Всего {len(Mid)} Мидеров: {Mid}')
# # print(f'Всего {len(Les)} Лесников: {Les}')
# # print(f'Всего {len(Bot)} Стрелков: {Bot}')
# # print(f'Всего {len(Sup)} Саппортов: {Sup}')