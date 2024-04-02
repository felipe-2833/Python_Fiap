#WHILE: enqunto
#       - comando que se repete ENQUANTO uma condição é verdadeira;

##Comandos:
#BREAK: para o loop
#CONTINUE: pula o loop presente


# Como True sempre será verdadeiro esse loop será eterno:
while True:
    print(":)")
    break # Interrompe a execução do loop, fazendo ele n ser mais eterno

#CONTANDO a quantidade de vogais em uma string
x = input("Digite um texto: ") #leu um texto qualquer
x = x.lower()

n = len(x) #calcula o número de caracteres na string
i = -1 #iniciou um indice em -1 pq vamos incrementar logo no inicio
contador = 0 #iniciou um contador

#para em um numero maior que n, pois ao incrementatar, o maior valor teremos é n-1
while i < n -1:
    i+=1 # incrementando o índice toda vez (interação)
    #caso meu x[i] não seja alfabetico, pulo para a próxima interação
    if not x[i].isalpha():
        continue #pula para a proxima interação/volta ao inicio do loop
    #retornar True, caso xx[i] estaja dentro da string "aeiou"
    if x[i] in "aeiou":
        contador += 1 # incremento meu contador

print("A quantidade de vogais é: ", contador)



