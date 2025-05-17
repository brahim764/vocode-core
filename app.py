from fastapi import FastAPI, Request
import os
from vocode.streaming.telephony.server.base import TwilioInboundCallConfig
from vocode.streaming.telephony.server.twilio.twilio_phone_call_router import TwilioPhoneCallRouter
from vocode.streaming.agent.simple_agent import SimpleAgent
from vocode.streaming.input_device.twilio_input import TwilioInputAudioConfig
from vocode.streaming.output_device.eleven_labs_output import ElevenLabsOutputAudioConfig
from vocode.streaming.models.synthesizer import ElevenLabsSynthesizerConfig
from vocode.streaming.models.transcriber import TwilioTranscriberConfig
from vocode.streaming.models.telephony import TwilioConfig

app = FastAPI()

twilio_router = TwilioPhoneCallRouter(
    agent_thunk=lambda: SimpleAgent(
        prompt_preamble="Bonjour, ici la Clinique Dentaire Laurier. Voulez-vous prendre un rendez-vous, en modifier un ou poser une question ?"
    ),
    twilio_config=TwilioConfig(
        account_sid=os.environ["TWILIO_ACCOUNT_SID"],
        auth_token=os.environ["TWILIO_AUTH_TOKEN"],
        phone_number=os.environ["TWILIO_PHONE_NUMBER"]
    ),
    input_audio_config=TwilioInputAudioConfig(),
    output_audio_config=ElevenLabsOutputAudioConfig(
        config=ElevenLabsSynthesizerConfig(
            api_key=os.environ["ELEVENLABS_API_KEY"],
            voice_id=os.environ["ELEVENLABS_VOICE_ID"]
        )
    ),
    transcriber_config=TwilioTranscriberConfig(),
)

@app.post("/twilio")
async def twilio(request: Request):
    body = await request.body()
    return await twilio_router.handle_request(body)
