# -*- coding: utf-8 -*-
import asyncio
from Comand_bot.send_log import send_log_comand
from datetime import datetime
# Смотеть тут 
# https://stackoverflow.com/questions/51530012/how-can-i-run-an-async-function-using-the-schedule-library

async def schedule_start(bot):
    '''
    3 поток для ежедневных событий (отправление лога)

    :ivar interactions.Client bot: Основной клиент запуска бота
    '''
    # Эта говнохуйня которая мне не нравиться
    while True:
        not_time = datetime.now()
        if not_time.hour == 19 and not_time.minute == 00:
            await send_log_comand(bot=bot)
            await asyncio.sleep(100)
        print(not_time)
        await asyncio.sleep(30)
        
        