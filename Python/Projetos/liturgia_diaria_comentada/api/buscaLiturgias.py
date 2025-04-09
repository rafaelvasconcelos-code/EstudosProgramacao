from datetime import datetime
import requests

def busca_liturgia_atual(data):
    #data_atual = datetime.now().strftime("%d/%m/%Y")

    dia = data.strftime("%d")
    mes = data.strftime("%m")
    ano = data.strftime("%Y")

    url = f"https://liturgia.up.railway.app/v2/?dia={dia}&mes={mes}&ano={ano}"

    try:       
        response= requests.get(url=url)
            
    except Exception as error:
        raise requests.HTTPException(status_code=400,detail=error)
    
    data = response.json() 

    return data