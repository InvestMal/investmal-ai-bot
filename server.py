from flask import Flask, request
import os
import bot  # استدعاء ملف البوت الرئيسي

app = Flask(__name__)

@app.route('/')
def home():
    return "InvestMal AI Bot Running Successfully!"

@app.route(f"/{os.environ.get('TELEGRAM_TOKEN')}", methods=["POST"])
def webhook():
    update = request.get_json()
    bot.dp.update_queue.put(update)  # إرسال التحديث للبوت
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
