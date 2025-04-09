from google import genai
import json
import firebase_admin
from firebase_admin import credentials, storage,db
import os
from datetime import datetime


def gerar_arquivo(dados_json,data):
   
   cred = credentials.Certificate(".\leitura-diaria-comentada-a893f-firebase-adminsdk-fbsvc-be6fa2af8c.json")
   if not firebase_admin._apps:
      firebase_admin.initialize_app(cred, {
      'storageBucket': 'leitura-diaria-comentada-a893f.firebasestorage.app'  # Seu bucket
      })

# Converter o dicionário pra string JSON
   dados_string = json.dumps(dados_json).encode('utf-8')

# Conectar ao bucket
   bucket = storage.bucket()

   data_atual_formatada = data.strftime("%Y%m%d")

# Definir o caminho no Storage onde o arquivo será salvo
   caminho_no_storage = f'leituraDiaria/{data_atual_formatada}.json'

# Fazer upload diretamente da string
   try:
       blob = bucket.blob(caminho_no_storage)
       blob.upload_from_string(dados_string, content_type='application/json')
   except Exception as e:
       print(f"Erro ao gravar o JSON: {e}")


def ler_arquivo():
   # Caminho do seu arquivo .json da conta de serviço
   credenciais_path = ".\leitura-diaria-comentada-a893f-firebase-adminsdk-fbsvc-be6fa2af8c.json"

# Nome do seu bucket do Firebase (geralmente algo como "nomedoprojeto.appspot.com")
   bucket_name = "leitura-diaria-comentada-a893f.firebasestorage.app"

# Nome do arquivo que você quer acessar no storage
   arquivo_path = "versiculos/dados.json"
   arquivo_destino = "arquivo-baixado.json"



# Inicializa o cliente
   storage_client = storage.Client.from_service_account_json(credenciais_path)

# Acessa o bucket
   bucket = storage_client.bucket(bucket_name)

# Pega o blob (arquivo)
   blob = bucket.blob(arquivo_path)

   # Lê o conteúdo como string
   conteudo = blob.download_as_text()

# Converte para dicionário
   dados = json.loads(conteudo)

   print(dados)

# Baixa o arquivo
   #blob.download_to_filename(arquivo_destino)

   print(f"Arquivo salvo como {arquivo_destino}") 