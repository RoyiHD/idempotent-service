from pydantic import BaseModel


class ChargeResponse(BaseModel, extra='forbid'):
    
    message: str
    transaction_completed: str
