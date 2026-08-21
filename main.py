import os
import hashlib
from pathlib import Path

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]


# Finds the welcome image you uploaded to GitHub automatically
def get_welcome_image():
    for file in Path(".").iterdir():
        if file.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp"]:
            return file
    return None


# Gives each Telegram user the SAME personal phrase every time they return
PERSONAL_PHRASES = [
    "Pink Paradise",
    "Purple Haze",
    "Terp Queen",
    "Highland Dream",
    "Neon Queen",
    "Ayrshire Gold",
    "Cloud Nine",
    "Royal Terps",
    "Purple Crown",
    "Sweet Dreams",
    "Good Vibes",
    "Pink Diamond",
    "Highland Queen",
    "Golden Crown",
    "Neon Dreams",
    "Royal Purple",
]


def personal_phrase(user_id):
    number = int(
        hashlib.sha256(str(user_id).encode()).hexdigest(),
        16
    )

    return PERSONAL_PHRASES[number % len(PERSONAL_PHRASES)]


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


async def send_home(update):
    user = update.effective_user

    phrase = personal_phrase(user.id)

    # First message - similar to GTOWN
    await update.effective_message.reply_text(
        "✅ You're in!\n\n"
        f"🔑 Your personal phrase: {phrase}\n\n"
        "Remember it — it will be shown to you when you return."
    )

    image = get_welcome_image()

    if image:
        with open(image, "rb") as photo:
            await update.effective_message.reply_photo(
                photo=photo,
                caption=(
                    "👑 Welcome to AYRSHIRE TERP QUEEN 👑\n\n"
                    "Choose an option below:"
                ),
                reply_markup=main_menu()
            )
    else:
        await update.effective_message.reply_text(
            "👑 Welcome to AYRSHIRE TERP QUEEN 👑\n\n"
            "Choose an option below:",
            reply_markup=main_menu()
        )


async def start(update, context):
    await send_home(update)


async def show_menu(update, context):
    await send_home(update)


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

        await query.message.reply_text(
            order_text,
            reply_markup=buttons
        )

    elif query.data == "menu":

        user = query.from_user
        phrase = personal_phrase(user.id)

        image = get_welcome_image()

        await query.message.reply_text(
            f"🔑 Your personal phrase: {phrase}"
        )

        if image:
            with open(image, "rb") as photo:
                await query.message.reply_photo(
                    photo=photo,
                    caption=(
                        "👑 Welcome to AYRSHIRE TERP QUEEN 👑\n\n"
                        "Choose an option below:"
                    ),
                    reply_markup=main_menu()
                )
        else:
            await query.message.reply_text(
                "👑 Welcome to AYRSHIRE TERP QUEEN 👑\n\n"
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
