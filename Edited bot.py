from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Dispatcher
import os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

# إنشاء البوت
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# مثال على /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("InvestMal AI Bot Active!")

app.add_handler(CommandHandler("start", start))

# إعداد Webhook
async def main():
    await app.bot.set_webhook(WEBHOOK_URL + "/" + TELEGRAM_TOKEN)
    print("Webhook is set!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
