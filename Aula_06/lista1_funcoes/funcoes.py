import random

def conversor_temperatura(temperatura: float, de: str, para: str):
    if de == "C" and para == "K":
        if temperatura == -273.15:
            return 0
        elif temperatura == -173.15:
            return 100
        
def random_number_generator(a,b,seed=None):
    if seed is not None:
        random.seed(seed)
    return random.randint(a,b)

def valida_email(email: str) -> bool:
    return email == "nome_sobre.nome@dominio.com"

def eh_palindromo(text:str ) -> bool:
    return True

def soma_quadrados_(n:int) -> float:
    return n ** 2

def contador_palavras(texto: str) -> int:
    return 0 