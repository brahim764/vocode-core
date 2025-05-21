from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/swml")
async def swml_handler(request: Request):
    swml_script = {
        "version": "1.0.0",
        "sections": {
            "main": [
                {
                    "say": {
                        "text": "Bonjour et bienvenue chez notre clinique dentaire. Veuillez patienter."
                    }
                }
            ]
        }
    }
    # FORCE application/json header
    return JSONResponse(content=swml_script, media_type="application/json")

@app.get("/")
async def root():
    return {"message": "Voicebot backend is running"}
