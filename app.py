from fastapi import FastAPI, Request
from fastapi.responses import Response

app = FastAPI()

@app.post("/twilio")
async def twilio_voice_handler(request: Request):
    twiml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say voice="alice" language="fr-FR">Bonjour, ici votre assistant virtuel.</Say>
</Response>"""
    return Response(content=twiml, media_type="application/xml")

@app.get("/")
def read_root():
    return {"message": "Voicebot backend running."}
