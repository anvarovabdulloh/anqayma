from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from keyboard import menu, nastroyka, kontakt, otmen, next_menu, instagram, otmen1

BOT_TOKEN = "6332602698:AAGl97iZvXnq0lHZg7QUEMrB54Mgie2wf4c"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

photo = "https://avatars.mds.yandex.net/i?id=cb05b294b802c97b5693912b3014aa20f3ca6922-9065836-images-thumbs&n=13"


@dp.message_handler(commands=["start", "help"])
async def start_bot(message: types.Message):
    await message.answer(text="""

Assalomu aleykum! Botimizga xush kelibsiz! Keling, avvaliga xizmat ko’rsatish tilini tanlab olaylik.

 Hello! Welcome to our Bot! Let's choose the language of service first""",
                         reply_markup=next_menu())


@dp.callback_query_handler()
async def callback_func(callback: types.CallbackQuery):
    if callback.data == "Русский  ru":
        await callback.message.answer(text="")
    elif callback.data == "Engilish us":
        await callback.message.answer_photo(photo=photo,
                                            caption="""Welcome to "Let's Food" - food service and delivery bot! Our bot is ready to offer you different dishes every day according to the menu. We work from 11:00 to 20:00 so that your lunch is tasty and timely.
Details about our menu can be found by following us on Instagram   @letsfood_tashkent (https://www.instagram.com/letsfood_tashkent) , for instruction on how to use the bot press /instruction 
We are ready to satisfy every taste and make your dinner unforgettable!

Also, we are pleased to announce that when ordering more than 5 servings, delivery is free! There are two types of portions in our menu: "Set" and "Half-set".
Serving cost:

"Set" is 40,000 sum

"Partial Set" - 35,000 sum

We guarantee that each meal will be fresh, tasty and prepared with love. We are waiting for your order!

Eat delicious every day
@letsfood_bot""",
                                            reply_markup=menu())
        await callback.message.answer(text="instagram", reply_markup=instagram())
    elif callback.data == "engilish uz":
        await callback.message.answer(text="")


@dp.message_handler(Text(equals="Back 🛍"))
async def start_bot(message: types.Message):
    await message.answer(text="""Sorry for inconvenience, but we are run out of orders
Try new tastes tomorrow!

@letsfood_bot""")


@dp.message_handler(Text(equals="INFORMATION ℹ️"))
async def start_bot(message: types.Message):
    await message.answer(text="""📌 Here you can find information about our restaurant    
📞 Phone number: +998(90) 177-73-37
🕐 Working time: 10:00 - 20:00
⚡️Contact: @letsfood_bot_admin
📲 Follower us on Instagram::""",
                            reply_markup=instagram())


@dp.message_handler(Text(equals="Nastoyka⚙️"))
async def start_bot(message: types.Message):
    await message.answer(text="change information", reply_markup=nastroyka())


@dp.message_handler(Text(equals="leave a comment  📩"))
async def start_bot(message: types.Message):
    await message.answer(text="Leave a comment", reply_markup=otmen())


@dp.message_handler(Text(equals="order ❌"))
async def start_bot(message: types.Message):
    await message.answer(text="Leave a comment", reply_markup=menu())


@dp.message_handler(Text(equals="change the language Engilish uz"))
async def start_bot(message: types.Message):
    await message.answer(text="choose your own language:", reply_markup=next_menu())


@dp.message_handler(Text(equals="change name✏️"))
async def start_bot(message: types.Message):
    await message.answer(text="Send your name:", reply_markup=otmen1())


@dp.message_handler(Text(equals="back"))
async def start_bot(message: types.Message):
    await message.answer(text="Оrtga", reply_markup=nastroyka())


@dp.message_handler(Text(equals="change phone dependency📱"))
async def start_bot(message: types.Message):
    await message.answer(text="""change phone number:
# \n
your current phone number:   948658089""", reply_markup=kontakt())


@dp.message_handler(Text(equals="Back⬅️"))
async def start_bot(message: types.Message):
    await message.answer(text="Send your phone number:", reply_markup=nastroyka())


@dp.message_handler(Text(equals="back⬅️"))
async def start_bot(message: types.Message):
    await message.answer(text="Click to order 🛍 Make an order", reply_markup=menu())
if __name__ == '__main__':
    executor.start_polling(dp)