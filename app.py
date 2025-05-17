from fastapi import FastAPI, Request
from fastapi.responses import Response

app = FastAPI()

@app.post("/twilio")
async def twilio_webhook(request: Request):
    twiml_response = """
    <?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Say voice="alice" language="fr-FR">Bonjour, ici votre assistant virtuel.</Say>
    </Response>
    """
    return Response(content=twiml_response, media_type="application/xml")
