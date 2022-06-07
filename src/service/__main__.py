import asyncio
import logging
from logging import config
from settings.logger import LOGGER_CONFIG
from settings import CONFIG
from datetime import datetime
from aiogram import executor
from service.bot import dp, send_message_to_channel
from service.models import Post


config.dictConfig(LOGGER_CONFIG)


async def execute() -> None:
    while True:
        logging.info('Start making message')
        post = Post(
            url='http://example.com',
            identifier='post_id',
            title='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
            date=datetime.now(),
            source='example_source'
        )
        # TODO: Read Post from QUEUE and send it
        logging.info('Start sending message')
        await send_message_to_channel(post=post)
        logging.info('Fall a sleep')
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
