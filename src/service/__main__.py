import asyncio
import logging
from logging import config
from settings.logger import LOGGER_CONFIG
from settings import CONFIG
from datetime import datetime
from aiogram import executor
from service.bot import dp, send_message_to_channel


config.dictConfig(LOGGER_CONFIG)


async def execute() -> None:
    while True:
        await send_message_to_channel(msg=f'{datetime.now()}')
        await asyncio.sleep(3)


loop = asyncio.get_event_loop()
try:
    logging.info(f'Start service: {CONFIG.service.service_name}')
    asyncio.ensure_future(execute())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    logging.info(f'Stop service: {CONFIG.service.service_name}')
    loop.close()
