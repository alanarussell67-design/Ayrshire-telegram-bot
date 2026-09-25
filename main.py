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


# ==================================================
# TELEGRAM TOKEN
# ==================================================

# Telegram token stored safely in Railway
TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]


# ==================================================
# PERSONAL PHRASES
# ==================================================

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
    """Give each user the same personal phrase when they return."""

    hashed = hashlib.sha256(str(user_id).encode()).hexdigest()
    number = int(hashed, 16)

    return PHRASES[number % len(PHRASES)]


# ==================================================
# FIND WELCOME IMAGE
# ==================================================

def get_welcome_image():
    """Find the welcome image stored in the GitHub project."""

    allowed_extensions = [".png", ".jpg", ".jpeg", ".webp"]

    for file in Path(".").iterdir():
        if file.is_file() and file.suffix.lower() in allowed_extensions:
            return file

    return None


# ==================================================
# MAIN MENU
# ==================================================

def main_menu():

    return InlineKeyboardMarkup([

        # SIGNAL
        [
            InlineKeyboardButton(
                "🔒 SIGNAL",
                url="https://signal.group/#CjQKIG_ywqWkwZ5CjvGpO_LlndovLwrGfxDd3ztRLegnm7AMEhCgPly_ZSYmHr9Yf_Sg7ITL"
            ),
        ],

        # TELEGRAM CHAT
        [
            InlineKeyboardButton(
                "💬 TELEGRAM CHAT",
                url="https://t.me/+88mdil14i9gzYjU0"
            ),
        ],

        # WHATSAPP GROUP
        [
            InlineKeyboardButton(
                "💚 WHATSAPP GROUP",
                url="https://chat.whatsapp.com/CYX2rinp56LDiZiqVriVLS"
            ),
        ],

        # GALLERY + ABOUT
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

        # PRICE LIST
        [
            InlineKeyboardButton(
                "💰 PRICE LIST",
                url="https://justpaste.it/Ayrshiregenetics"
            ),
        ],

        # CONTACT + HELP
        [
            InlineKeyboardButton(
                "💌 CONTACT US",
                url="https://wa.me/447546338571"
            ),

            InlineKeyboardButton(
                "❓ HELP",
                callback_data="help"
            ),
        ],

    ])


# ==================================================
# HOME SCREEN
# ==================================================

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


# ==================================================
# /START
# ==================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await send_home(
        update.message,
        update.effective_user
    )


# ==================================================
# /ABOUT
# ==================================================

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        """💗 👑 ABOUT US 👑 💗

🚗 DELIVERY TIME SLOTS

🕑 2PM DELIVERY RUN
🕔 5PM DELIVERY RUN

Please have your order in before the run time.

⚠️ If you order after the 2PM run has left, your order will go onto the 5PM run.

📍 COLLECTIONS

Collections are available throughout the day 🤙

Message us when you're ready to collect and we'll arrange everything with you.

💷 PLEASE NOTE

💵 CASH ONLY

❌ NO TICK
❌ NO TRANSFERS
❌ NO DAFTYS 👀😂

Keep it simple, keep it sweet 💚🤙""",
        reply_markup=main_menu(),
    )


# ==================================================
# /GALLERY
# ==================================================

async def gallery(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "📸 GALLERY\n\n"
        "Press the Gallery button below to view our gallery.",
        reply_markup=main_menu(),
    )


# ==================================================
# /CONTACT
# ==================================================

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "💌 CONTACT US\n\n"
        "Press the Contact Us button below to message us directly on WhatsApp.",
        reply_markup=main_menu(),
    )


# ==================================================
# /HELP
# ==================================================

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "❓ HELP & INFORMATION\n\n"

        "🔒 SIGNAL — Open our Signal community\n\n"

        "💬 TELEGRAM CHAT — Open our Telegram chat\n\n"

        "💚 WHATSAPP GROUP — Join our WhatsApp group\n\n"

        "📸 GALLERY — View our gallery\n\n"

        "👑 ABOUT US — Find out more about us\n\n"

        "💰 PRICE LIST — View our price list\n\n"

        "💌 CONTACT US — Message us directly on WhatsApp\n\n"

        "Type /start at any time to return to the main menu.",

        reply_markup=main_menu(),
    )


# ==================================================
# BUTTON CALLBACKS
# ==================================================

async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    # ==================================================
    # ABOUT US
    # ==================================================

    if query.data == "about":

        await query.message.reply_text(
            """💗 👑 ABOUT US 👑 💗

🚗 DELIVERY TIME SLOTS

🕑 2PM DELIVERY RUN
🕔 5PM DELIVERY RUN

Please have your order in before the run time.

⚠️ If you order after the 2PM run has left, your order will go onto the 5PM run.

📍 COLLECTIONS

Collections are available throughout the day 🤙

Message us when you're ready to collect and we'll arrange everything with you.

💷 PLEASE NOTE

💵 CASH ONLY

❌ NO TICK
❌ NO TRANSFERS
❌ NO DAFTYS 👀😂

Keep it simple, keep it sweet 💚🤙""",
            reply_markup=main_menu(),
        )


    # ==================================================
    # HELP
    # ==================================================

    elif query.data == "help":

        await query.message.reply_text(
            "❓ HELP & INFORMATION\n\n"

            "🔒 SIGNAL — Open our Signal community\n\n"

            "💬 TELEGRAM CHAT — Open our Telegram chat\n\n"

            "💚 WHATSAPP GROUP — Join our WhatsApp group\n\n"

            "📸 GALLERY — View our gallery\n\n"

            "👑 ABOUT US — Find out more about us\n\n"

            "💰 PRICE LIST — View our price list\n\n"

            "💌 CONTACT US — Message us directly on WhatsApp\n\n"

            "Type /start at any time to reopen the main menu.",

            reply_markup=main_menu(),
        )


# ==================================================
# OTHER MESSAGES
# ==================================================

async def unknown_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "👑 Use the buttons below or type /start to open the main menu.",
        reply_markup=main_menu(),
    )


# ==================================================
# RUN THE BOT
# ==================================================

def main():

    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("about", about)
    )

    app.add_handler(
        CommandHandler("gallery", gallery)
    )

    app.add_handler(
        CommandHandler("contact", contact)
    )

    app.add_handler(
        CommandHandler("help", help_command)
    )

    # About / Help buttons
    app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    # Other text messages
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            unknown_message
        )
    )

    print(
        "Ayrshire Telegram Bot is running...",
        flush=True
    )

    # Keep bot running continuously
    app.run_polling()


# ==================================================
# START
# ==================================================

if __name__ == "__main__":
    main()
