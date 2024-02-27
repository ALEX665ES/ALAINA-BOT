import asyncio
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.core.userbot import Userbot
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from VIPMUSIC import app

userbot = Userbot()

@app.on_message(filters.command(["userbotjoin", f"userbotjoin@{app.username}"]) & ~filters.private & ~filters.bot
)
async def join_group(client, message):
    chid = message.chat.id
    try:
        await userbot.one.start()
        invitelink = await app.export_chat_invite_link(chid)
    except BaseException:
        await message.reply_text(
            "• **I'm not have permission:**\n\n» ❌ __Add Users__",
        )
        return

    try:
        await userbot.one.join_chat(invitelink)
        await asyncio.sleep(2) 
        await userbot.one.stop()
    except UserAlreadyParticipant:
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"🛑 Flood Wait Error 🛑 \n\n**userbot couldn't join your group due to heavy join requests for userbot**"
            "\n\n**or add assistant manually to your Group and try again**",
        )
        return
    await message.reply_text(
        f"**Userbot Succesfully Entered Chat**",
    )


@app.on_message(filters.command("userbotleave") & filters.group)

async def leave_one(client, message):
    try:
        await userbot.one.start()
        await userbot.one.leave_chat(message.chat.id)
        await app.send_message(message.chat.id, "✅ Userbot Successfully Left Chat")
        await asyncio.sleep(0.5) 
        await userbot.one.stop()
        
    except BaseException:
        await message.reply_text(
            "❌ **Userbot couldn't Leave your Group, May be Floodwaits.**\n\n**» or manually kick userbot from your group**"
        )

        return


@app.on_message(filters.command(["leaveall", f"leaveall@{app.username}"]) & SUDOERS)
async def leave_all(client, message):
    await userbot.one.start()
    if message.from_user.id not in SUDOERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 **Userbot** Leaving All Chats !")
    
    # Get all dialogs
    dialogs = await userbot.one.get_dialogs()
    
    for dialog in dialogs:
        try:
            await userbot.one.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(
                f"Userbot leaving all group...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        except BaseException:
            failed += 1
            await lol.edit(
                f"Userbot leaving...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        await asyncio.sleep(0.7)
        
    await app.send_message(
        message.chat.id, f"✅ Left from: {left} chats.\n❌ Failed in: {failed} chats.")
        # Stop the Pyrogram client after sending messages
    await userbot.one.stop()
