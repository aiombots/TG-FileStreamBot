# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot


@StreamBot.on_message(filters.command(["start"]))
async def start(_, m: Message):
    await m.reply(
        f"""Hᴇʟʟᴏ 👋 {m.from_user.mention(style="md")}, 

Tʜɪs Is A Fɪʟᴇ Tᴏ Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ Bᴏᴛ

Yᴏᴜ Cᴀɴ Usᴇ Mᴇ Tᴏ Dᴏᴡɴʟᴏᴀᴅ Fɪʟᴇs Fʀᴏᴍ Yᴏᴜ'ʀᴇ Bʀᴏᴡsᴇʀ

Jᴜsᴛ Sᴇɴᴅ Mᴇ A Tᴇʟᴇɢʀᴀᴍ Fɪʟᴇ Aɴᴅ Sᴇᴇ Mʏ Pᴏᴡᴇʀ

Pᴏᴡᴇʀᴇᴅ ʙʏ : @AIOM_BOTS"""
    )
