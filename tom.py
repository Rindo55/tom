from pyrogram import Client, idle, filters, enums
from db import is_voted, save_vote
import time
from SafoneAPI import SafoneAPI
import os
import asyncio
from html_telegraph_poster.upload_images import upload_image
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto
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
bot_token = "7005003917:AAG1GwMAm4uFxMOzvesg1vTWRjVX0hHKStM"
app = Client("anime_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

post

@app.on_message(filters.private & filters.command("start"))
async def handle_message(bot, cmd: Message):
    user_id = cmd.from_user.id
    username = cmd.from_user.username
    uname = f"@{username}"
    img = "https://i.ibb.co/3zKCMXN/IMG-20240723-181715-102.jpg"
    text = f'''Hi, @{unsme}! This is TOM 👋 

Click on TOM to earn TOM Points. Invest points to buy upgrades, complete tasks, and invite your friends to earn more TOM Points

Get all the points you can to climb the ranking, you will receive an airdrop depending on the position you occupy in the ranking

Higher position in the ranking = bigger airdrop

Will you be the first in the ranking?'''
    await app.send_photo(text=text, img
