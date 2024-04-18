from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"<b>🏮 مرحبا {message.from_user.first_name},\n\n🏮 انا اسمي {Anony.mention},\n🏮 استطيع استخراج جلسات التيرمكس والبايروجرام بسهوله وسرعه وامان.</b>",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
