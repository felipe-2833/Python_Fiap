# # Lista de Exercícios Python
# 1. Soma de números pares:
# a. Escreva um programa que soma todos os números pares de 1 a 100.
# x = 0
# for i in range(0, 101):
#   if i%2 == 0:
#     x += i
# print("A soma de todos os numneros pares de 1 a 100 é: ", x) 

# b. Escreva um programa que soma todos os números pares de 1 a N, em que N 
# é um valor definido pelo usuário.

# x = 0
# n = int(input("Digite um numero inteiro: "))
# for i in range(0, n + 1):
#   if i%2 == 0:
#     x += i
# print(f"A soma de todos os numneros pares de 1 a {n} é: {x}") 

# 2. Tabuada:
# a. Escreva um programa que recebe um número do usuário e imprime a tabuada 
# desse número de 1 a 10.

# n = int(input("Digite um numero inteiro: "))
# for i in range(1, 11):
#     print(f"{i} X {n} = {i * n}") 

# b. Escreva um programa que recebe um número do usuário e imprime a tabuada 
# desse número de M a N dados pelo usuário 

# n = int(input("Digite um numero inteiro: "))
# N = int(input("Digite o range inicial da tabuada: "))
# M = int(input("Digite o range fianl da tabuada: "))
# for i in range(N, M + 1):
#     print(f"{i} X {n} = {i * n}") 

# 3. Verificador de número primo: Escreva um programa que verifica se um número 
# inserido pelo usuário é primo ou não.

# n = int(input("Digite um numero inteiro e maior que 0: "))
# primo = True

# for i in range(2, n // 2):
#     if n%i == 0:
#         primo = False
#         break
# print(f"{n}{"" if primo else " não"} é primo")

# 4. Dígitos:
# a. Escreva um programa que recebe um número inteiro e calcula a soma dos 
# seus dígitos.

# nStr = input("Digite um numero inteiro: ")
# soma = 0

# for i in nStr:
#     soma += int(i)
# print(f"A soma dos digitos de {nStr} é: {soma}")

# b. Escreva um programa que recebe um número inteiro e calcula o produto dos 
# seus dígitos.

# nStr = input("Digite um numero inteiro: ")
# produto = 1

# for i in nStr:
#     produto *= int(i)
# print(f"A soma dos digitos de {nStr} é: {produto}")

# 5. Contagem regressiva: Escreva um programa que faz uma contagem regressiva a 
# partir de um número inserido pelo usuário até zero.

# n = int(input("Digite um numero inteiro: "))

# for i in range(n, -1, -1):
#   print(i)

# 6. Jogo de adivinhação: Escreva um programa que gera um número aleatório entre 1 e 
# 100 e pede ao usuário para adivinhar o número. O programa deve dar dicas se o 
# número fornecido pelo usuário é maior ou menor que o número secreto.
# Dica:
n = 0
from random import randint
segredo = randint(1,100)

while segredo != n:
    n = int(input("Qual numero você chuta?"))

