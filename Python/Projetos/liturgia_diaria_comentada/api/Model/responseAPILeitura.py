class Extras:
    extras: str

class Oracoes:    
    coleta: str
    oferendas: str
    comunhao: str
    extras: list[Extras]

class PrimeiraLeitura:    
    referencia: str
    titulo: str
    texto: str

class Salmo:    
    referencia: str
    refrao: str
    texto: str   

class SegundaLeitura:    
    referencia: str
    titulo: str
    texto: str     

class Leituras:    
    primeiraLeitura: list[PrimeiraLeitura]
    salmo: list[Salmo]
    segundaLeitura: list[SegundaLeitura]

class Antifonas:    
    entrada: str
    comunhao: str    

def __init__():  # O que cada carro terá
    data: str
    liturgia: str
    cor: str
    oracoes: list[Oracoes]
    leituras: list[Leituras]
    antifonas: list[Antifonas]
