import logging
import logging.config

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


    #Общий словать количесва использований использования
    comand_dict = {
        'registration':0,
        'rename':0,
        'rerating':0,
        'rerole':0,
        'me':0,
        'startevent':0,
        'participate_event':0,
        'participate_event_check':0,
        'leave_event':0,
        'start_dm_mess':0,
        'start_event':0,
        'end_event':0,
        'participate_event_check_team':0,
        'error':0
    }

    return logger_bot_component_start, logger_bot_component_end, logger_comand, logger_bot, comand_dict
