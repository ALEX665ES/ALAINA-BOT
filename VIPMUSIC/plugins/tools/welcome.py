import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from VIPMUSIC import app
from pyrogram import filters
from pyrogram.errors import RPCError
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
from os import environ
import random
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, time, aiohttp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from asyncio import sleep
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode


import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
from typing import Union, Optional

# --------------------------------------------------------------------------------- #

get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)
resize_text = (
    lambda text_size, text: (text[:text_size] + "...").upper()
    if len(text) > text_size
    else text.upper()
)

# --------------------------------------------------------------------------------- #

async def get_userinfo_img(
    bg_path: str,
    font_path: str,
    user_id: Union[int, str],
    profile_path: Optional[str] = None
):
    bg = Image.open(bg_path)

    if profile_path:
        img = Image.open(profile_path)
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.pieslice([(0, 0), img.size], 0, 360, fill=255)

        circular_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        circular_img.paste(img, (0, 0), mask)
        resized = circular_img.resize((400, 400))
        bg.paste(resized, (440, 160), resized)

    img_draw = ImageDraw.Draw(bg)

    img_draw.text(
        (529, 627),
        text=str(user_id).upper(),
        font=get_font(46, font_path),
        fill=(255, 255, 255),
    )

    path = f"./userinfo_img_{user_id}.png"
    bg.save(path)
    return path

# --------------------------------------------------------------------------------- #

bg_path = "VIPMUSIC/assets/userinfo.png"
font_path = "VIPMUSIC/assets/hiroko.ttf"

# --------------------------------------------------------------------------------- #

# welcome

@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for user in message.new_chat_members:
        count = await app.get_chat_members_count(chat.id)
        photo = await app.download_media(user.photo.big_file_id)

        welcome_photo = await get_userinfo_img(
            bg_path=bg_path,
            font_path=font_path,
            user_id=user.id,
            profile_path=photo,
        )
        msg = (
            f"**🌷𝐇ᴇʏ {message.from_user.mention}**\n**𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ 𝐀 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ🥳**\n\n"
            f"**📝𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ: {message.chat.title}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**🔐𝐂ʜᴀᴛ 𝐔.𝐍: @{message.chat.username}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**💖𝐔ʀ 𝐈d: {user.id}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**✍️𝐔ʀ 𝐔.𝐍: @{user.username}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**👥𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀ𝐬🎉**"
        )
        await app.send_photo(message.chat.id, photo=welcome_photo, caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"𝐊ɪᴅɴᴀᴘ 𝐌ᴇ", url=f"https://t.me/{app.username}?startgroup=true")]
        ]))
