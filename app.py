from fastapi import FastAPI, Request
from vocode.streaming.telephony.server.twilio import TwilioInboundCallConfig, TwilioInboundCallHandler
import os

app = FastAPI()

call_handler = TwilioInboundCallHandler(
    TwilioInboundCallConfig(
        url=os.getenv("BASE_URL") + "/twilio",  # Exemple : https://nexttalkai-voicebot.onrender.com/twilio
        use_speaker_embeddings=False
    )
)

@app.post("/twilio")
async def twilio_endpoint(request: Request):
    return await call_handler.handle_request(request)
