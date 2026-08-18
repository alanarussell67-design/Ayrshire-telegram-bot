import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

# Your token will be stored securely on the hosting service later
TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]


def main_menu():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "📱 TELEGRAM",
                url="https://t.me/+M9HXL5mrCYYzYzRk"
            ),
            InlineKeyboardButton(
                "🔒 SIGNAL",
                url="https://signal.group/#CjQKIG_ywqWkwZ5CjvGpO_LlndovLwrGfxDd3ztRLegnm7AMEhCgPly_ZSYmHr9Yf_Sg7ITL"
            ),
        ],
        [
            InlineKeyboardButton(
                "💰 PRICE LIST",
                url="https://justpaste.it/Ayrshiregenetics"
            ),
            InlineKeyboardButton(
                "📸 GALLERY",
                url="https://t.me/+IFm1y-zt9txkZWE0"
            ),
        ],
        [
            InlineKeyboardButton(
                "📦 ORDER INFO",
                callback_data="orders"
            ),
            InlineKeyboardButton(
                "💌 CONTACT US",
                url="https://t.me/Terpqueenayrshire"
            ),
        ],
    ])


async def start(update, context):
    await update.message.reply_text(
        "👑 Welcome to AYRSHIRE TERP QUEEN 👑\n\n"
        "Choose an option below:",
        reply_markup=main_menu()
    )


async def show_menu(update, context):
    await update.message.reply_text(
        "👑 Welcome to AYRSHIRE TERP QUEEN 👑\n\n"
        "Choose an option below:",
        reply_markup=main_menu()
    )


async def button(update, context):
    query = update.callback_query
    await query.answer()

    if query.data == "orders":

        order_text = (
            "📦 ORDER INFO\n\n"
            "⏰ DROP TIMES\n\n"
            "All orders to be in for:\n\n"
            "🕛 12AM\n"
            "🕓 4PM\n"
            "🕖 7PM\n\n"
            "📦 BULK ORDERS\n\n"
            "Any bulk orders need to be pre-ordered. "
            "Please get them in that morning so they can be "
            "sorted throughout the day in one big run.\n\n"
            "📍 COLLECTIONS\n\n"
            "DM for collection location."
        )

        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "💌 CONTACT US",
                    url="https://t.me/Terpqueenayrshire"
                )
            ],
            [
                InlineKeyboardButton(
                    "⬅️ BACK TO MAIN MENU",
                    callback_data="menu"
                )
            ]
        ])

        await query.edit_message_text(
            text=order_text,
            reply_markup=buttons
        )

    elif query.data == "menu":

        await query.edit_message_text(
            text="👑 Welcome to AYRSHIRE TERP QUEEN 👑\n\n"
                 "Choose an option below:",
            reply_markup=main_menu()
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, show_menu)
)

print("AYRSHIRE TERP QUEEN BOT IS RUNNING 👑")

app.run_polling()
