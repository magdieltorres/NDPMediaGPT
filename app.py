
from flask import Flask, request
import requests

app = Flask(__name__)

VERIFY_TOKEN = 'ndpgpt123'
WHATSAPP_TOKEN = 'EAALlA2pPBYkBP7JtGREIOBZAKT0OQLFXlLqD44aAiZB5ZCIOFhldAaxtAu0JUnFys5qtVREMNkK0c29X1FTcAeVWZAFwCbfGv0vrZBB33LNunKP4X3yMZCUa4BYZBojpEWcNojgniUhAdUJp91mVTSYH2ZCib1pXtUSjZA3qt9F1ZBl3kx91I2u3CM2B37KZBJqno2e5yfxP4kfZBAHpzTKA8ZBVwpP8OROJrW3lttugiUGz0WFkofoellKEW2cHVIZBy7OCDXmZCJEPgZBJQCk1EYHiKH98WP8LuE2m1orZC4ebK'
PHONE_NUMBER_ID = '862072523654615'
OPENAI_KEY = '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'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Token inválido", 403

    if request.method == 'POST':
        data = request.get_json()
        try:
            message = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            sender = data['entry'][0]['changes'][0]['value']['messages'][0]['from']

            gpt_response = requests.post(
                'https://api.openai.com/v1/chat/completions',
                headers={'Authorization': f'Bearer {OPENAI_KEY}'},
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": [{"role": "user", "content": message}]
                }
            ).json()

            reply = gpt_response['choices'][0]['message']['content']

            requests.post(
                f'https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages',
                headers={
                    'Authorization': f'Bearer {WHATSAPP_TOKEN}',
                    'Content-Type': 'application/json'
                },
                json={
                    "messaging_product": "whatsapp",
                    "to": sender,
                    "type": "text",
                    "text": {"body": reply}
                }
            )
        except Exception as e:
            print("Error:", e)
        return "ok", 200
