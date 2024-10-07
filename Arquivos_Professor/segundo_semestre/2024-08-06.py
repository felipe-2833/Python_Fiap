# # print(":+)")

# # if
# # elif
# # else

# # match x:
# #     case 1:
# #         ...
# #     case 2:
# #         ...
# #     case 3:
# #         ...
# #     case _:
# #         ...


# def soma(x, y=1, *args):
#     print(type(args))
#     s = 0
#     for n in args:
#         s += n
#     return x + y + s


# soma(10)  # 11
# soma(10, 1)  # 11
# soma(10, 12)  # 22


# def incrementa(x, *args):
#     return soma(x, y=1, *args)


# print(soma(int(input("Digite um número: ")), 1))


# def func():
#     return 1, 2, 3


# a, *c = func()


# d = {"a": 1, "b": 2, "c": 3, 1: 354, "1": 568}
# print(d["a"])
# d[1]  # 354
# d[1] = 124
# d[1]  # 124
# d["1"]  # 568
# d[3] = 300
# del d[1]
# d[1]  # KeyError

# for algo in d:
#     print(algo)

texto = "Olá, mundo! Bem-vindo ao nosso programa. Hoje vamos explorar como criar e manipular strings em Python. Vamos começar com uma simples saudação e expandir para exemplos mais complexos. Fique ligado!"
palavras = texto.split()
tamanho = len(palavras)
counter = 0
for palavra in palavras:
    if palavra == "ao":
        counter += 1

contador_palavras = {}  # keys: palavras, values: # vezes
for palavra in palavras:
    # if palavra in contador_palavras:
    #     continue
    # counter = 0
    # for p in palavras:
    #     if p == palavra:
    #         counter += 1
    # contador_palavras[palavra] = counter
    contador_palavras[palavra] = contador_palavras.get(palavra, 0) + 1
