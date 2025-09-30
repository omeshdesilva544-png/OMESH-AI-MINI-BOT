from flask import Flask, request
import os
from dotenv import load_dotenv
import openai
from twilio.twiml.messaging_response import MessagingResponse

load_dotenv()
app = Flask(__name__)

BOT_NAME = "OMESH AI MINI BOT"

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ai_reply(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or your preferred model
        messages=[
            {"role": "system", "content": f"You are {BOT_NAME}, a Sinhala-English sniper-style trading assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content.strip()

@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body", "")
    reply = generate_ai_reply(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
