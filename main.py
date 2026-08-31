import os
import hashlib
from pathlib import Path

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]


# -----------------------------
# PERSONAL PHRASES
# -----------------------------

PHRASES = [
    "Pink Paradise",
    "Purple Dream",
    "Golden Queen",
    "Neon Nights",
    "Lucky Star",
    "Pink Diamond",
    "Purple Haze",
    "Moonlight",
    "Sweet Dreams",
    "Royal Queen",
    "Starlight",
    "Pink Cloud",
]


def personal_phrase(user_id):
    hashed = hashlib.sha256(str(user_id).encode()).hexdigest()
    number = int(hashed, 16)
    return PHRASES[number % len(PHRASES)]


# -----------------------------
# FIND WELCOME IMAGE
# -----------------------------

def get_welcome_image():
    allowed_extensions = [".png", ".jpg", ".jpeg", ".webp"]

    for file in Path(".").iterdir():
        if file.is_file() and file.suffix.lower() in allowed_extensions:
            return file

    return None


# -----------------------------
# MAIN MENU
# -----------------------------

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
                "💬 CHAT WITH US",
                url="https://t.me/+88mdil14i9gzYjU0"
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
                "💰 PRICE LIST",
                url="https://justpaste.it/Ayrshiregenetics"
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


# -----------------------------
# HOME SCREEN
# -----------------------------

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
                reply_markup=main_menu(),
            )
    else:
        await message.reply_text(
            caption,
            reply_markup=main_menu(),
        )


# -----------------------------
# COMMANDS
# -----------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_home(
        update.message,
        update.effective_user
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👑 ABOUT US 👑\n\n"
        "Welcome to AYRSHIRE TERP QUEEN.\n\n"
        "Use the menu below to navigate.",
        reply_markup=main_menu(),
    )


async def gallery(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📸 GALLERY\n\n"
        "Use the Gallery button below to view our gallery.",
        reply_markup=main_menu(),
    )


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💌 CONTACT US\n\n"
        "Use the Contact Us or Chat With Us button below.",
        reply_markup=main_menu(),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❓ HELP & INFORMATION\n\n"
        "📱 TELEGRAM — Open our Telegram\n"
        "🔒 SIGNAL — Open our Signal\n"
        "💬 CHAT WITH US — Join our chat\n"
        "📸 GALLERY — View our gallery\n"
        "👑 ABOUT US — Learn more about us\n"
        "💰 PRICE LIST — View the Luxe Resin Studio price list\n"
        "💌 CONTACT US — Contact us directly\n\n"
        "Type /start at any time to return to the main menu.",
        reply_markup=main_menu(),
    )


# -----------------------------
# BUTTONS
# -----------------------------

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    await query.answer()

    if query.data == "about":
        await query.message.reply_text(
            "👑 ABOUT US 👑\n\n"
            "Welcome to AYRSHIRE TERP QUEEN.\n\n"
            "Use the menu below to navigate.",
            reply_markup=main_menu(),
        )

    elif query.data == "help":
        await query.message.reply_text(
            "❓ HELP\n\n"
            "📱 Telegram\n"
            "🔒 Signal\n"
            "💬 Chat With Us\n"
            "📸 Gallery\n"
            "👑 About Us\n"
            "💰 Luxe Resin Studio Price List\n"
            "💌 Contact Us\n\n"
            "Type /start at any time to reopen the menu.",
            reply_markup=main_menu(),
        )


# -----------------------------
# OTHER MESSAGES
# -----------------------------

async def unknown_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👑 Use the menu below or type /start.",
        reply_markup=main_menu(),
    )


# -----------------------------
# RUN BOT
# -----------------------------

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("gallery", gallery))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(CallbackQueryHandler(button_handler))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            unknown_message
        )
    )

    print("Ayrshire Telegram Bot is running...", flush=True)

    app.run_polling()


if __name__ == "__main__":
    main()
