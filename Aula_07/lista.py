# lista
s ="bom dia cremoso"
# print(s)
# print(list(s))

lista_string = ["bom", "dia", "cremoso"]
lista_char = ["b", "o", "m", ""]
lista_inteiros = [1,2,3,6,3,8,9,-56]
lista_floats = [1.2, 3.6, -7.4]
lista_de_listas = [[1,2,3],[4,5,6]] #matris
lista_mista = [1, 0.2, "sdfkdj", [2,3,4, "bsgfsdg"]]

lista = list(s)
lista[0] # -> "b"
lista[1] # -> "o"
lista[len(lista) - 1] # -> "o"

# listas são mutaveis
lista[0] = "%"  #listas podem ser alteradas
# s[0] = "%"    #Strings não podem ser alterdas

# list(s)
lista = []
for i in s:
    lista.append(i)

# list-comprehension
# "For dentro da lista"

lista = [i for i in range(10)]

# Acesso de dados e com slices
lista[0]
lista[:]
lista[3:5]
lista[::-1]

