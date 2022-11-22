from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class Keyboard:
    __menu = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton(text='Гороскоп'),
        #KeyboardButton(text='Настройки')
    )
    __inline_horoscope_menu = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text='Овен', callback_data='aries'),
        InlineKeyboardButton(text='Телец', callback_data='taurus'),
        InlineKeyboardButton(text='Близнецы', callback_data='gemini'),
        InlineKeyboardButton(text='Рак', callback_data='cancer'),
        InlineKeyboardButton(text='Лев', callback_data='leo'),
        InlineKeyboardButton(text='Дева', callback_data='virgo'),
        InlineKeyboardButton(text='Весы', callback_data='libra'),
        InlineKeyboardButton(text='Скорпион', callback_data='scorpio'),
        InlineKeyboardButton(text='Стрелец', callback_data='sagittarius'),
        InlineKeyboardButton(text='Козерог', callback_data='capricorn'),
        InlineKeyboardButton(text='Водолей', callback_data='aquarius'),
        InlineKeyboardButton(text='Рыбы', callback_data='pisces')
    )

    @classmethod
    def get_menu(cls):
        return cls.__menu
    
    @classmethod
    def get_inline_horoscope_menu(cls):
        return cls.__inline_horoscope_menu
