from enum import Enum
from typing import Optional
from pydantic import BaseModel


# More info about these structures:
# https://cloud.google.com/dialogflow/es/docs/fulfillment-webhook#webhook_request
# https://cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Message
# https://cloud.google.com/dialogflow/es/docs/reference/rest/v2/WebhookResponse


class Platform(Enum):
    PLATFORM_UNSPECIFIED = "PLATFORM_UNSPECIFIED"


class TextObject(BaseModel):
    text: list[str]


class Message(BaseModel):
    platform: Platform
    text: TextObject


class Context(BaseModel):
    """
    https://cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions.contexts#Context
    """

    name: str
    lifespanCount: Optional[int]
    parameters: Optional[dict]


class QueryResult(BaseModel):
    queryText: str
    languageCode: str
    speechRecognitionConfidence: Optional[str] | None
    action: str
    parameters: dict
    allRequiredParamsPresent: bool
    cancelsSlotFilling: Optional[bool] | None
    fulfillmentText: Optional[str] | None
    fulfillmentMessages: Optional[list] | None
    webhookSource: Optional[str] | None
    webhookPayload: Optional[dict] | None
    outputContexts: list
    intent: dict
    intentDetectionConfidence: float
    diagnosticInfo: Optional[dict] | None
    sentimentAnalysisResult: Optional[dict] | None


class Payload(BaseModel):
    """Response payload from WhatsApp Only."""

    From: Optional[str] | None  # "whatsapp:+584123130000"
    To: Optional[str] | None  # "whatsapp:+18045340000"
    ProfileName: Optional[str] | None


class OriginalDetectIntentRequest(BaseModel):
    source: Optional[str] | None
    version: Optional[str] | None
    payload: Payload


class DialogFlowRequest(BaseModel):
    """
    https://cloud.google.com/dialogflow/es/docs/reference/rest/v2/WebhookRequest
    """

    session: str
    responseId: str
    queryResult: QueryResult
    originalDetectIntentRequest: OriginalDetectIntentRequest


class DialogFlowResponse(BaseModel):
    """
    https://cloud.google.com/dialogflow/es/docs/reference/rest/v2/WebhookResponse
    """

    fulfillmentText: str
    # fulfillmentMessages: list[Message] | None
    source: Optional[str] | None
    # payload: dict
    outputContexts: Optional[list[Context]]
    # followupEventInput: EventInput
    # sessionEntityTypes: list[SessionEntityType]
