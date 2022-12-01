# -*- coding: utf-8 -*-

import interactions
from interactions.ext.files import command_send
from logging import Logger
import shutil
from datetime import date
import os
import bot_info

from log_start import create_result_log



async def send_log_comand(ctx: interactions.CommandContext = None, logger_comand: Logger = None, bot = None):
    '''
    Отправить лог(Comand_bot/send_log.py). Передать парметры изначальной функции бота.

    :ivar interactions.CommandContext ctx: Контекст команды
    :ivar interactions.Client bot: Основной клиент запуска бота
    :ivar Logger logger_comand: Клас логера обрабочика
    '''
    create_result_log()
    if logger_comand is not None:
        logger_comand.debug('Сгенерировали результырующий лог')

    # Создаем пустые фалы для передачи лога
    with open(f'Bot_all_log_{date.today()}.log', 'tw', encoding='utf-8') as f:
        pass
    with open(f'Bot_result_log_{date.today()}.log', 'tw', encoding='utf-8') as f:
        pass
    if logger_comand is not None:
        logger_comand.debug('Создали дубляры файлов')

    # Копируем остновной лог в новые файлы
    shutil.copyfile('Bot_all_log.log', f'Bot_all_log_{date.today()}.log')
    shutil.copyfile('Bot_result_log.log', f'Bot_result_log_{date.today()}.log')
    if logger_comand is not None:
        logger_comand.debug('Скопировали лог в дубляры')

    # Компануем файлы
    file_all = interactions.File(filename=f'Bot_all_log_{date.today()}.log')
    file_res = interactions.File(filename=f'Bot_result_log_{date.today()}.log')
    if logger_comand is not None:
        logger_comand.debug('Создали библиотечные файлы')

    # Отправляем файлы
    if ctx is not None:
        # Командный вызов
        await command_send(ctx, files=[file_res, file_all])
    else:
        # Временной вызов
        log_channel = interactions.Channel(**await bot._http.get_channel(channel_id=bot_info.log_channel_id), _client=bot._http)
        await log_channel.send(f'-----Файлы за {date.today()}-----', files=[file_res, file_all])
    if logger_comand is not None:
        logger_comand.debug('Отправили файлы')

    # Удаляем файлы
    os.remove(f'Bot_all_log_{date.today()}.log')
    os.remove(f'Bot_result_log_{date.today()}.log')
    if logger_comand is not None:
        logger_comand.debug('Удалили файлы')
