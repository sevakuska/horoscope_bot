import asyncio

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from handler import Handler


async def on_startup(dispatcher: Dispatcher):
    pass


def main():
    bot = Bot(TOKEN)
    storage = MemoryStorage()
    dispatcher = Dispatcher(bot, storage=storage)
    handler = Handler(bot, dispatcher)
    handler.register_message_handlers()
    handler.register_callback_handlers()
    executor.start_polling(
        dispatcher=dispatcher,
        on_startup=on_startup,
        skip_updates=True
    )


if __name__ == '__main__':
    main()
