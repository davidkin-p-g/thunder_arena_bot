import json


def Add_Player_test(info, key):
    try:

        info.append(str(info[0]))
        DataBase = {}
        role = info[2].split(' ')
        info[2] = role
        try:
            fh = open('Data_Base.json', 'r')
            DataBase = json.load(fh)
            fh.close()
        except:
            print('Не удалось получить базу')

        DataBase.update({str(key): info})
        print(DataBase)

        fh = open('Data_Base.json', 'w')
        json.dump(DataBase, fh,  ensure_ascii=False, indent=4)
        return 1
    except:
        return 0




