from flask import Flask, request
import requests
import os

TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    message = request.data.decode("utf-8")
    
    text = f"📊 Signal:\n{message}"
    
    requests.get(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": text}
    )
    
    return {"status": "ok"}

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == "__main__":
    app.run()
