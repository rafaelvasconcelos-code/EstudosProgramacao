from datetime import datetime
import requests
import json



def ler_json_metodo1():
    try:
        with open('resultado.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print("Erro: O arquivo 'resultado.json' não foi encontrado")
        return None
    except json.JSONDecodeError:
        print("Erro: O arquivo contém JSON inválido")
        return None
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")
        return None
        

data_atual = datetime.now().strftime("%d/%m/%Y")
dia = datetime.now().strftime("%d")
mes = datetime.now().strftime("%m")
ano = datetime.now().strftime("%Y")


    # URL base do Católico Orante
url = f"https://liturgia.up.railway.app/v2/?dia={dia}&mes={mes}&ano={ano}"

try:
        # Faz a requisição para a página
    response = ler_json_metodo1() #requests.get(url)
    response2 = responseAPILeitura(response)

    #print(response.text)

    

    data = response["data"]
    liturgia = response["liturgia"]
    cor = response["cor"]
    oracoes = response["oracoes"]
    leituras = response["leituras"]
    antifonas = response["antifonas"]

    print(response["data"])
    print(response["liturgia"])
    print(response["oracoes"])
    print(response["leituras"])
    print(response["antifonas"])
    
except requests.exceptions.RequestException as e:
    response="Nada"