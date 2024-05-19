import asyncio
import logging
import random
import time

from aiogram import Bot,Dispatcher,F
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from config import TOKEN,a,b
import keyboard as kb
bot= Bot(token=TOKEN)
dp=Dispatcher()
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('серега лох',reply_markup=kb.main)
@dp.message(F.text=='помощь')
async def get_help(message: Message):
    await  message.answer('Помощи не будет!')
##@dp.message(F.photo)
##async def get_photo(message: Message):
##    await message.answer(f'ID фото: {message.photo[-1].file_id}')
@dp.message(F.text=='мотивация')
async def motivation(message: Message):
    g=random.randint(0,10)
    await message.answer_photo(photo=a[g])



