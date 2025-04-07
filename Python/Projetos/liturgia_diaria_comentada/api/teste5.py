# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI
from fastapi import FastAPI,HTTPException
from datetime import datetime
import requests
import json
import re


app = FastAPI(title="Liturgia API")

def get_liturgia_api():

   try:
      client = OpenAI(api_key="sk-9f502773f7c64fd5a05d5992369b4656", base_url="https://api.deepseek.com")
      response = client.chat.completions.create(
       model="deepseek-chat",
       messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
       stream=False
          )
      return response.choices[0].message.content   
   except Exception as error:
      resultado = re.sub(r"Error code: \d+ - ", "", str(error))
      #erro_json = str(resultado).split("402 - ", 1)[1]
      string_erro = resultado.replace("'", '"').replace("None", "null")
      # Converter em dicionário
      objeto_json = json.loads(string_erro)
      # Converter de volta para string JSON
      json_string = json.dumps(objeto_json)
      return objeto_json["error"]["message"]
      #Mensagem_erro = erro_json.get("error", {}).get("message", "Erro desconhecido")
   

@app.get("/")
def get_liturgia():
    result= get_liturgia_api()
    return result