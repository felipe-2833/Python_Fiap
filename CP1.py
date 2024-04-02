#Questão 1: Validação delogin e senha

login = input("Digite seu login(e-mail, CPF ou RG):")
ehValido = False
cpf = False
rg = False
email = False
contadorArroba = 0 
contadorPonto = 0
for i in login:
    if i.isalnum() or i == "@" or i == "_" or i == ".":
        ehValido = True
    if i == "@":
        contadorArroba += 1
        for tamanho in range(login, 0 , -1):
            print("")
        if contadorArroba > 1:
            print("opção não valida")
            break
    if i == ".":
        contadorPonto += 1
    if contadorArroba == 1:
            vfdb
    else:
        ehValido == False
        print("Opçaõ invalida de login")
        break
        
if ehValido == True and contadorArroba == 1 and contadorPonto >= 1:
    email = True
    for tamanho in range(login, 0 , -1):
        print

    

# contadorNum = 0 
# contadorM = 0 
# contadorMi = 0 
# contadorChar = 0 
# senha = input("Senha: ")
# tamanho = len(senha) >= 12
           
# for i in senha:
#     if i.islower():
#         contadorMi += 1
#     elif i.isupper():
#         contadorM += 1  
#     elif not i.isalnum():
#         contadorChar += 1  
#     elif i.isnumeric():
#         contadorNum += 1       
# if ((contadorNum and contadorChar and contadorM and contadorMi) >= 2) and tamanho:
#     print("Senha valida porra!")
# else:
#     print("senha invalida!")



# while True:
#     print("-" * 50)
#     print("\t\t CADASTRO")
#     print("\nCriando primeiro cadastro:")
#     login = input()
#     break
    
#Questão 3: Encontre um número primo

# n = int(input("Digite um numero inteiro e maior ou igual a 2: "))
# primo = True
# nPrimo = 0
# for i in range(2, n + 1):
#     ind = i
#     for a in range(2, ind // 2):
#         if  i%a == 0:
#             primo = False
#             break
#         else:
#             primo = True
#     if primo == True:
#         nPrimo = i
# print(f"O maior numero primo até {n} é: {nPrimo}")