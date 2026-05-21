from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = "8919459210:AAGWtjHwgUFETIABPIVTOrhB2dcgGFvMLBc"

DEMO_CHANNEL = "https://t.me/demochannlink"
PREMIUM_CHANNEL = "https://t.me/pbtchannlink"


def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("💎 Get Premium", callback_data='premium')],
        [InlineKeyboardButton("🎬 Demo Videos", url=DEMO_CHANNEL)],
        [InlineKeyboardButton("📖 How To Get Premium", url=PREMIUM_CHANNEL)],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = """
🎬 Available Collection

1. Plan A
2. Plan B
3. Plan C
4. VIP Access

Choose an option below 👇
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

    query.message.reply_photo(
        photo=open('demo.jpg', 'rb'),
        caption="🔥 Choose Your Plan:",
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
