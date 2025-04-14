from dotenv import load_dotenv
from fastapi import FastAPI, Form
from twilio.twiml.messaging_response import MessagingResponse
import requests
import os

load_dotenv()
API_URL = os.getenv("API_URL", "http://localhost:8000") # valor padrão caso null

app = FastAPI()

@app.post("/twilio-webhook")
async def twilio_webhook(Body: str = Form(...)):
    response = requests.post(f"{API_URL}/mensagem", json={"mensagem": Body})
    resposta = response.json().get("resposta", "Erro ao processar")
    
    twilio_resp = MessagingResponse()
    twilio_resp.message(resposta)
    return str(twilio_resp)
