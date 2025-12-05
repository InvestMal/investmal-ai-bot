import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler
from app.config import TELEGRAM_TOKEN, WEBHOOK_URL, PORT
from app.handlers.start import start

async def main():
    # إنشاء التطبيق
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # إضافة أوامر البوت
    app.add_handler(CommandHandler("start", start))

    # تشغيل Webhook
    await app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TELEGRAM_TOKEN,
        webhook_url=f"{WEBHOOK_URL}/{TELEGRAM_TOKEN}"
    )

if __name__ == "__main__":
    asyncio.run(main())
