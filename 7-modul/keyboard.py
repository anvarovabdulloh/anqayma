from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def nastroyka():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="change the languageENG"), KeyboardButton(text="change phone number 📱"))
    rkm.row(KeyboardButton(text="change name✏️"), KeyboardButton(text="back⬅️"))
    return rkm


def menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="order 🛍"), KeyboardButton(text="information ℹ️"))
    rkm.row(KeyboardButton(text="Nastoryka⚙️"), KeyboardButton(text=" comment  📩"))
    return rkm


def kontakt():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="share a phone number📞", request_contact=True))
    rkm.row(KeyboardButton(text="back⬅️"))
    return rkm


def otmen():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="don't ❌"))
    return rkm


def otmen1():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="don't"))
    return rkm

def next_menu():
    ikm = InlineKeyboardMarkup()
    ikm.row(InlineKeyboardButton(text="Русский 🇷🇺", callback_data="Русский 🇷🇺"))
    ikm.row(InlineKeyboardButton(text="English 🇺🇸", callback_data="English 🇺🇸"))
    ikm.row(InlineKeyboardButton(text="Õzbek🇺🇿", callback_data="Õzbek🇺🇿"))
    return ikm


def instagram():
    ikm = InlineKeyboardMarkup()
    ikm.row(InlineKeyboardButton(text="Instagram🎉", callback_data="instagram🎉"))
    return ikm