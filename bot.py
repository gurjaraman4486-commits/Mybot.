from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = "8919459210:AAGWtjHwgUFETIABPIVTOrhB2dcgGFvMLBc"

DEMO_CHANNEL = "https://t.me/demochannlink"
PREMIUM_CHANNEL = "https://t.me/howtogetpre"


def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("💎 Get Premium", callback_data='premium')],
        [InlineKeyboardButton("🎬 Demo Videos", url=DEMO_CHANNEL)],
        [InlineKeyboardButton("📖 How To Get Premium", url=PREMIUM_CHANNEL)],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = """
🎬 Available Collection

🎬 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐕𝐢𝐝𝐞𝐨𝐬 𝐂𝐨𝐥𝐥𝐞𝐜𝐭𝐢𝐨𝐧

𝟏. 𝐌𝟎𝐌 𝐒𝟎𝐍 𝐯𝐢𝐝𝐞𝐨𝐬 - 𝟓𝟎𝟎𝟎+

𝟐. 𝐒!𝐬𝐭𝐞𝐫 𝐁𝐫𝟎𝐭𝐡𝐞𝐫 𝐯𝐢𝐝𝐞𝐨𝐬 -𝟐𝟎𝟎𝟎+

𝟑. €𝐏 𝐯𝐢𝐝𝐞𝐨𝐬 - 𝟏𝟓𝟎𝟎𝟎+

𝟒. 𝟏𝟖𝐓𝐞𝐞𝐧 𝐕𝐢𝐝𝐞𝐨𝐬 - 𝟔𝟎𝟎𝟎+

𝟓. 𝐈𝐧𝐝𝐢𝐚𝐧 𝐝𝐞𝐬𝐢 𝐯𝐢𝐝𝐞𝐨𝐬 - 𝟏𝟎𝟎𝟎𝟎+

𝟔. 𝐇𝐢𝐝𝐝𝐞𝐧 𝐜𝐚𝐦 𝐯𝐢𝐝𝐞𝐨𝐬 - 𝟐𝟎𝟎𝟎+

Click Get Premium 👇
"""

    update.message.reply_text(text, reply_markup=reply_markup)


def premium_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("👉 BASIC PLAN - ₹99", callback_data='plan1')],
        [InlineKeyboardButton("👉 STANDARD PLAN - ₹149", callback_data='plan2')],
        [InlineKeyboardButton("👉 ALL IN ONE - ₹249", callback_data='plan3')],
        [InlineKeyboardButton("👉 VIP ACCESS - ₹499", callback_data='plan4')],
        [InlineKeyboardButton("⬅ Back", callback_data='back')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.reply_text(
        "🔥 Choose Your Plan:",
        reply_markup=reply_markup
    )


def send_payment(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    plan_data = {
        'plan1': ('BASIC PLAN', '₹99'),
        'plan2': ('STANDARD PLAN', '₹149'),
        'plan3': ('ALL IN ONE', '₹249'),
        'plan4': ('VIP ACCESS', '₹499')
    }

    plan_name, amount = plan_data[query.data]

    keyboard = [
        [InlineKeyboardButton("✅ GET PRIVATE CHANNEL LINK", url=PREMIUM_CHANNEL)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    caption = f"""
💰 Plan: {plan_name}
💵 Amount: {amount}
🆔 Order ID: ORD123456

📌 Pay using the QR code below.
After payment contact admin.
"""

    query.message.reply_photo(
        photo=open('qr.jpg', 'rb'),
        caption=caption,
        reply_markup=reply_markup
    )


def back_button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("💎 Get Premium", callback_data='premium')],
        [InlineKeyboardButton("🎬 Demo Videos", url=DEMO_CHANNEL)],
        [InlineKeyboardButton("📖 How To Get Premium", url=PREMIUM_CHANNEL)],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.reply_text(
        "Main Menu 👇",
        reply_markup=reply_markup
    )


def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query

    if query.data == 'premium':
        premium_menu(update, context)

    elif query.data in ['plan1', 'plan2', 'plan3', 'plan4']:
        send_payment(update, context)

    elif query.data == 'back':
        back_button(update, context)


updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CallbackQueryHandler(button_handler))

print("Bot Running...")

updater.start_polling()
updater.idle()
