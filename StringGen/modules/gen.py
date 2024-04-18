import asyncio

from pyrogram import Client, filters
from oldpyro import Client as Client1
from oldpyro.errors import ApiIdInvalid as ApiIdInvalid1
from oldpyro.errors import PasswordHashInvalid as PasswordHashInvalid1
from oldpyro.errors import PhoneCodeExpired as PhoneCodeExpired1
from oldpyro.errors import PhoneCodeInvalid as PhoneCodeInvalid1
from oldpyro.errors import PhoneNumberInvalid as PhoneNumberInvalid1
from oldpyro.errors import SessionPasswordNeeded as SessionPasswordNeeded1
from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PasswordHashInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from pyromod.listen.listen import ListenerTimeout

from config import SUPPORT_CHAT
from StringGen import Anony
from StringGen.utils import retry_key


async def gen_session(
    message, user_id: int, telethon: bool = False, old_pyro: bool = False
):
    if telethon:
        ty = f"تيرمكس"
    elif old_pyro:
        ty = f"بايروجرام"

    await message.reply_text(f"**🥤| تم بدء {ty} استخراج الجلسة...**")

    try:
        api_id = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="**🥤| أرسـل الابب أيـدي الخـاص بـك - Send APP ID Bro ...**",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "**🥤| لقد تجاوزت الحد الزمني 10 دقائق أعد استخراج الجلسة مرة أخرى.**",
            reply_markup=retry_key,
        )

    if await cancelled(api_id):
        return

    try:
        api_id = int(api_id.text)
    except ValueError:
        return await Anony.send_message(
            user_id,
            "**🥤| غير صالحAPI_ID(أعد المحاولة).  الخاص بك غير صالح حاول مرة أخرى.**",
            reply_markup=retry_key,
        )

    try:
        api_hash = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="**🥤| أرسـل الأيبـي هـاش الخـاص بـك - Send API HASH Bro...**",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "**🥤| لقد تجاوزت الحد الزمني 5 دقائق أعد استخراج الجلسة مرة أخرى.**",
            reply_markup=retry_key,
        )

    if await cancelled(api_hash):
        return

    api_hash = api_hash.text

    if len(api_hash) < 30:
        return await Anony.send_message(
            user_id,
            ""**🥤| غير صالحAPI_hash(أعد المحاولة).  الخاص بك غير صالح حاول مرة أخرى.**" ",
            reply_markup=retry_key,
        )
     try:
        phone_number = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="**🥤| يـرجـى إرسـال رقـم هاتفـك مـع رمـز الدولة\nمثــال 📱: +96479702387**",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "**🥤| لقد تجاوزت الحد الزمني 5 دقائق أعد استخراج الجلسة مرة أخرى.**",
            reply_markup=retry_key,
        )

    if await cancelled(phone_number):
        return
    phone_number = phone_number.text

    await Anony.send_message(user_id, "**🥤| جاري إرسال الكود انتظر قليلًا من فضلكـ...**")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="Anony", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()

    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
        await asyncio.sleep(1)

    except FloodWait as f:
        return await Anony.send_message(
            user_id,
            f"**🥤| انتهت مـدة الكـود\nأعـد استخـراج الجلسـة مـرة أخـرى**",
            reply_markup=retry_key,
        )
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        return await Anony.send_message(
            user_id,
            "**🥤| الأيبـي أيـدي والأيبـي هـاش غير صالحـان أعـد استخـراج الجلسـة مـرة أخـرى **",
            reply_markup=retry_key,
        )
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return await Anony.send_message(
            user_id,
            "**🥤| رقـم الهـاتف الذي أرسلـته غير صالح أعـد استخـراج الجلسـة مـرة أخـرى.**",
            reply_markup=retry_key,
        )

    try:
        otp = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text=f"**🥤| تحقق من الرسائل في تيليجرام وارسل رمز التحقق\n🥤| قم بإرساله بالشكل التالي**\n1234 => 1 2 3 4\n**🥤| اترك مسافة بين كل رقم**",
            filters=filters.text,
            timeout=600,
        )
        if await cancelled(otp):
            return
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "**🥤| لقد تجاوزت الحد الزمني 5 دقائق أعد استخراج الجلسة مرة أخرى.**",
            reply_markup=retry_key,
        )

    otp = otp.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, otp, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, otp)
    except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
        return await Anony.send_message(
            user_id,
            "**🥤| الكـود الخـاص بـك غير صالـح\n🥤| أعد استخـراج الجلسـة مـرة أخـرى**",
            reply_markup=retry_key,
        )
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        return await Anony.send_message(
            user_id,
            "**🥤| انتهت مـدة الكـود\n🥤| أعـد استخـراج الجلسـة مـرة أخـرى**",
            reply_markup=retry_key,
        )
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        try:
            pwd = await Anony.ask(
                identifier=(message.chat.id, user_id, None),
                text="**🥤| التحقق بخطوتين مفعل بحسابك لذا قم بإرساله هنا من فضلكـ**",
                filters=filters.text,
                timeout=300,
            )
        except ListenerTimeout:
            return Anony.send_message(
                user_id,
                "**🥤| لقد تجاوزت المدة الزمنية يجب عليك إعادة استخراج الجلسة مرة أخرى**",
                reply_markup=retry_key,
            )

        if await cancelled(pwd):
            return
        pwd = pwd.text

        try:
            if telethon:
                await client.sign_in(password=pwd)
            else:
                await client.check_password(password=pwd)
        except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
            return await Anony.send_message(
                user_id,
                "**🥤| التحقق بخطوتين الذي ادخلته خطأ يرجى إعادة الاستخراج مرة أخرى .**",
                reply_markup=retry_key,
            )

    except Exception as ex:
        return await Anony.send_message(user_id, f"خطأ : <code>{str(ex)}</code>")

    try:
        txt = "تم استخراج {0} الجلسة. \n\n**🥤| يرجى فحص الرسائل المحفوظة!**"
        if telethon:
            string_session = client.session.save()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                link_preview=False,
                parse_mode="html",
            )
            await client(JoinChannelRequest("@ah07v"))
        else:
            string_session = await client.export_session_string()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                disable_web_page_preview=True,
            )
            await client.join_chat("ah07v")
    except KeyError:
        pass
    try:
        await client.disconnect()
        await Anony.send_message(
            chat_id=user_id,
            text=f"**{0} كود الجلسة** \n\n`{ty}` \n\n**🥤| انتبه لا تعطي الرمز لأي أحد يمكنه الدخول لحسابك عبره كما يستطيع حذف حسابك! **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs",
                            url=f"tg://openmessage?user_id={user_id}",
                        )
                    ]
                ]
            ),
            disable_web_page_preview=True,
        )
    except:
        pass


async def cancelled(message):
    if "/cancel" in message.text:
        await message.reply_text(
            "» ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴩʀᴏᴄᴇss.", reply_markup=retry_key
        )
        return True
    elif "/restart" in message.text:
        await message.reply_text(
            "» sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇsᴛᴀʀᴛᴇᴅ ᴛʜɪs ʙᴏᴛ.", reply_markup=retry_key
        )
        return True
    elif message.text.startswith("/"):
        await message.reply_text(
            "» ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴩʀᴏᴄᴇss.", reply_markup=retry_key
        )
        return True
    else:
        return False
