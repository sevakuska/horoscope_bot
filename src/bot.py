import asyncio

from aiogram import Bot, Dispatcher

import config


async def main():
    bot = Bot(token=config.Settings().bot_token.get_secret_value())
    dispatcher = Dispatcher()
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
