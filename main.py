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
