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


# -------------------------
# WELCOME IMAGE
# -------------------------

def get_welcome_image():
    for file in Path(".").iterdir():
        if file.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp"]:
            return file
    return None


# -------------------------
# PERSONAL PHRASES
# -------------------------

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


# -------------------------
# MAIN MENU
# -------------------------

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
                "❓ HELP",
                callback_data="help"
            ),
        ],
    ])


# -------------------------
# HOME SCREEN
# -------------------------

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


# -------------------------
# /START
# -------------------------

async def start(update, context):
    await send_home(
        update.message,
        update.effective_user
    )


# -------------------------
# ABOUT COMMAND
# -------------------------

async def about_command(update, context):

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🏠 MAIN MENU",
                callback_data="menu"
            )
        ]
    ])

    await update.message.reply_text(
        "👑 AYRSHIRE TERP QUEEN 👑\n\n"
        "Welcome to our community hub.\n\n"
        "📸 Gallery\n"
        "📱 Telegram community\n"
        "🔒 Signal\n"
        "💌 Contact us\n\n"
        "Good vibes • Community • Ayrshire 💜",
        reply_markup=keyboard
    )


# -------------------------
# GALLERY COMMAND
# -------------------------

async def gallery_command(update, context):

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "📸 OPEN GALLERY",
                url="https://t.me/+IFm1y-zt9txkZWE0"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 MAIN MENU",
                callback_data="menu"
            )
        ]
    ])

    await update.message.reply_text(
        "📸 GALLERY\n\n"
        "Tap below to view the gallery:",
        reply_markup=keyboard
    )


# -------------------------
# CONTACT COMMAND
# -------------------------

async def contact_command(update, context):

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "💌 MESSAGE US",
                url="https://t.me/Terpqueenayrshire"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 MAIN MENU",
                callback_data="menu"
            )
        ]
    ])

    await update.message.reply_text(
        "💌 CONTACT US\n\n"
        "Tap below to get in touch:",
        reply_markup=keyboard
    )


# -------------------------
# HELP COMMAND
# -------------------------

async def help_command(update, context):

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🏠 MAIN MENU",
                callback_data="menu"
            )
        ]
    ])

    await update.message.reply_text(
        "❓ HELP & INFORMATION\n\n"
        "/start - Open the main menu\n"
        "/about - About us\n"
        "/gallery - View the gallery\n"
        "/contact - Contact us\n"
        "/help - Show help",
        reply_markup=keyboard
    )


# -------------------------
# BUTTON PRESSES
# -------------------------

async def button(update, context):

    query = update.callback_query
    await query.answer()

    if query.data == "about":

        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "🏠 MAIN MENU",
                    callback_data="menu"
                )
            ]
        ])

        await query.message.reply_text(
            "👑 AYRSHIRE TERP QUEEN 👑\n\n"
            "Welcome to our community hub.\n\n"
            "📸 Gallery\n"
            "📱 Telegram community\n"
            "🔒 Signal\n"
            "💌 Contact us\n\n"
            "Good vibes • Community • Ayrshire 💜",
            reply_markup=keyboard
        )

    elif query.data == "help":

        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "🏠 MAIN MENU",
                    callback_data="menu"
                )
            ]
        ])

        await query.message.reply_text(
            "❓ HELP & INFORMATION\n\n"
            "Use the buttons on the main menu to navigate.\n\n"
            "👑 About Us\n"
            "📸 Gallery\n"
            "📱 Telegram\n"
            "🔒 Signal\n"
            "💌 Contact Us",
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


# -------------------------
# NORMAL MESSAGES
# -------------------------

async def regular_message(update, context):
    await send_home(
        update.message,
        update.effective_user
    )


# -------------------------
# START BOT
# -------------------------

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("about", about_command))
app.add_handler(CommandHandler("gallery", gallery_command))
app.add_handler(CommandHandler("contact", contact_command))
app.add_handler(CommandHandler("help", help_command))

app.add_handler(CallbackQueryHandler(button))

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        regular_message
    )
)

print("AYRSHIRE TERP QUEEN BOT IS RUNNING 👑")

app.run_polling()
