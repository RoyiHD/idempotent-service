from functools import wraps
from typing import Any, Callable

from pydantic import BaseModel
from flask import g, request


def request_dto(dto_cls: type[BaseModel]) -> Callable:
    
    def decorator(route: Callable) -> Callable:
        
        @wraps(route) 
        def warpper(*args, **kwargs) -> Any:
            
            request_dto = g.request_dto = dto_cls.model_validate(request.json)
            
            return route(*args, **kwargs, request_dto=request_dto)
        return warpper
    return decorator
