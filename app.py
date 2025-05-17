from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Voicebot backend running."}

@app.post("/twilio")
async def twilio_webhook(request: Request):
    response_xml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say>Bonjour, ici votre assistant virtuel.</Say>
</Response>"""
    return Response(content=response_xml, media_type="application/xml")
