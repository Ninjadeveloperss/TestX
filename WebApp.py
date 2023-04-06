from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

API_TOKEN = '5960630563:AAH7va9KPMdjgIUinFnMKOIyurpMtACB8Jk'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open WebApp',web_app= WebAppInfo(url = 'https://yandex.com/games/app/218622?utm_medium=search&utm_source=google&utm_campaign=en-uzb_games_general_all_google_search%7C19896569997&utm_term=online%20game#app-id=218622&catalog-session-uid=catalog-70bfb772-760b-5b67-a74e-93a6e50e0340-1680608686586-cf77&rtx-reqid=4678460255045967970&pos=%7B%22listType%22%3A%22suggested%22%2C%22tabCategory%22%3A%22common%22%7D')))
    await message.answer('Hello This is Game App',reply_markup=markup)









if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)