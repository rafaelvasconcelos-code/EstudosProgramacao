from pydantic import BaseModel,Field,field_validator
from typing import List
import re


class ConvertInput(BaseModel):
    to_currencies:List[str]
    price:float = Field(gt=0)
    

    @field_validator('to_currencies')
    def validator_to_currencies(cls,value):
        print("Passou aqui")
        for currencies in value:
            if not re.match("^[A-Z]{3}$",currencies):
                print("Passou aqui")
                raise ValueError(f"Invalid currency {currencies}")
        return value
    
class ConverterOutput(BaseModel):
    message:str
    data: List[dict]