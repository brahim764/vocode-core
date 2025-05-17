from fastapi import FastAPI, Request
from vocode.streaming.telephony.twilio_signal import TwilioSignalHandler
from vocode.streaming.agent.simple_agent import SimpleAgent
from vocode.streaming.output.eleven_labs_output import ElevenLabsOutputAudioConfig
from vocode.streaming.input.twilio_input import TwilioInputAudioConfig
from vocode.streaming.models.telephony import TwilioConfig
import os

app = FastAPI()

@app.post("/twilio")
async def twilio_webhook(request: Request):
    handler = TwilioSignalHandler(
        agent=SimpleAgent(
            prompt_preamble="Bonjour ! Ici la Clinique Dentaire Laurier. Souhaitez-vous prendre un rendez-vous, en modifier un, ou poser une question ?"
        ),
        twilio_config=TwilioConfig(
            account_sid=os.environ["TWILIO_ACCOUNT_SID"],
            auth_token=os.environ["TWILIO_AUTH_TOKEN"],
            phone_number=os.environ["TWILIO_PHONE_NUMBER"],
        ),
        input_audio_config=TwilioInputAudioConfig(),
        output_audio_config=ElevenLabsOutputAudioConfig(
            api_key=os.environ["ELEVENLABS_API_KEY"],
            voice_id=os.environ["ELEVENLABS_VOICE_ID"]
        ),
    )
    return await handler.handle_signal(request)
