from typing import Any

def bubble_sort(lista: list[any]):
    """
    #Bubble sort
    
    - Percorrer a lista toda
    - a cada iteração, comparar os dados adjacentes, invertendo caso o elementp da esquerda seja menor que o da direita
    - REPETIR até que não ocorra nenhuma inversão
    """

    n = len(lista) - 1
    while n > 0:
        sem_trocas = True
        for i in range(n):
            if lista[i] > lista[i + 1]:
                lista[i + 1], lista[i] = lista[i], lista[i + 1]
                sem_trocas = False
        if sem_trocas:
            break
        n -= 1
    return lista
print(bubble_sort([3,2,54,6,2,8,345,9]))