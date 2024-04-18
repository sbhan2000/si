from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="‹ بدء استخراج الجلسة ›", callback_data="gensession")],
        [
            InlineKeyboardButton(text="‹ قـناة الـبوت ›", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="‹ الـمطور ›", url="https://t.me/ah_2_v"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="‹ بايروجرام ›", callback_data="pyrogram"),
            InlineKeyboardButton(text="‹ تيرمكس ›", callback_data="telethon"),
        ],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="‹ بدء استخراج الجلسة ›", callback_data="gensession")]]
)
