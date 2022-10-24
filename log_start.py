# -*- coding: utf-8 -*-

import logging
import logging.config
from datetime import date





from bot_info import comand_dict as info_dict

def create_config_log():
    """
    Подробнее здесь http://docs.python.org/howto/logging.html#configuring-logging
    """

    # Конфиг логера
    log_name = 'Bot_all_log.log'

    dictLogConfig = {
        "version":1,
        "handlers":{
            "fileHandler_bot_component_start":{
                "class":"logging.FileHandler",
                "formatter":"bot_component_start",
                "encoding":"utf-8",
                "filename":f"{log_name}"
            },
            "fileHandler_bot_component_end":{
                "class":"logging.FileHandler",
                "formatter":"bot_component_end",
                "encoding":"utf-8",
                "filename":f"{log_name}"
            },
            "fileHandler_comand":{
                "class":"logging.FileHandler",
                "formatter":"comand",
                "encoding":"utf-8",
                "filename":f"{log_name}"
            },
            "fileHandler_bot":{
                "class":"logging.FileHandler",
                "formatter":"bot",
                "encoding":"utf-8",
                "filename":f"{log_name}"
            }
        },
        "loggers":{
            "BotComponentStart":{
                "handlers":["fileHandler_bot_component_start"],
                "level":"DEBUG",
            },
            "BotComponentEnd":{
                "handlers":["fileHandler_bot_component_end"],
                "level":"DEBUG",
            },
            "Comand":{
                "handlers":["fileHandler_comand"],
                "level":"DEBUG",
            },
            "Bot":{
                "handlers":["fileHandler_bot"],
                "level":"DEBUG",
            },
        },
        "formatters":{
            "bot_component_start":{
                "format":"%(asctime)s\n%(levelname)s - %(name)s - %(funcName)s - %(message)s"
            },
            "bot_component_end":{
                "format":"%(levelname)s - %(name)s - %(funcName)s - %(message)s"
            },
            "comand":{
                "format":"%(levelname)s - %(lineno)d - %(message)s"
            },
            "bot":{
                "format":"%(asctime)s\n%(levelname)s - %(name)s - %(message)s"
            },
        }
    }
    
    # Логеры
    logging.config.dictConfig(dictLogConfig)
    logger_bot_component_start = logging.getLogger("BotComponentStart")
    logger_bot_component_end = logging.getLogger("BotComponentEnd")
    logger_comand = logging.getLogger("Comand")
    logger_bot = logging.getLogger("Bot")

    return logger_bot_component_start, logger_bot_component_end, logger_comand, logger_bot
    
        


def create_result_log():

    with open("Bot_result_log.log", "w",encoding='utf-8' ) as Bot_result_log:

        len_table = 120
        # Строим 1 строку - гапка таблицы с выравниванием
        line = f'Срез использованных ресуров за {date.today()}'
        count_whole = (len_table - len(line)) // 2
        count_remainder = (len_table - len(line)) % 2
        zero_line = ' ' * (count_whole) + line + ' ' * (count_whole + count_remainder) 
        Bot_result_log.write(f'{zero_line}\n')

        # # Линия таблицы
        table_line = '-' * len_table

        Bot_result_log.write(f'{table_line}\n')
        # Название столбцов
        line_1 = 'Название методов'
        count_whole_1 = ((len_table // 2) - len(line_1)) // 2
        count_remainder_1 = ((len_table // 2) - len(line_1)) % 2

        line_2 = 'Общее число вызовов (С последнего файла)'
        count_whole_2 = ((len_table // 2) - len(line_2)) // 2
        count_remainder_2 = ((len_table // 2) - len(line_2)) % 2

        value_line = '--' + ' ' * (count_whole_1 - 2) + line_1 + ' ' * (count_whole_1 + count_remainder_1 - 1) + '--' + ' ' * (count_whole_2 - 1) + line_2 + ' ' * (count_whole_2 + count_remainder_2 - 2) + '--'
        Bot_result_log.write(f'{value_line}\n')
        Bot_result_log.write(f'{table_line}\n')

        
        # Таблица
        i = 0
        i_1 = 0
        for item in info_dict.values():
            if item[2] != 'Ошибки':
                i += item[0]
                i_1 += item[0] - item[1]
            else:
                er = item[0]
                er_1 = item[0] - item[1]

            line_1 = f'{item[2]}'
            count_whole_1 = ((len_table // 2) - len(line_1)) // 2
            count_remainder_1 = ((len_table // 2) - len(line_1)) % 2

            line_2 = f'{item[0]} ({item[0] - item[1]})'
            count_whole_2 = ((len_table // 2) - len(line_2)) // 2
            count_remainder_2 = ((len_table // 2) - len(line_2)) % 2

            value_line = '--' + ' ' * (count_whole_1 - 2) + line_1 + ' ' * (count_whole_1 + count_remainder_1 - 1) + '--' + ' ' * (count_whole_2 - 1) + line_2 + ' ' * (count_whole_2 + count_remainder_2 - 2) + '--'
            Bot_result_log.write(f'{value_line}\n')
            Bot_result_log.write(f'{table_line}\n')

            # Сохраняем предыдущий результат
            item[1] = item[0]

        # Итог
        line_1 = "Всего / Ошибок %"
        count_whole_1 = ((len_table // 2) - len(line_1)) // 2
        count_remainder_1 = ((len_table // 2) - len(line_1)) % 2

        if i != 0:
            # Общее количество
            all = float(er)/float(i)
            all = float('{:.3f}'.format(all))
            # С последнего вызова
            if i_1 != 0:

                all_1 = float(er_1)/float(i_1)
                all_1 = float('{:.3f}'.format(all))

                line_2 = f'{i} ({i_1}) / {all} ({all_1}) %'
            else:
                line_2 = f'{i} (0) / {all} (0) %'
        else:
            line_2 = f'{i} (0) / 0 (0) %'
        count_whole_2 = ((len_table // 2) - len(line_2)) // 2
        count_remainder_2 = ((len_table // 2) - len(line_2)) % 2

        value_line = '--' + ' ' * (count_whole_1 - 2) + line_1 + ' ' * (count_whole_1 + count_remainder_1 - 1) + '--' + ' ' * (count_whole_2 - 1) + line_2 + ' ' * (count_whole_2 + count_remainder_2 - 2) + '--'
        Bot_result_log.write(f'{value_line}\n')
        Bot_result_log.write(f'{table_line}\n')



