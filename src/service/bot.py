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
template = env.get_template("post.html")


# Setup aiogram bot settings
bot = Bot(token=CONFIG.service.bot_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


async def send_message_to_channel(msg: str) -> None:
    # for post in results:
    # await message.answer(template.render(post))
    logging.info(f'Send message to Chat: {CONFIG.service.chat_id}')
    await bot.send_message(chat_id=CONFIG.service.chat_id, text=msg)
