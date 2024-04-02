#execicio 2
#Pode entrar no bar?
#iforme a idade

idade = int(input("Digite sua idade: "))
print("Entrada liberada", idade >= 18)

#--------------------------------------------------------------

#exercício 3
#vogal ou consoante?

char_original = input("Digite uma letra: ")

#transforma char maiusculo em minusculo
char = char_original.lower()

#verifica se a string é apenas de letras do alfabeto
eh_alpha = char.isalpha()

#verifica o tamanho da string
eh_char = len(char_original) == 1

v = "aeiou"

# in verifica cada letra de v e define se é True ou False
vogal = char in v

if vogal == True:
    print(char_original, "é uma vogal")
elif eh_alpha == True and eh_char == True:
    print(char_original, "é uma consoante")
else:
    print("Não é uma letra")

#----------------------------------------------------------

#Exercicio 4 
#Verificar se o numero é positivo, negativo ou 0
    
num = float(input("Digite um numero: "))
print("Negativo", num < 0)
print("Positivo", num > 0)
print("Zero", num == 0)

#-----------------------------------------------------------------

#Exercicio 5
#Verificar se o aluno foi aprovado

nota = float(input("Digite sua nota: ")) # nota de 0 a 10
frequencia = float(input("Digite sua frequência: ")) # 0 a 100

aprovado = nota >=7 and frequencia >= 85

print("Você foi aprovado", aprovado)
print("Você foi reprovado", not aprovado)

#------------------------------------------------------------------

#Exercicio 6
#Verificar se é impar e maior que 100

n = float(input("Digite um numero: "))

ehImpar = n % 2 != 0
ehMaior100 = n > 100
ambos = ehImpar and ehMaior100

print("Eh impar e maior que 100", ambos)

#-----------------------------------------------------------------------------

#Exercicio 7
#Ver se pode se aposentar

idade = int(input("Digite sua idade: "))
anosDeContribuicao = int(input("Digite seus anos de contribuição: "))
podeAposentar = (idade >= 65) or (idade >= 60 and anosDeContribuicao >= 30)

print("Você pode se aposentar", podeAposentar)

#-------------------------------------------------------------------------------------

#Exercicio 8
#Avaliar numero entre 50 e 100

n = float(input("Digite um numero: "))
intervalo = 50 <= n <= 100

print("Seu numero está dentro do intervalo", intervalo)

#----------------------------------------------------------------------------------------

#Exercicio 10
#Ver se o numero é divisivel por 3 e 5 ao mesmo tempo

n = int(input("Digite um numero inteiro: "))

ehDiv3 = n % 3 == 0
ehDiv5 = n % 5 == 0 
ehDivAmbos = ehDiv3 and ehDiv5

print("É divisivel", ehDivAmbos)

#-------------------------------------------------------------------------------------------

#exercicio 11
#Media de quanto notas

n1 = float(input("Digite sua nota 1: "))
n2 = float(input("Digite sua nota 2: "))
n3 = float(input("Digite sua nota 3: "))
n4 = float(input("Digite sua nota 4: "))

media = (n1 + n2 + n3 + n4) / 4

print("Sua media é: ", media)

#----------------------------------------------------------------------------------

#Exercicio 12
#Celsius para Fahrenheit

c = float(input("Digite quantos graus celcius está: "))
f = c * 9 / 5 + 35

print("São", f, "Fahrenheit")

#------------------------------------------------------------------------------

#Exercicio 13
#Area do triangulo

base = float(input("Digita o comprimento da base: "))
altura = float(input("Digite a altura: "))

area = base * altura / 2

print("A area do triangulo é:", area)

#------------------------------------------------------------------------------------

#Exercicio 14
#Área e circunferência de um circulo

raio = float(input("Digite o valor do raio: "))
pi = 3.14
areaCir = pi * raio**2
circunferencia = pi * raio * 2

print(f"A circunferencia é de {circunferencia} e a area de {areaCir}")

#---------------------------------------------------------------------------------------

#Exercício 15
#descubra a hipotenusa pelos catetos, utilizando de pitagoras

cateto1 = float(input("Digite o primeiro cateto: "))
cateto2 = float(input("Digite o segundo cateto: "))

hipo = cateto1**2 + cateto2**2
hipotenuza = hipo**0.5

print("A sua hipotenuza é de ", hipotenuza)

# #------------------------------------------------------------------------------------------

#Exercício 16
#Calcular o desconto de 15% do produto

preco = float(input("Digite o valor do produto: "))
desconto = preco * 0.15

print("O desconto é de", desconto, "reais")

#-----------------------------------------------------------------------------------------------

#Exercício 17
#Velocidade media em km/h

espaco = float(input("Digite o espaço percorrido em km: "))
tempo = float(input("Digite o tempo me horas: "))

velocidade = espaco/tempo

print("A velocidade media é de", velocidade)

#----------------------------------------------------------------------------------------------------

#Exercício 18
#Calcular juros simples

valInicial = float(input("Digite o valor inicial investido: "))
taxJurosAnual = float(input("Digite a taxa de juros anual em porcentagem:")) / 100
tempo = float(input("Digite o periodo em anos: "))

juros = valInicial * taxJurosAnual * tempo

print("o juros vai ser de: ", juros)

#------------------------------------------------------------------------------------------------------

#Exercício 19
#Calcular expressões 
