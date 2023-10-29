from base64 import b64encode
import os
from flask import Flask, request
from typing import Dict
from decorators import request_dto, response_dto
from routes.v1.dtos import ChargeRequest, ChargeResponse
from werkzeug.datastructures import Headers
from models import IdempotentTransaction, TransactionStatus


datastore: Dict[str, IdempotentTransaction] = dict()
IDEMPOTENCY_TOKEN = "idempotency-token"


def register_routes(app: Flask) -> None:
    
    @app.post("/api/v1/charge")
    @request_dto(ChargeRequest)
    @response_dto(ChargeResponse)
    def create_charge(request_dto: ChargeRequest) -> ChargeResponse:
        """
        This api only supports idempotent requests. For non idempotent request use xxx

        """
        headers: Headers = request.headers

        # We could wrap this as a decorator 
        if IDEMPOTENCY_TOKEN not in headers:
            raise Exception("Idempotent header is missing from request")
        
        token: str = headers[IDEMPOTENCY_TOKEN]

        if token in datastore:
            transaction = datastore[token]
            return ChargeResponse(
                message="Operation completed", 
                transaction_completed=transaction.transaction_status.value
            )
        try:
            # Process charge and record in the db
            # Processing ...

            datastore[token] = IdempotentTransaction(
                transaction_amount=request_dto.amount, 
                transaction_recipient=request_dto.recipient,
                transaction_status=TransactionStatus.SUCCESS,
            )
        except:
            return ChargeResponse(message="Could not process charge", transaction_completed=TransactionStatus.FAILURE.value)
        
        return ChargeResponse(message="operation_successful", transaction_completed=datastore[token].transaction_status.value)
            

    
