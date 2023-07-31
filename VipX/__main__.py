import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from VipX import LOGGER, app, userbot
from VipX.core.call import Vip
from VipX.plugins import ALL_MODULES
from VipX.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("VipX").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("VipX").warning(
            "Sur spotify id aur secret toh daala hi nahi aapne ab toh spotify se nahi chala paaoge gaane."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("VipX.plugins." + all_module)
    LOGGER("VipX.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Vip.start()
    try:
        await Vip.stream_decall("https://telegra.ph/file/de3464aa7d6bfafdd2dc3.mp4")
    except:
        pass
    try:
        await Vip.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("VipX").error(
            "[ 𝐄𝐫𝐫𝐨𝐫:- 𝗛𝗲𝘆 𝗕𝗮𝗯𝘆 𝗬𝗼𝘂 𝗛𝗮𝘃𝗲 𝗧𝘂𝗿𝗻𝗲𝗱 𝗢𝗳𝗳 𝗩𝗼𝗶𝗰𝗲 𝗖𝗵𝗮𝘁 𝗢𝗳 𝗬𝗼𝘂𝗿 𝗟𝗼𝗴𝗴𝗲𝗿 𝗚𝗿𝗼𝘂𝗽 \n 𝗣𝗹𝗲𝗮𝘀𝗲 𝗧𝘂𝗿𝗻 𝗢𝗻 𝗩𝗼𝗶𝗰𝗲 𝗖𝗵𝗮𝘁 𝗜𝗻 𝗟𝗼𝗴𝗴𝗲𝗿 𝗚𝗿𝗼𝘂𝗽 𝗔𝗻𝗱 𝗧𝗵𝗲𝗻 𝗥𝗲𝘀𝘁𝗮𝗿𝘁 𝗛𝗲𝗿𝗲. \ 𝗗𝗼𝗻𝘁 𝗧𝘂𝗿𝗻 𝗢𝗳𝗳 𝗧𝗵𝗲 𝗩𝗼𝗶𝗰𝗲 𝗖𝗵𝗮𝘁 𝗢𝗳 𝗬𝗼𝘂𝗿 𝗟𝗼𝗴𝗴𝗲𝗿 𝗚𝗿𝗼𝘂𝗽 𝗔𝗻𝘆𝘁𝗶𝗺𝗲 𝗢𝘁𝗵𝗲𝗿𝘄𝗶𝘀𝗲 𝗬𝗼𝘂𝗿 𝗕𝗼𝘁 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗗𝗲𝗮𝗱.]"
        sys.exit()
    except:
        pass
    await Vip.decorators()
    LOGGER("VipX").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝗩𝗜𝗣 𝗕𝗢𝗬♨️\n╚═════ஜ۩۞۩ஜ════╝")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("VipX").info("Stopping Music Bot...")
