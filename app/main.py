# main.py - Main FastAPI application.
# Copyright (C) 2022 Lino Urdaneta.


# ----- Run the application -----
# $ uvicorn main:app --reload
# ----- Documentation -----
# http://127.0.0.1:8000/docs (local)

# ----- Imports -----

from fastapi import FastAPI, HTTPException, Response, Depends
from app.models import DialogFlowRequest, DialogFlowResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Sanity Check": "OK"}


@app.post("/dialogflow-webhook")
async def dialogflow_request(request: DialogFlowRequest):
    action = request.queryResult.action
    match action:
        case "intent_1":
            response_text = "Esta es la respuesta 1."
        case "intent_2":
            response_text = "Esta es la respuesta 2."
    response = DialogFlowResponse(fulfillmentText=response_text, source="webhookdata")

    return response

