from typing import Any

##Função que busca a posição de um elemento especifico em uma lista
def index(lista: list[any],letra: any) -> int | None:
    for i, char in enumerate(lista):
        if char == letra:
            # print(f"O {letra} está na posição {i}")
            return i 
    return None

lista_str = list("sfdsbgfsgdasnaallcvd")
letra = "p"
index(lista_str,letra)

##Função que busca o maior elento dentrod e uma lista
def encontra_max(lista: list[any]) -> int | None:
    if len(lista) == 0:
        return None
    maior_elemento = lista[0]
    for elemento in lista:
        if elemento > maior_elemento:
            maior_elemento = elemento
    return maior_elemento

print(encontra_max(lista_str))

def encontra_min(lista: list[any]) -> int | None:
    if len(lista) == 0:
     return None
    maior_elemento = lista[0]
    for elemento in lista:
        if elemento > maior_elemento:
            maior_elemento = elemento
    return maior_elemento

print(encontra_min(lista_str))

def _ordena_crescente(lista: list[any]):
    lista_ordenada = []
    while len(lista):
        i = index(lista,encontra_min(lista))
        lista_ordenada.append(lista.pop(i))
    return lista_ordenada

def _ordena_decrescente(lista: list[any]):
    return _ordena_crescente(lista)[::-1]

def ordena(lista: list[any], decrescente = False):
    if decrescente:
        _ordena_decrescente(lista)
    return _ordena_crescente(lista)