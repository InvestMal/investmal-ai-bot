#!/bin/bash

echo "🔧 Creating clean project structure for Telegram Bot..."

# إنشاء مجلد التطبيق
mkdir -p app/handlers

# إنشاء ملف config.py
cat <<EOF > app/config.py
import os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
PORT = int(os.environ.get("PORT", 10000))
EOF

echo "✔️ Created app/config.py"

# إنشاء start handler
cat <<EOF > app/handlers/start.py
from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("InvestMal AI Bot Active!")
EOF

echo "✔️ Created app/handlers/start.py"

# __init__.py
echo "" > app/__init__.py

# كتابة bot.py نظيف
cat <<EOF > bot.py
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler
from app.config import TELEGRAM_TOKEN, WEBHOOK_URL, PORT
from app.handlers.start import start

async def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    await app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TELEGRAM_TOKEN,
        webhook_url=f"{WEBHOOK_URL}/{TELEGRAM_TOKEN}"
    )

if __name__ == "__main__":
    asyncio.run(main())
EOF

echo "✔️ Created clean bot.py"

# إعادة إنشاء runtime.txt
echo "python-3.10.12" > runtime.txt
echo "✔️ Created runtime.txt"

# إعادة إنشاء requirements.txt
cat <<EOF > requirements.txt
python-telegram-bot==20.7
EOF
echo "✔️ Created requirements.txt"

# README.md احترافي
cat <<EOF > README.md
# InvestMal AI Telegram Bot

This is a clean and structured Telegram Bot designed for deployment on Render using Webhook.

## 🚀 Project Structure

\`\`\`
bot.py
app/
  ├── config.py
  ├── __init__.py
  └── handlers/
      └── start.py
\`\`\`

## 🛠️ Deployment on Render

1. Set environment variables:
   - TELEGRAM_TOKEN
   - WEBHOOK_URL
2. Add Start Command:
   \`\`\`
   python bot.py
   \`\`\`
3. Make sure runtime.txt contains:
   \`\`\`
   python-3.10.12
   \`\`\`

## ✔️ Supported:
- Webhook only
- python-telegram-bot v20+

EOF

echo "✔️ Created README.md"

echo "🎉 DONE! Your bot project is now fully organized and ready for deployment."
echo "➡️ Next steps:"
echo "   git add ."
echo "   git commit -m 'Clean bot structure for Render'"
echo "   git push"
