import os
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.post("/twilio")
async def twilio_webhook(request: Request):
    # Pour debug simple, on imprime ce qu'on reçoit
    data = await request.body()
    print("Twilio Webhook Received:", data)

    # Réponse vide attendue par Twilio pour accuser réception
    return PlainTextResponse("<Response></Response>", media_type="text/xml")

@app.get("/")
def read_root():
    return {"message": "Voicebot backend running."}
