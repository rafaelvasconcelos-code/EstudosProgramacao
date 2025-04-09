from buscaLiturgias import busca_liturgia_atual
from datetime import datetime,timedelta
from apiGeminai import gera_resumo
from CrudFirebase import gerar_arquivo
import time

formato = "%d/%m/%Y"
Data_inicio = datetime.strptime("01/02/2025", formato).date()
Data_fim = datetime.strptime("01/11/2025", formato).date()

while Data_inicio<Data_fim:

    liturgia_hoje = busca_liturgia_atual(Data_inicio)


    primeiraLeitura = liturgia_hoje["leituras"]["primeiraLeitura"][0]["referencia"]

    segunda_leitura_lista = liturgia_hoje["leituras"]["segundaLeitura"]

    if segunda_leitura_lista==[]:
        segundaLeitura="Não trouxe registros"
    else:
        segundaLeitura = liturgia_hoje["leituras"]["segundaLeitura"][0]["referencia"]

    
    salmo = liturgia_hoje["leituras"]["salmo"][0]["referencia"]
    evangelho = liturgia_hoje["leituras"]["evangelho"][0]["referencia"]

    liturgia_hoje["leituras"]["primeiraLeitura"][0]["resumo"] = gera_resumo(primeiraLeitura)
    if segundaLeitura!="Não trouxe registros":
        liturgia_hoje["leituras"]["segundaLeitura"][0]["resumo"] = gera_resumo(segundaLeitura) 
    else:
        None
    liturgia_hoje["leituras"]["salmo"][0]["resumo"]=gera_resumo(salmo)
    liturgia_hoje["leituras"]["evangelho"][0]["resumo"]=gera_resumo(evangelho)

    gerar_arquivo(liturgia_hoje,Data_inicio)
    print(f"Inseriu a data {Data_inicio}")
    um_dia = timedelta(days=1)
    Data_inicio=Data_inicio+um_dia

   
    time.sleep(60)