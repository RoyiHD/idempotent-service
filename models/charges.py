from enum import Enum
from pydantic import BaseModel


class TransactionStatus(Enum):
    
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class IdempotentTransaction(BaseModel, extra='forbid'):
    
    transaction_amount: float
    transaction_recipient: str
    transaction_status: TransactionStatus
