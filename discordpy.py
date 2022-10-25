# -*- coding: utf-8 -*-
import imp
import discord
from logging import Logger

def check_memeber_voice(user_to_event, client, logger_comand: Logger):
    try:
        # id канала
        id_event_voice_channel=user_to_event[0][9]
        channel = client.get_channel(id_event_voice_channel)
        members = channel.voice_states.keys()
        print(f'{members}')
        # Определяем не пришедгих участников
        missing_members = []
        for user in user_to_event:
            if user[0] not in  members:
                missing_members.append(user[0])
        # Завершаем работу бота
        logger_comand.debug('Сгенерировали список отсутствующих учасников')
        error = ''
        return missing_members, error
    except:
        logger_comand.warning('Не удалось сгенерировать список отсутствующих')
        error = 'Произошла не критическая ошибка с определением участников в голосовм канале, теперь жто не будет влиять на распределение'
        return [], error

