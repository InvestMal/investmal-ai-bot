import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")  # مثال: https://investmal-ai-bot.onrender.com

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("InvestMal AI Bot Active!")

async def main():
    # إنشاء التطبيق
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # إضافة الهاندلرز
    app.add_handler(CommandHandler("start", start))

    # تشغيل Webhook Server
    await app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        url_path=TELEGRAM_TOKEN,
        webhook_url=f"{WEBHOOK_URL}/{TELEGRAM_TOKEN}"
    )

if __name__ == "__main__":
    asyncio.run(main())
