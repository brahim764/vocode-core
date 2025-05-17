from fastapi import FastAPI, Request
from fastapi.responses import Response

app = FastAPI()

@app.post("/twilio")
async def twilio_webhook(request: Request):
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say language="fr-FR" voice="alice">Bonjour, ici votre assistant virtuel.</Say>
</Response>"""
    return Response(content=xml, media_type="application/xml")

@app.get("/")
async def root():
    return {"message": "Voicebot backend running."}
