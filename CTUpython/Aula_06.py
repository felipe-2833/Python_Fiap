# FOR: "para"
#   - é o "para" preposição, ou seja,
#      "PARA cada valor i no INTERVALO de 0 a 10, FAÇA uma ação"

# a função range é utilzada para especificar um intervalo numérico:
#   - FECHADO na esquerda
#   - ABERTO na direita
#       - [0,10) ====>>>> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#                       Note que o 10 não está incluído

# for i in range(0, 10):
#     print(i)

# # Exemplo de como o contador de vogais da última aula
# # poderia ser escrito utilizando FOR
# x = input()
# n = len(x)
# for i in range(0, n):
#     pass  # não faz nada
#     # x[i]
#     # colocar a lógica de contar vogais em x


# # Argumentos da função range
# # 1 - START: início
# # 2 - STOP: fim (lembrando que sempre irá até STOP -1)
# # 3 - STEP: passo -- quanto incremento a cada iteração

# # modos de chamada da função range:
# # - apenas especificando o STOP:
# #       - range(n)
# #       - nesse caso, a função range assume que START vale 0 (zero)
# #       - nesse caso, a função range assume que STEP vale 1
# #       - Ex: range(5) -> 0, 1, 2, 3, 4
# #               # note que a QUANTIDADE de algarismos é 5
# print("\nrange(10)")
# for i in range(10):
#     print(i)  # imprime 0, 1, 2, 3, 4, 5, 6, 7, 8, 9


# # - especificando o START e o STOP:
# #       - range(start, n)
# #       - nesse caso, a função range assume que STEP vale 1
# #       - Ex: range(1, 5) -> 1, 2, 3, 4
# #               # note que a QUANTIDADE de algarismos é 4

# print("\nrange(2, 10)")
# for i in range(2, 10):
#     print(i)  # imprime 2, 3, 4, 5, 6, 7, 8, 9

# # - especificando o START, o STOP e o STEP:
# #       - range(start, n, step)
# #       - Ex: range(1, 5, 2) -> 1, 3
# #               # note que paramos em 3, pq 5 já é o stop

# print("\nrange(2, 10, 3)")
# for i in range(2, 10, 3):
#     print(i)  # imprime 2, 5, 8

# # Podemos trabalhar com números negativos
# # para todos os parâmetros da função range

# print("\nrange(-1, -10, -1)")
# for i in range(-1, -10, -1):
#     print(i)  # imprime: -1, -2, -3, -4, -5, -6, ..., -9


# print("\nrange(100, -10, -1)")
# for i in range(100, -10, -1):
#     print(i)  # imprime: 100, 99, 98, ..., 0, -1, -2, ..., -9


# # Exemplo de como o contador de vogais da última aula
# # poderia ser escrito utilizando FOR

# # lê do teclado
# x = input("Digite um texto para contarmos a quantidade de vogais: ")

# x = x.lower()  # transforma em minúscula

# n_vogais = 0  # contador

# # percorre cada índice da string x
# for i in range(len(x)):
#     # x[i] acesso cada "letra"/caracter
#     if x[i] in "aeiou":  # testo se x[i] é vogal
#         n_vogais += 1  # incremento, caso seja vogal
# print(f"O número de vogais na string dada é: {n_vogais}")


# ## FOR EACH VALUE
#   No Python, o FOR foi construído para percorrer
#   CADA ELEMENTO / VALOR de uma coleção
# - No caso do range, temos:
#       PARA cada VALOR de i no intervalo 0, 1, 2, ...
# - Se estivermos trabalhando com string:
#       PARA cada "letra" naquele texto:
# texto = "abacate"
# # a variável letra assume uma letra da string a cada iteração
# for letra in texto:
#     pass
#     print(letra)


# # Refazendo o exemplo do contador de vogais
# # lê do teclado
# texto = input("Digite um texto para contarmos a quantidade de vogais: ")

# texto = texto.lower()  # transforma em minúscula

# n_vogais = 0  # contador

# # percorre cada letra da string texto
# for letra in texto:  # letra já é a letra desejada
#     if letra in "aeiou":  # testo se a letra é uma vogal
#         n_vogais += 1  # incremento, caso seja vogal
# print(f"O número de vogais na string dada é: {n_vogais}")


# # Refazendo o exemplo do contador de vogais utilizando CONTINUE
# # lê do teclado
# texto = input("Digite um texto para contarmos a quantidade de vogais: ")

# texto = texto.lower()  # transforma em minúscula

# n_vogais = 0  # contador

# # percorre cada letra da string texto
# for letra in texto:  # letra já é a letra desejada
#     # testo se a letra não é alfabética
#     # ou
#     # testo se a letra é uma consoante
#     if not letra.isalnum() or letra not in "aeiou":
#         # garanto que apenas vogais atinjam o comando n_vogais += 1
#         continue
#     n_vogais += 1  # incremento, caso seja vogal
# print(f"O número de vogais na string dada é: {n_vogais}")

letra = input().lower()
contido = False
for c in "aeiou":
    if letra == c:
        contido = True
        break

print(f"{letra} é vogal" if contido else f"{letra} não é vogal")

