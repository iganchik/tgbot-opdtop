import asyncio
import logging
from aiogram import Bot, Dispatcher
from run import dp, bot
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')