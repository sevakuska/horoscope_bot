from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text

from keyboard import Keyboard
import horoscope


class Handler:
    def __init__(self, bot: Bot, dispatcher: Dispatcher):
        self.__bot = bot
        self.__dispatcher = dispatcher
    
    async def __handle_start_command(self, message: Message):
        await self.__bot.send_message(
            chat_id=message.from_user.id,
            text='Привет, Я бот, который отправляет гороскопы :)',
            reply_markup=Keyboard.get_menu()
        )

    async def __handle_horoscope_command(self, message: Message):
        await self.__bot.send_message(
            chat_id=message.from_user.id,
            text='Выберите знак зодиака',
            reply_markup=Keyboard.get_inline_horoscope_menu()
        )
    
    async def __handle_callback_horoscope_sign(self, callback: CallbackQuery):
        sign = callback.data
        prediction = await horoscope.get_horoscope(sign)
        await self.__bot.send_message(
            chat_id=callback.from_user.id,
            text=prediction
        )
        await callback.answer(cache_time=0)

    def register_message_handlers(self):
        self.__dispatcher.register_message_handler(
            self.__handle_start_command,
            commands=('start', 'help'),
            content_types=('text',)
        )
        self.__dispatcher.register_message_handler(
            self.__handle_horoscope_command,
            commands=('horoscope',),
            content_types=('text',)
        )
        self.__dispatcher.register_message_handler(
            self.__handle_horoscope_command,
            Text(equals='гороскоп', ignore_case=True),
            content_types=('text',)
        )
    
    def register_callback_handlers(self):
        self.__dispatcher.register_callback_query_handler(
            self.__handle_callback_horoscope_sign
        )
