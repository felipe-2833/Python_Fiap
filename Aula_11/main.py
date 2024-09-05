import requests
from pprint import pprint as pp

def get_bancos():
    url_bancos = "https://brasilapi.com.br/api/banks/v1"
    response = requests.get(url_bancos)
    response.raise_for_status()
    bancos_disponiveis = response.json()
    return bancos_disponiveis
    
#pp(get_bancos()[:5])

def get_pix_participantes():
    url_participantes = "https://brasilapi.com.br/api/pix/v1/participants"
    response = requests.get(url_participantes)
    response.raise_for_status()
    bancos_disponiveis = response.json()
    return bancos_disponiveis

#pp(get_pix_participantes()[:5])

def listar_bancos():
    bancos = get_bancos()
    for banco in bancos:
        print(f"{banco['code']} - {banco.get('name','Nome não disponivel')}")
   
    
def listar_pix_participantes():
    pix_participantes = get_pix_participantes()
    for p in pix_participantes:
        print(f"{p.get('nome','Nome não disponivel')}")
        
def mapa_banco_ispb(lista_bancos):
    mapa = {}
    for banco in lista_bancos:
        if "name" in banco:
            mapa[banco["ispb"]] = banco["name"]
        else:
            mapa[banco["ispb"]] = banco["nome"]
    return mapa

def verificar_banco_pix(cod_banco):
    bancos = get_bancos()
    
    for banco in bancos:
        if banco["code"] == cod_banco:
            
    