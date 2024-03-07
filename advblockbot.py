# Последняя проверка работы была в феврале 2024 года с aiogram 3.4.1 на python 3.11
import os
if os.path.isfile('config.py'):
    from config import TOKEN
else:
    with open('life.dat', 'w') as f:
        f.write(chr(0b10))
    input('Файл ключа config.py не найден\n')
    os._exit(-1)
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from asyncio import run
import keyboard
import sqlite3

bot = Bot(TOKEN)
dp = Dispatcher()

db = sqlite3.connect('usage.db')
crs = db.cursor()
crs.execute("CREATE TABLE IF NOT EXISTS usage (chat_id INTEGER NOT NULL, calls_number INTEGER NOT NULL, status BOOLEAN NOT NULL CHECK (status IN (0, 1)))")

def Restart():
    os.startfile('advblockbot.py')
    with open('life.dat', 'w') as f:
        f.write(chr(0b01))
    os._exit(1)

def checkgroup(func):
    pass

keyboard.add_hotkey('R+1+Home', Restart)

try:


    if os.path.isfile('life.dat'):
        with open('life.dat', 'r') as f:
            if f.read() == chr(0b01): print('Успешный перезапуск')
            else: print('Начало действия')
    else:
        print('Начало действия')
    with open('life.dat', 'w') as f:
        f.write(chr(0b00))

    @dp.message(Command('start'))
    async def NewChat(m: types.Message):
        if m.chat.type == 'group' or m.chat.type == 'supergroup':
            await m.answer('Я \- бот, который поможет избавляться от рекламы других ботов\. Поддержать можно по команде [/donate](/donate@advblockbot)', parse_mode=ParseMode.MARKDOWN_V2);
        else: await m.answer('Бот работает только в группах')

    @dp.message(Command('off'))
    async def Off(m: types.Message):
        if m.chat.type == 'group' or m.chat.type == 'supergroup':
            await m.answer('Блокировка рекламы выключена');
        else: await m.answer('Бот работает только в группах')

    @dp.message(Command('on'))
    async def On(m: types.Message):
        pass

    @dp.message(Command('donate'))
    async def Donate(m: types.Message):
        pass

    async def main():
        await dp.start_polling(bot)

    if __name__ == "__main__":
        run(main())

except Exception as e:
    input(e)