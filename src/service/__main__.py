import asyncio
import logging
from logging import config
from settings.logger import LOGGER_CONFIG
from settings import CONFIG


config.dictConfig(LOGGER_CONFIG)


def main() -> None:
    logging.info(f'Service started, token: f{CONFIG.service.bot_token}')


if __name__ == '__main__':
    try:
        main()
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass
