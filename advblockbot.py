# Последняя проверка работы была в сентябре 2024 года с aiogram 3.12.0 на python 3.11
import os
if os.path.isfile('config.py'):
    from config import TOKEN # type: ignore
else:
    with open('life.dat', 'w') as f:
        f.write(chr(0b10))
    input('Файл ключа config.py не найден\n')
    os._exit(-1)
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import BaseFilter
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from asyncio import run
import keyboard
import sqlite3
import time

bot = Bot(TOKEN)
dp = Dispatcher()
rt1 = Router()
dp.include_router(rt1)

def foo(func):
    def wrapper(*args):
        t = time.time()
        func(*args)
        print((time.time() - t) * 1000)
    return(wrapper)

@foo
def Provoz(command: str):
    con = sqlite3.connect('usage.db')
    cur = con.cursor()
    cur.execute(command)
    con.commit()
    cur.close()
    con.close()

def Restart():
    os.startfile('advblockbot.py')
    with open('life.dat', 'w') as f:
        f.write(chr(0b01))
    os._exit(1)

keyboard.add_hotkey('R+1+Home', Restart)

rt1.message.filter(lambda m: m.chat.type != "private")

try:
    
    t = time.time()
    with sqlite3.connect('usage.db') as db:
        db.cursor().execute("CREATE TABLE IF NOT EXISTS usage (chat_id INTEGER NOT NULL, calls_number INTEGER NOT NULL, status BOOLEAN NOT NULL CHECK (status IN (0, 1) ), UNIQUE (chat_id) )")
    db.close()
    print(int((time.time() - t) * 1000), 'миллисекунд')


    if os.path.isfile('life.dat'):
        with open('life.dat', 'r') as f:
            if f.read() == chr(0b01): print('Успешный перезапуск')
            else: print('Начало действия')
    else:
        print('Начало действия')
    with open('life.dat', 'w') as f:
        f.write(chr(0b00))

    @rt1.message(Command('start'))
    async def NewChat(m: types.Message):
        #Provoz(f'INSERT INTO usage VALUES ({}, {}, {})')
        await m.answer('Я \- бот, который поможет избавляться от рекламы других ботов\. Поддержать можно по команде [/donate](/donate@advblockbot)', parse_mode = ParseMode.MARKDOWN_V2)

    @rt1.message(Command('off'))
    async def Off(m: types.Message):
        #Provoz('INSERT INTO usage ')
        await m.answer('Блокировка рекламы выключена')

    @rt1.message(Command('on'))
    async def On(m: types.Message):
        await m.answer('Блокировка рекламы включена')

    @rt1.message(Command('donate'))
    async def Donate(m: types.Message):
        await m.answer('На данный момент донаты не принимаются')

    @dp.message(lambda m: m.chat.type == "private", Command(commands = ['start', 'off', 'on', 'donate']))
    async def OutReply(m: types.Message): await m.answer('Бот работает только в группах')

    async def main():
        await dp.start_polling(bot)

    if __name__ == "__main__":
        run(main())

except Exception as e:
    input(e)