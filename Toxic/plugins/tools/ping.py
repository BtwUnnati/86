from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from Toxic import app
from Toxic.core.call import Dev
from Toxic.utils import bot_sys_stats
from Toxic.utils.decorators.language import language
from Toxic.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_video(
        video="https://ar-hosting.pages.dev/1753091331936.mp4",
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await Dev.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
