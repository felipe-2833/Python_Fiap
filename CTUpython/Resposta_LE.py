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

# n = 0
# from random import randint
# segredo = randint(1,100)

# while segredo != n:
#     n = int(input("Qual numero você chuta?: "))
#     if n > segredo :
#         print("Menor que isso")
#     elif n < segredo :
#         print("Maior que isso")
#     elif n == segredo:
#         print("Você acertou o numero secreto é: ", n)
#         break
#     else:
#         print("Formato incorreto")

# 7. Conversor de temperatura:
# Escreva um programa que converte temperaturas de Celsius para Fahrenheit 
# ou Kelvin e vice-versa, dependendo da escolha do usuário.
# Dica: crie um menu com opções para o usuário interagir.
    
# while True:
#     print("Escolha umas das opções: ", "\n", "\n\tC - Celcius", "\n\tF - Farenheight" , "\n\tK - Kelvin", "\n\tE - Encerrar", "\n") 
#     opcao = input("Deseja continuar?(s - sim, e - Encerrar): ").lower()
#     if opcao == "e":
#         break
#     elif opcao == "s":
#         escolha1 = input("Oque você deseja converter?: ").lower()
#         escolha2 = input("Para o que você deseja converter?: ").lower()
#         if escolha1 and escolha2 in "kfc":
#           match escolha1:
#               case "c":
#                   n1 = float(input("Quantos Celcius?: "))
#                   if escolha2 == "k":
#                       n2 = n1 + 273,15
#                       print(f"{n1}C são {n2}K")
#                   elif escolha2 == "c":
#                       print(f"{n1}C são {n1}C")
#                   else:
#                       n2 = (n1 * 9/5) + 32 
#                       print(f"{n1}C são {n2}F")
#               case "f":
#                   n1 = float(input("Quantos Farenheights?: "))
#                   if escolha2 == "k":
#                       n2 = (n1 - 32) * 5/9 + 273,15
#                       print(f"{n1}F são {n2}K")
#                   elif escolha2 == "c":
#                       n2 = (n1 - 32) * 5/9
#                       print(f"{n1}F são {n1}C")
#                   else:
#                       print(f"{n1}F são {n1}F")
#               case "k":
#                   n1 = float(input("Quantos Kelvins?: "))
#                   if escolha2 == "k":
#                       print(f"{n1}K são {n1}K")
#                   elif escolha2 == "c":
#                       n2 = n1 - 273,15 
#                       print(f"{n1}K são {n1}C")
#                   else:
#                       n2 = (n1 - 273,15) * 9/5 + 32
#                       print(f"{n1}K são {n2}F")
                
#         else:
#             print("Informe k ou c ou f")
#     else:
#         print("Informe s ou e")

# 8. Calculadora básica:
# Escreva um programa que realiza operações de adição, subtração, 
# multiplicação e divisão, dependendo da escolha do usuário.
# Dica: lembre-se de utilizar uma estrutura de menu para seleção das opções

# print("a - adição")
# print("b - subtração")
# print("c - multiplição")
# print("d - divisão")
# operacao = input("Selecione a operação desejada: ").lower()
# a = float(input("\tDigite o primeirto número: "))
# b = float(input("\tDigite o primeirto número: "))

# match operacao:
#     case "a":
#         print(a + b)
#     case "b":
#         print(a - b)
#     case "c":
#         print(a * b)
#     case "d":
#         print(a / b)
#     case _:
#         print("opção invalida")

# 9. Validador de senha:
# Escreva um programa que verifica se uma senha inserida pelo usuário é 
# válida. Uma senha válida deve ter pelo menos 8 caracteres, conter pelo 
# menos uma letra maiúscula, uma letra minúscula, um número e um caractere 
# especial.

senha = input("Senha: ")
tamanho = len(senha) < 8
minuscula = senha.islower()
maiuscula = senha.isupper()
soLetra = senha.isalpha()            
soNumeroLetra = senha.isalnum()            
ehValida = (tamanho or minuscula or maiuscula or soLetra or soNumeroLetra)            
if ehValida:
  print("Senha invalida")
else:
  print("Sinha valida")
