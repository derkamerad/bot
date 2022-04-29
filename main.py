from datetime import datetime, timedelta
from aiogram.types import Message
from aiogram import Bot, Dispatcher, types
from aiogram.types.base import String

from aiogram.utils import executor
# from pip._internal.utils import datetime

bot = Bot(token="1509146881:AAE9DgUR0Gtkb0zv_5C3G8uwWE7hAdmMHWg")
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    inv_id = -429620840
    if message.text != "":
        name = message.text
    else:
        name = "Knight"
    text = "Hello "
    expire_date = datetime.now() + timedelta(days=1)
    # link = "https://t.me/+Etdbo15bdl81ZmYy"
    # link = await bot.export_chat_invite_link (chat_id)
    link = await bot.create_chat_invite_link(inv_id, expire_date, 1)
    await bot.send_message(chat_id=chat_id, text=text + name + ", заходи сюда: " + link.invite_link)

    # sent_mess = await bot.send_photo(chat_id=chat_id, photo="https://images.indianexpress.com/2020/03/cat.jpg",
    # caption="Котик)) 🎲") print(sent_mess.photo[-1].file_unique_id) result = await bot.set_chat_title(
    # chat_id=chat_id, title=name)

    local_bot = await bot.get_me()
    print(local_bot.username)
executor.start_polling(dp)
