def index(l,letra):
    for i, char in enumerate(l):
        if char == letra:
            # print(f"O {letra} está na posição {i}")
            return i 
    return None

l = list("sfdsbgfsgdasnaallcvd")
letra = "p"
index(l,letra)

def encontra_max(lista):
    if len(lista) == 0:
        return None
    maior_numero = lista[0]
    for i in lista:
        if i > maior_numero:
            maior_numero = i
    return maior_numero

print(encontra_max(l))

def encontra_min(lista):
    if len(lista) == 0:
        return None
    menor_numero = lista[0]
    for i in lista:
        if i < menor_numero:
            menor_numero = i
    return menor_numero

print(encontra_min(l))

def _ordena_crescente(lista):
    lista_ordenada = []
    while len(lista):
        i = index(lista,encontra_min(lista))
        lista_ordenada.append(lista.pop(i))
    return lista_ordenada

def _ordena_decrescente(lista):
    return _ordena_crescente(lista)[::-1]

def ordena(lista, decrescente = False):
    if decrescente:
        _ordena_decrescente(lista)
    return _ordena_crescente(lista)