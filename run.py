 from flask import Flask, request
import requests
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

BOT_NAME = "OMESH AI MD BOT"

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.json.get('Body', '')
    reply = generate_ai_response(incoming_msg)
    send_whatsapp_message(reply)
    return "OK", 200

def generate_ai_response(text):
    # Replace with actual AI logic
    return f"{BOT_NAME} says: {text[::-1]}"

def send_whatsapp_message(msg):
    # Add WhatsApp API logic here (Meta or Twilio)
    print(f"Sending: {msg}")

if __name__ == '__main__':
    app.run() 
