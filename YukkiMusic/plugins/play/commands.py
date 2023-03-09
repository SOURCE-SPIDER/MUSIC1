import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from config import START_IMG_URL
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")

OWNER = getenv("OWNER")


@app.on_message(
    command(["الاوامر","اوامر"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG_URL}",
        caption=f"""
════════ ××× ════════
▶️╖ تشغيل «» ريلاي علي اغنيه او فديو
🎶╢ تشغيل + اسم الاغنيه
🔊╢ اكتب لتشغيل اغنيه /play + اسم الاغنيه
📹╢ تشغيل فديو + اسم الفديو
〽️╢ اكتب لتشغيل فديو /vplay + اسم الفديو
🔴╢ تشغيل + لينك بث مباشر
💢╢ ايقاف
💫╢ تخطي
😵╢ كتم
👷‍♂️╢ تحميل + اسم الاغنيه
💥╢ سورس «» جابوا
👮╜ المطور «» بوت
════════ ××× ════════
💎 « المطور الاساسي » ⇊
════════ ××× ════════
⚡╖ حظر «» ريلاي علي الشخص
🐾╢ فك «» ريلاي علي الشخص
💎╢ عام «» ريلاي علي الشخص
✨╢ الغلي «» ريلاي علي الشخص
🗣️╢ رفع «» ريلاي علي الشخص
👥╢ تنزيل «» ريلاي علي الشخص
🌀╢ العام
🐣╢ الادمنيه
🚧╢ ذيع «» ريلاي علي الكلمه
🗽╜ ذيع بالمساعد «» ريلاي علي الكلمه
════════ ××× ════════""",
        reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "• مطور البوت 🤖", url=f"https://t.me/{OWNER}")
                ],[
                    InlineKeyboardButton(
                       "• اضف البوت الي مجموعتك ✅", url=f"https://t.me/{MUSIC_BOT_NAME}?startgroup=true"),
                ],
            ]
        ),
    )
    
@app.on_message(
    command(["الالعاب","العاب"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/774e63a7b05e0ff3e3fec.jpg",
        caption=f"""
════════ ××× ════════
‹• الالعاب بوت الميوزك 🤖 •›
════════ ××× ════════
🐣╖ تويت - صراحه
💠╢ احكام -نكته
🏌️╜ حروف - لو خيروك
════════ ××× ════════""",
        reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "• مطور البوت 🤖", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                       "• اضف البوت الي مجموعتك ✅", url=f"https://t.me/{MUSIC_BOT_NAME}?startgroup=true"),
                ],
            ]
        ),
    )