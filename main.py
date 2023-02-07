import requests
import json
from aiogram import Bot, Dispatcher, executor, types

url = "https://coinranking1.p.rapidapi.com/coins"
querystring = {"referenceCurrencyUuid": "yhjMzLPhuIDl", "timePeriod": "24h", "tiers[0]": "1", "orderBy": "marketCap",
               "orderDirection": "desc", "limit": "50", "offset": "0"}
headers = {
    "X-RapidAPI-Key": "309762a3f1mshb8816378be4c2bcp1e702fjsn568bcbe3baf1",
    "X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers, params=querystring)
x = json.loads(response.text)
data = x['data']
coins = data['coins']
TOKEN = '5857824235:AAF7kbEN1xJtRh7CJAxwwOi6Qyf3WPmCSt8'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    from markup import x
    await message.answer("Привет\nЯ крипто bot\nКакие крипто волюты хотите", reply_markup=x)

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.answer("Вы крипто боте\nНажмите на кнопки")
@dp.message_handler()
async def cripto(message: types.Message):
    for i in coins:
        if i['symbol'] == message.text:
            await message.answer(
                f"{i['price']}💸 - Сколько стоит\n{i['name']} - Его имя\n{i['rank']} - на каком месте")
            break

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
