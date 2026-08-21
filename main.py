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


def get_welcome_image():
    for file in Path(".").iterdir():
        if file.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp"]:
            return file
    return None


PERSONAL_PHRASES = [
    "Pink Paradise",
    "Purple Crown",
    "Neon Queen",
    "Highland Dream",
    "Ayrshire Gold",
    "Cloud Nine",
    "Good Vibes",
    "Pink Diamond",
    "Royal Purple",
    "Neon Dreams",
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
                "📸 GALLERY",
                url="https://t.me/+IFm1y-zt9txkZWE0"
            ),
            InlineKeyboardButton(
                "👑 ABOUT US",
                callback_data="about"
            ),
        ],
        [
            InlineKeyboardButton(
                "💌 CONTACT US",
                url="https://t.me/Terpqueenayrshire"
            ),
            InlineKeyboardButton(
                "🏠 MAIN MENU",
                callback_data="menu"
            ),
        ],
    ])


async def send_home(message, user):
    phrase = personal_phrase(user.id)

    await message.reply_text(
        "✅ You're in!\n\n"
        f"🔑 Your personal phrase: {phrase}\n\n"
        "Remember it — it will be shown to you when you return."
    )

    image = get_welcome_image()

    caption = (
        "👑 Welcome to AYRSHIRE TERP QUEEN 👑\n\n"
        "Choose an option below:"
    )

    if image:
        with open(image, "rb") as photo:
            await message.reply_photo(
                photo=photo,
                caption=caption,
                reply_markup=main_menu()
            )
    else:
        await message.reply_text(
            caption,
            reply_markup=main_menu()
        )


async def start(update, context):
    await send_home(
        update.message,
        update.effective_user
    )


async def regular_message(update, context):
    await send_home(
        update.message,
        update.effective_user
    )


async def button(update, context):
    query = update.callback_query
    await query.answer()

    if query.data == "about":
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "⬅️ BACK TO MAIN MENU",
                    callback_data="menu"
                )
            ]
        ])

        await query.message.reply_text(
            "👑 AYRSHIRE TERP QUEEN 👑\n\n"
            "Welcome to our community hub.\n\n"
            "📸 Browse the gallery\n"
            "📱 Join our Telegram community\n"
            "🔒 Connect through Signal\n"
            "💌 Contact us directly\n\n"
            "Good vibes • Community • Ayrshire 💜",
            reply_markup=keyboard
        )

    elif query.data == "menu":
        image = get_welcome_image()

        caption = (
            "👑 Welcome back to AYRSHIRE TERP QUEEN 👑\n\n"
            "Choose an option below:"
        )

        if image:
            with open(image, "rb") as photo:
                await query.message.reply_photo(
                    photo=photo,
                    caption=caption,
                    reply_markup=main_menu()
                )
        else:
            await query.message.reply_text(
                caption,
                reply_markup=main_menu()
            )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        regular_message
    )
)

print("AYRSHIRE TERP QUEEN BOT IS RUNNING 👑")

app.run_polling()
