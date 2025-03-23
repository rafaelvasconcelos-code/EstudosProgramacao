from datetime import datetime
import requests


data_atual = datetime.now().strftime("%d/%m/%Y")
dia = datetime.now().strftime("%d")
mes = datetime.now().strftime("%m")
ano = datetime.now().strftime("%Y")


print(ano)

    # URL base do Católico Orante
url = f"https://liturgia.up.railway.app/v2/?dia={dia}&mes={mes}&ano={ano}"


try:
        # Faz a requisição para a página
    response = requests.get(url)
    print(response.text[1]["data"])
    response.raise_for_status()  # Verifica se houve erro na requisição
except requests.exceptions.RequestException as e:
    response="Nada"