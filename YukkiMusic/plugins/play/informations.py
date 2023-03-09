import asyncio
import os
import re
import requests
from pyrogram import Client, filters
from strings import get_command
from aiohttp import ClientSession
from traceback import format_exc
from strings.filters import command
from pyrogram.types import *
from random import choice
from config import START_IMG_URL,UPDATES_CHANNEL
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

@app.on_message(command(["طباعه","/pr"]))
async def paste_func(_, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("قم بالرد على الرساله بالأمر `طباعه`")
    r = message.reply_to_message
    if not r.text and not r.document:
        return await message.reply_text("يتم دعم النصوص والمستندات فقط ")
    m = await message.reply_text("لصق ...")
    if r.text:
        content = str(r.text)
    elif r.document:
        if r.document.file_size > 40000:
            return await m.edit("يمكنك فقط لصق ملفات أصغر من 40 كيلوبايت .")
        if not pattern.search(r.document.mime_type):
            return await m.edit("يمكن لصق الملفات النصية فقط .")
        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)
    link = await paste(content)
    kb = [[InlineKeyboardButton(text="رابط اللصق", url=link)]]
    try:
        if m.from_user.is_bot:
            await message.reply_photo(photo=link,quote=False,caption="تم نسخ النص",reply_markup=InlineKeyboardMarkup(kb),)
        else:
            await message.reply_photo(photo=link,quote=False,caption="تم نسخ النص",reply_markup=InlineKeyboardMarkup(kb),)
        await m.delete()
    except Exception:
        await m.edit("فتح الرابط", reply_markup=InlineKeyboardMarkup(kb))


@app.on_message(command(["الرابط","رابط","/link"]) & ~filters.bot & ~filters.private)
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        return await message.reply_text("⦁ قم برفعي مسؤول في المجموعة أولا ؟\n√")
    await message.reply_text(f"⦁ رابط الجروب -> {invitelink}\n√")
    
@app.on_message(filters.voice_chat_started)
async def brah(client, message):
       await message.reply("• تم بدا محادثة صواتية جديدة 🎸 |\n√")
       
@app.on_message(filters.voice_chat_ended)
async def brah2(client, message):
       await message.reply("• تم انهاء المحادثه الصواتيه 🎸 |\n√")
       
@app.on_message(filters.voice_chat_members_invited)
async def fuckoff(client, message):
           text = f"🎸 | قام -> {message.from_user.mention}\n"
           x = 0
           for user in message.voice_chat_members_invited.users:
             try:
               text += f"🎸 | بدعوة -> {user.mention} \n🎸 | إلي المحادثة المرئية •"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text}")
           except:
             pass

def get_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            "contact",
            "dice",
            "poll",
            "location",
            "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj


@app.on_message(command(["ايدي","الايدي","id","/id","/ايدي","ايديي"]))
async def shadow(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    user = usr.username
    mention = usr.mention
    await message.reply_photo(
        photo=f"{START_IMG_URL}",
        caption=f"""💎╖ ايدِيڪ ⇇ `{message.from_user.id}`\n🐣╢ اسمڪ ⇇ {mention}\n☀️╢ يوزرڪ ⇇ @{user}\n🌍╢ اسـم الـروم ⇇ {message.chat.title}\n👁╢ يـوزر الـروم ⇇ @{message.chat.username}\n🎈╜ ايـدي الـروم ⇇ {message.chat.id}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                        name, url=f"https://t.me/{user}"
                ),
        ],
        ]
     ),
  )
@app.on_message(
    command(["اسمي"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**💠 | اسمك » {name}**""",)

@app.on_message(
    command(["يوزري","معرفي"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    user = usr.username
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**🧶 | يوزرك » @{user}**""",)                    

@app.on_message(
    command(["بايو","البايو"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_chat(message.from_user.id)
    kbio = usr.bio
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""🐣 | البايو » {kbio}""",)
 
@app.on_message(
    command(["اسمي2"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""💠 | اسمك ↑↓""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}"),               
                ],
            ]
        ),
    )
    
@app.on_message(
    command(["قول","كول"])
    & filters.group
    & ~filters.edited
)
def echo(client, msg):
    text = msg.text.split(None, 1)[1]
    msg.reply(text)

@app.on_message(
    command(["معلوماتي"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    bo = await client.get_chat(message.from_user.id)
    name = usr.first_name
    user = usr.username
    bioo = bo.bio
    lname = f"• 🖤 | 𝑵𝑨𝑴𝑬 : {name}"
    luser = f"• 🖤 | 𝑼𝑬𝑺 : @{message.from_user.username}"
    uid = f"• 🖤 | 𝑰𝑫 : {message.from_user.id}"
    group = f"• 🖤 | 𝑩𝑰𝑶 : {bioo}"    
    async for photo in client.iter_profile_photos(MUSIC_BOT_NAME, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**• 🖤 |𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝑮𝒓𝒐𝒖𝒑| 🖤 •**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        lname, url=f"https://t.me/{message.from_user.username}"),
                ],
                [
                    InlineKeyboardButton(
                        luser, url=f"https://t.me/{message.from_user.username}"),
                ],
                [
                    InlineKeyboardButton(
                        uid, url=f"https://t.me/{message.from_user.username}"),
                ],
                [
                    InlineKeyboardButton(
                        group, url=f"https://t.me/{message.from_user.username}"),
                ],
                [ 
                InlineKeyboardButton(
                        "⌁ 𝑴𝑼𝑺𝑰𝑪 𝑺𝑨𝑰𝑫𝑰 ⚡️", url=f"https://t.me/SaidiMusic"),
                ],
            ]
        ),
    )


array = []

@app.on_message(filters.command(["all", "تاك"], "") & ~filters.private)
async def num(client, message):
  chek = await app.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in ["creator", "administrator"] :
    await message.reply("• يجب ان تكون مشرف بالمجموعه لاستخدام التاك")
    return
  i = 0
  txt = ""
  zz = message.text
  try:
   zz = zz.replace("all","")
  except:
    zz = zz.replace("تاك","")
  array.append(message.chat.id)
  async for x in app.iter_chat_members(message.chat.id):
      if message.chat.id not in array:
        return
      i += 1
      txt += f"{x.user.mention}"
      if i == 5:
        await app.send_message(message.chat.id, f"{zz}\n{txt}")
        i = 0
        txt = ""
        await asyncio.sleep(2)


@app.on_message(filters.command("ايقاف", ""))
async def stop(client, message):
  if message.chat.id not in array:
     await message.reply("• التاك متوقف بالفعل")
     return False 
  if message.chat.id in array:
    array.remove(message.chat.id)
    await message.reply("• تم ايقاف التاك")
    return False