# Последняя проверка работы была в феврале 2024 года с aiogram 3.4.1 на python 3.11
import os
if os.path.isfile('config.py'):
    from config import TOKEN
else:
    input('Файл ключа config.py не найден\n')
    with open('life.dat', 'w') as f:
        f.write(chr(0b10))
    os._exit(-1)
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio
import keyboard

bot = Bot(TOKEN)
dp = Dispatcher()

def Restart():
    os.startfile('advblockbot.py')
    with open('life.dat', 'w') as f:
        f.write(chr(0b01))
    os._exit(1)

keyboard.add_hotkey('R', Restart)

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
        await m.answer('Hi');

    async def main():
        await dp.start_polling(bot)

    if __name__ == "__main__":
        asyncio.run(main())

    
except Exception as e:
    input(e)