import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Bot token (BotFather से लिया हुआ)
BOT_TOKEN = "YOUR_BOT_TOKEN"

# QR Code image ka path
QR_CODE_PATH = "payment_qr.png"

# Logging enable
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("नमस्ते! 'pay' लिखो और मैं तुम्हें Payment QR भेजूँगा।")

# Jab user 'pay' likhe
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "pay" in text:
        msg = await update.message.reply_photo(photo=open(QR_CODE_PATH, "rb"), caption="यह रहा आपका Payment QR Code ✅")

        # 30 सेकंड बाद QR Code auto delete
        await context.bot.delete_message(chat_id=update.message.chat_id, message_id=msg.message_id, delay=30)

# Main function
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
