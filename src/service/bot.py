import logging
from settings import CONFIG

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from jinja2 import Environment
from jinja2 import PackageLoader
from jinja2 import select_autoescape


# Setup Jinja2 template necessities
env = Environment(loader=PackageLoader("service"), autoescape=select_autoescape())

bot = Bot(token=CONFIG.service.bot_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


async def send_message_to_channel(msg: str) -> None:
    logging.info(f'Send message to Chat: {CONFIG.service.chat_id}')
    await bot.send_message(chat_id=CONFIG.service.chat_id, text=msg)


async def recieve_message_from_queue() -> None:

    connection = await connect(CONFIG.rabbitmq.get_connection_url())

    async with connection:
        # Creating a channel
        channel = await connection.channel()

        # Declaring queue
        queue = await channel.declare_queue("queue_from_scheduler")

        # Start listening the queue with name 'hello'
        await queue.consume(on_message, no_ack=True)

        print(" [*] Waiting for messages. To exit press CTRL+C")
        await asyncio.Future()