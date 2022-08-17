['balberchik', 'Золото 2', 'Мид Саппорт Топ Бот Лес']
import random
import bot_info
from Add_Player_test import Add_Player_test

u = 0
for n in range(46):

    test = ['balberchik', 'Золото 2', 'Мид Саппорт Топ Бот Лес', '1']
    # Имя
    word = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z']
    name = ''
    for i in range(6):
        name +=word[random.randint(0,18)]
    test[0] = name

    #Ранг
    test[1] = f'{bot_info.Rating_main[random.randint(0,5)]} {random.randint(1,4)}'

    #Роль
    rrr = random.sample([0, 1, 2, 3, 4], 5)
    test[2] = f'{bot_info.Role[rrr[0]]} {bot_info.Role[rrr[1]]} {bot_info.Role[rrr[2]]} {bot_info.Role[rrr[3]]} {bot_info.Role[rrr[4]]}'

    #Номер для сортировки
    test[3] = u

    #Ключ
    key = ''
    for i in range(18):
        key += str(random.randint(0, 9))

    Add_Player_test(test, key)
    u  += 1

