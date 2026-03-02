from flask import Flask, request
import requests
import os
import threading

TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

app = Flask(__name__)

def send_to_telegram(message):
    requests.get(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": message}
    )

@app.route('/webhook', methods=['POST'])
def webhook():
    message = request.data.decode("utf-8")
    text = f"📊 Signal:\n{message}"

    threading.Thread(target=send_to_telegram, args=(text,)).start()

    return "ok", 200

@app.route('/')
def home():
    return "Bot is running!"
