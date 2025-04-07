from fastapi import FastAPI
from datetime import datetime
import requests
import json

# Abrir e ler o arquivo JSON
dados=[]
with open('resultado.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)


app = FastAPI(title="Liturgia API")

def busca_liturgia_atual():
    data_atual = datetime.now().strftime("%d/%m/%Y")

    dia = datetime.now().strftime("%d")
    mes = datetime.now().strftime("%m")
    ano = datetime.now().strftime("%Y")

    url = f"https://liturgia.up.railway.app/v2/?dia={dia}&mes={mes}&ano={ano}"

    try:
        print(url)        
        response= requests.get(url=url)
            
    except Exception as error:
        raise HTTPException(status_code=400,detail=error)
    data = response.json() 

    return data

@app.get("/")
def get_liturgia():

    """
    Retorna os dados da liturgia do dia
    """
    data = dados["data"]
    data = dados["liturgia"]
    data = dados["leituras"]["primeiraLeitura"][0]["referencia"]

    return data

    # Sua chave de API
API_KEY = "xai-GaQkiizgeY4QHKsJGdBE9g0RtTACBOzZOvSY7iWuhTutjKFZIl2FkEmuKSBXhDfQG1ti0GK3YhEOiyjS"  # Substitua pela sua chave real

# URL da API da xAI (verifique a documentação oficial para o endpoint exato)
API_URL = "https://api.xai.com/v1/chat/completions"  # Hypothetical endpoint

# Headers para autenticação
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

pergunta = "Explique de forma detalhada o Ex 3,1-8.13-15 da Bíblia, fazendo um contexto da realidade atual."

payload = {
    "model": "grok",  # Especifica que quer usar o Grok (pode variar, veja a doc)
    "messages": [
        {"role": "system", "content": "Responda em português do Brasil."},
        {"role": "user", "content": pergunta}
    ],
     "model": "grok-2-latest",
      "stream":False ,
    #"max_tokens": 1000,  # Limite de tokens na resposta (ajuste conforme necessário)
    "temperature": 0.0  # Controla a criatividade da resposta (0 a 1)
}

try:
    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
    response.raise_for_status()  # Levanta um erro se a requisição falhar

    # Extrair a resposta
    resposta = response.json()
    texto_resposta = resposta#["choices"][0]["message"]["content"]
    print("Resposta do Grok:")
    print(texto_resposta)

except requests.exceptions.RequestException as e:
    print(f"Erro ao chamar a API: {e}")