from pydantic import BaseModel


class ChargeRequest(BaseModel, extra='forbid'):
    
    amount: float
    recipient: str
