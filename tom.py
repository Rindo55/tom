from pyrogram import Client, idle, filters, enums
import time
from SafoneAPI import SafoneAPI
import os
import asyncio
from html_telegraph_poster.upload_images import upload_image
from pyrogram.types import Message, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, CallbackQuery, InputMediaPhoto

from jikanpy import Jikan
import signal
from io import BytesIO
import sys
import random
import base64
import aiohttp
import requests
from html_telegraph_poster import TelegraphPoster
api_id = 3845818
api_hash = "95937bcf6bc0938f263fc7ad96959c6d"
bot_token = "7374311692:AAFJhri3iPUdTc5UPkqMVFIspVVee-VvDgM"
app = Client("anime_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)




@app.on_message(filters.private & filters.text)
async def handle_message(bot, cmd: Message):
    user_id = cmd.from_user.id
    username = cmd.from_user.username
    uname = f"@{username}"
    img = "https://i.ibb.co/3zKCMXN/IMG-20240723-181715-102.jpg"
    START_MARKUP = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="🎮 Launch Game", url=f"https://app.tomcoin.app/?idUser={user_id}&idRef=1425489930")
            ],
            [
                InlineKeyboardButton(text="🍅 Tom Website", url="https://www.tomcoin.app/")
            ],
            [
                InlineKeyboardButton(text="🐦 TOM Twitter", url="https://twitter.com/TomCoinBnb")
            ],
            [
                InlineKeyboardButton(text="❓ More Info", url="https://t.me/tom_clicker_bot?start=info"),
            ]
        ]
    )
    end_markup = KeyboardButton.KeyboardButtonSimpleWebView(text="🎮 Launch Game", url=f"https://app.tomcoin.app/?idUser={user_id}&idRef=1425489930")
   
    text = f'''Hi, {uname}! This is TOM 👋 

Click on TOM to earn TOM Points. Invest points to buy upgrades, complete tasks, and invite your friends to earn more TOM Points

Get all the points you can to climb the ranking, you will receive an airdrop depending on the position you occupy in the ranking

Higher position in the ranking = bigger airdrop

Will you be the first in the ranking?'''
    text2 = '''🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅

**Welcome to the farm!**

Playing TOM is straightforward. Just tap on the tomato and watch your balance grow.

Use your tomatoes to buy power-ups and harvest more tomatoes faster.

Leverage your referral links and complete tasks to multiply your tomato earnings.

**Come on! It's harvest time!**

This guide is also available by typing /help

🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅'''
    text3 = '''🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅

**Welcome to the farm!**

Playing TOM is straightforward. Just tap on the tomato and watch your balance grow.

Use your tomatoes to buy power-ups and harvest more tomatoes faster.

Leverage your referral links and complete tasks to multiply your tomato earnings.

**Come on! It's harvest time!**

🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅'''
    img2 = "https://i.ibb.co/0QM7dzR/IMG-20240725-094100-985.jpg"
    usr_cmd = cmd.text.split("_", 1)[-1]
    
    if usr_cmd == "/start":
        await app.send_photo(user_id, img, caption=text,reply_markup=START_MARKUP)
    elif usr_cmd == "/start info":
        await app.send_message(user_id, text2, reply_markup=end_markup)
    elif usr_cmd == "/help":
        await app.send_photo(user_id, img2, caption=text3, reply_markup=end_markup)
app.run()
