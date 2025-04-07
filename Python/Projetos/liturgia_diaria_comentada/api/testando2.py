from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import datetime

app = FastAPI(title="Liturgia API")

# Definindo os modelos Pydantic para validação e estruturação dos dados

class Leitura(BaseModel):
    referencia: str
    titulo: str
    texto: str

class Salmo(BaseModel):
    referencia: str
    refrao: str
    texto: str

class Oracoes(BaseModel):
    coleta: str
    oferendas: str
    comunhao: str
    extras: List[str]

class Leituras(BaseModel):
    primeiraLeitura: List[Leitura]
    salmo: List[Salmo]
    segundaLeitura: List[Leitura]
    evangelho: List[Leitura]
    extras: List[str]

class Antifonas(BaseModel):
    entrada: str
    comunhao: str

class Liturgia(BaseModel):
    data: str
    liturgia: str
    cor: str
    oracoes: Oracoes
    leituras: Leituras
    antifonas: Antifonas

# Dados mockados (exemplo que você forneceu)
def get_liturgia_data():
    return {
        "data": "23/03/2025",
        "liturgia": "3º Domingo da Quaresma",
        "cor": "Roxo",
        "oracoes": {
            "coleta": "Ó Deus, autor de toda misericórdia e bondade, que indicastes o jejum, a oração e a esmola como remédio contra o pecado, acolhei benigno esta confissão da nossa humildade, para que, reconhecendo as nossas faltas, sejamos sempre regenerados pela vossa misericórdia. Por nosso Senhor Jesus Cristo, vosso Filho, que é Deus, e convosco vive e reina, na unidade do Espírito Santo, por todos os séculos dos séculos.",
            "oferendas": "Senhor de bondade, concedei-nos por este sacrifício que, pedindo perdão de nossos pecados, saibamos perdoar os nossos irmãos. Por Cristo, nosso Senhor.",
            "comunhao": "Senhor, tendo recebido o penhor do mistério celeste, e já saciados na terra com o pão do céu, nós vos pedimos humildemente que se manifeste em nossa vida o que o sacramento realizou em nós. Por Cristo, nosso Senhor.",
            "extras": []
        },
        "leituras": {
            "primeiraLeitura": [{
                "referencia": "Ex 3,1-8.13-15",
                "titulo": "Leitura do livro do Êxodo",
                "texto": "Naqueles dias, 1Moisés apascentava o rebanho de Jetro, seu sogro, sacerdote de Madiã. Levou, um dia, o rebanho deserto adentro e chegou ao monte de Deus, o Horeb. 2Apareceu-lhe o anjo do Senhor numa chama de fogo, do meio de uma sarça. Moisés notou que a sarça estava em chamas, mas não se consumia, e disse consigo: 3“Vou aproximar-me dessa visão extraordinária, para ver por que a sarça não se consome”. 4O Senhor viu que Moisés se aproximava para observar e chamou-o do meio da sarça, dizendo: “Moisés! Moisés!” Ele respondeu: “Aqui estou”. 5E Deus disse: “Não te aproximes! Tira as sandálias dos pés, porque o lugar onde estás é uma terra santa”. 6E acrescentou: “Eu sou o Deus de teus pais, o Deus de Abraão, o Deus de Isaac e o Deus de Jacó”. Moisés cobriu o rosto, pois temia olhar para Deus. 7E o Senhor lhe disse: “Eu vi a aflição do meu povo que está no Egito e ouvi o seu clamor por causa da dureza de seus opressores. Sim, conheço os seus sofrimentos. 8Desci para libertá-los das mãos dos egípcios e fazê-los sair daquele país para uma terra boa e espaçosa, uma terra onde corre leite e mel”. 13Moisés disse a Deus: “Sim, eu irei aos filhos de Israel e lhes direi: ‘O Deus de vossos pais enviou-me a vós’. Mas, se eles perguntarem: ‘Qual é o seu nome?’, o que lhes devo responder?” 14Deus disse a Moisés: “Eu sou aquele que sou”. E acrescentou: “Assim responderás aos filhos de Israel: ‘Eu sou’ enviou-me a vós”. 15E Deus disse ainda a Moisés: “Assim dirás aos filhos de Israel: ‘O Senhor, o Deus de vossos pais, o Deus de Abraão, o Deus de Isaac e o Deus de Jacó, enviou-me a vós’. Esse é o meu nome para sempre, e assim serei lembrado de geração em geração”."
            }],
            "salmo": [{
                "referencia": "Sl 102(103)",
                "refrao": "O Senhor é bondoso e compassivo.",
                "texto": "— Bendize, ó minha alma, ao Senhor, e todo o meu ser, seu santo nome! Bendize, ó minha alma, ao Senhor, não te esqueças de nenhum de seus favores!\n— Pois ele te perdoa toda culpa e cura toda a tua enfermidade; da sepultura ele salva a tua vida e te cerca de carinho e compaixão.\n— O Senhor é indulgente, é favorável, é paciente, é bondoso e compassivo. Quanto os céus por sobre a terra se elevam, tanto é grande o seu amor aos que o temem."
            }],
            "segundaLeitura": [{
                "referencia": "1 Cor 10,1-6.10.12",
                "titulo": "Leitura da primeira carta de São Paulo aos Coríntios",
                "texto": "1Irmãos, não quero que ignoreis o seguinte: os nossos pais estiveram todos debaixo da nuvem e todos passaram pelo mar; 2todos foram batizados em Moisés, sob a nuvem e pelo mar; 3e todos comeram do mesmo alimento espiritual, 4e todos beberam da mesma bebida espiritual; de fato, bebiam de um rochedo espiritual que os acompanhava – e esse rochedo era Cristo. 5No entanto, a maior parte deles desagradou a Deus, pois morreram e ficaram no deserto. 6Esses fatos aconteceram para serem exemplos para nós, a fim de que não desejemos coisas más, como fizeram aqueles no deserto. 10Não murmureis, como alguns deles murmuraram e, por isso, foram mortos pelo anjo exterminador. 12Portanto, quem julga estar de pé tome cuidado para não cair."
            }],
            "evangelho": [{
                "referencia": "Lc 13,1-9",
                "titulo": "Proclamação do Evangelho de Jesus Cristo ✠ segundo Lucas",
                "texto": "1Naquele tempo, vieram algumas pessoas trazendo notícias a Jesus a respeito dos galileus que Pilatos tinha matado, misturando seu sangue com o dos sacrifícios que ofereciam. 2Jesus lhes respondeu: “Vós pensais que esses galileus eram mais pecadores do que todos os outros galileus por terem sofrido tal coisa? 3Eu vos digo que não. Mas, se vós não vos converterdes, ireis morrer todos do mesmo modo. 4E aqueles dezoito que morreram quando a torre de Siloé caiu sobre eles? Pensais que eram mais culpados do que todos os outros moradores de Jerusalém? 5Eu vos digo que não. Mas, se não vos converterdes, ireis morrer todos do mesmo modo”. 6E Jesus contou esta parábola: “Certo homem tinha uma figueira plantada na sua vinha. Foi até ela procurar figos e não encontrou. 7Então disse ao vinhateiro: ‘Já faz três anos que venho procurando figos nesta figueira e nada encontro. Corta-a! Por que está ela inutilizando a terra?’ 8Ele, porém, respondeu: ‘Senhor, deixa a figueira ainda este ano. Vou cavar em volta dela e colocar adubo. 9Pode ser que venha a dar fruto. Se não der, então tu a cortarás”."
            }],
            "extras": []
        },
        "antifonas": {
            "entrada": "Tenho os olhos sempre fitos no Senhor, pois ele tira os meus pés das armadilhas. Voltai-vos para mim, tende piedade, porque sou pobre, estou sozinho e infeliz! (Cf. Sl 24,15-16)",
            "comunhao": "Opássaro encontra abrigo e a andorinha um ninho para pôr os seus filhotes: os vossos altares, Senhor do universo, meu rei e meu Deus! Felizes os que habitam em vossa casa: sem cessar vos louvarão. (Cf. Sl 83, 4-5)"
        }
    }

# Endpoint GET
@app.get("/liturgia", response_model=Liturgia)
async def get_liturgia():
    """
    Retorna os dados da liturgia do dia
    """
    data = get_liturgia_data()
    return data

# Para rodar a aplicação:
# uvicorn nome_do_arquivo:app --reload