#Questão 1: Validação delogin e senha

login = ("Digite seu login(e-mail, CPF ou RG):")


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