from fastapi import APIRouter,Path,Query
from converter import sync_converter,async_converter
from asyncio import gather
from schema import ConvertInput,ConverterOutput
from typing import List

router = APIRouter(prefix="/convert")



@router.get("")
def converter():
    return "It Work"

@router.get("{from_currency}")
def converter(from_currency:str 
              ,to_currencies:str
              ,price:float 
                                   ):

    to_currencies = to_currencies.split(",")
    from_currency = from_currency.split(",")
    result = []

    for fcurrency in from_currency:
        for currencies in to_currencies:
            res = sync_converter(from_currency=fcurrency,
                                to_currency=currencies,
                                prince=price)
            result.append(res)


    return result

@router.get("async/{from_currency}")
async def asyn_converter(    
    from_currency:str = Path(max_length=50, regex="^[A-Z]{3}$")
     ,to_currencies:str = Query(max_length=50,regex="^[A-Z]{3}(,[A-Z]{3})*$")
     ,price:float = Query(gt=0)):
    
    to_currencies = to_currencies.split(",")
    from_currency = from_currency.split(",")
    coroutines = []

    for fcurrency in from_currency:
        for currencies in to_currencies:
            coro =  async_converter(from_currency=fcurrency,
                                to_currency=currencies,
                                prince=price)
            coroutines.append(coro)
    
    result = await gather(*coroutines)

    return result



@router.get("async/v2/{from_currency}",response_model=ConverterOutput)
async def asyn_converter_router(
    body:ConvertInput,
    from_currency:str = Path(max_length=50, regex="^[A-Z]{3}$")):


    to_currencies = body.to_currencies

    #to_currencies = teste.split(",")
    from_currency = from_currency.split(",")
    price = body.price


    coroutines = []
    print("Passou aqui")

    for fcurrency in from_currency:
        for currencies in to_currencies:
            coro =  async_converter(from_currency=fcurrency,
                                to_currency=currencies,
                                prince=price)
            coroutines.append(coro)
    
    result = await gather(*coroutines)

    return ConverterOutput(
        message="Sucess",
        data=result)