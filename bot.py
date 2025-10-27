import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# === BOT SETTINGS ===
BOT_TOKEN = "8095856335:AAELT9NIm_mxREHMvykzkJHiOnrwC9XQv60"
CHANNEL_LINK = = "https://t.me/+gwpx1n_VBZJmNzc0"
GROUP_LINK = = "https://t.me/+CjcVnktCaC8wMDVk"
ADMIN_LINK = "https://t.me/Mon3yMoTime"
# =====================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name or user.username or "there"

    text = (
        f"*{name.upper()}, JOIN UP QUICK – STAY PLUGGED IN FOR EVERYDAY FRESH FULLZ & CRYPTO LEADS UPDATE!* 🏪🥇\n\n"
        "🔥 *FORWARD THIS MSG TO 15+ CONTACTS & GROUP CHATS, YOUR SUPPORT MEANS A LOT!* 👏\n\n"
        "💎 *PM @Mon3yMoTime FOR FREE LIST – DON’T SLEEP ON IT. LET’S GET IT BUZZING!* 💼📹"
    )

    # Vertical keyboard layout (one button per row)
    keyboard = [
        [InlineKeyboardButton("💬 CONTACT MO", url=ADMIN_LINK)],
        [InlineKeyboardButton("📢 JOIN CHANNEL", url=CHANNEL_LINK)],
        [InlineKeyboardButton("💬 JOIN GROUP CHAT", url=GROUP_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    message_obj = update.message or update.effective_message
    if message_obj is None:
        return

    try:
        await message_obj.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')
    except Exception:
        logger.exception("Failed to send start message (error swallowed to avoid crash)")

# Global error handler — prevents 'No error handlers are registered' warning
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.exception("Exception while handling an update: %s", context.error)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_error_handler(error_handler)
    app.run_polling()

if name == "__main__":
    main()
