from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/swml")
async def swml_handler(request: Request):
    data = await request.json()

    # Exemple de réponse simple
    response = {
        "version": "1.0.0",
        "sections": {
            "main": [
                {"say": {"text": "Bonjour et bienvenue chez notre clinique dentaire. Veuillez patienter."}}
            ]
        }
    }

    return JSONResponse(content=response)

@app.get("/")
def root():
    return {"message": "Voicebot backend running."}
