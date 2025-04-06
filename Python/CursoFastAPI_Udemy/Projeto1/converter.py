import requests
from fastapi import HTTPException,Path
import aiohttp

from os import getenv #Buscar variaveis de amibiente

ALPHAVANTAGE_APIKEY = getenv('ALPHAVANTAGE_APIKEY')

def sync_converter(from_currency:str, to_currency:str,prince: float):
    url=f"https://economia.awesomeapi.com.br/json/{from_currency}-{to_currency}"

    try:
        print(url)        
        response= requests.get(url=url)
        
    except Exception as error:
        raise HTTPException(status_code=400,detail=error)

    data = response.json()   

    print(data)
    if "code" not in str(data):
        raise HTTPException(status_code=400,detail="code não está nos dados")
    
    try:
        erro = data["status"]
    except Exception as error:
        erro=error

    if str(erro) == "404":        
        message = data["message"]
        raise HTTPException(status_code=400,detail=message)
    
    valor = float(data[0]["bid"])

    return valor*prince


async def async_converter(from_currency:str, to_currency:str,prince: float):
    url=f"https://economia.awesomeapi.com.br/json/{from_currency}-{to_currency}"

    try:
        print(url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                 data = await response.json()   
    except Exception as error:
        raise HTTPException(status_code=400,detail=error)

    if "code" not in str(data):
        "Está nos nossos dados"
        raise HTTPException(sstringtatus_code=400,detail="code não está nos dados")
    
    valor = float(data[0]["bid"])

    return {to_currency: valor*prince}