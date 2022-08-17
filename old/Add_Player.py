import json


def Add_Player(info, mes):
    try:
        author = mes.author
        info.append(str(author))
        DataBase = {}
        info.append(0)
        info.append(0)

        try:
            fh = open('Data_Base.json', 'r')
            DataBase = json.load(fh)
            fh.close()
        except:
            print('Не удалось получить базу')

        DataBase.update({str(author.id): info})

        fh = open('Data_Base.json', 'w')
        json.dump(DataBase, fh,  ensure_ascii=False, indent=4)
        return 1
    except:
        return 0



