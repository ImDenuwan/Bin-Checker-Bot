import requests
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from configs import config

Bot = Client(
    ":memory:",
    api_hash=config.API_ID,
    api_id= config.API_HASH,
    bot_token=config.BOT_TOKEN
)

