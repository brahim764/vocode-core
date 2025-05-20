from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/swml")
async def swml_handler(request: Request):
    # Script simple de test bilingue
    swml_script = {
        "version": "1.0.0",
        "sections": {
            "main": [
                {"say": {"text": "Bonjour et bienvenue chez notre clinique dentaire."}},
                {"say": {"text": "Hello and welcome to our dental clinic."}},
                {"collect": {
                    "name": "choice",
                    "questions": [
                        {"question": {
                            "name": "intent",
                            "question": "Souhaitez-vous prendre, modifier ou annuler un rendez-vous?",
                            "question_en": "Would you like to book, modify or cancel an appointment?"
                        }}
                    ],
                    "on_complete": {"redirect": "main"}
                }}
            ]
        }
    }
    return JSONResponse(content=swml_script)
