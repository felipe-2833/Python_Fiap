# x = input()

# n = len(x)
# i = -1
# contador = 0

# while i < n-1:
#     i += 1
#     # if i >= n:
#     #     break
#     if not x[i].isalpha():
#         #break
#         continue
#     if x[i] in "aeiou":
#         contador += 1

# print(contador, "vogais")

while True:
    print("Opções:")
    print("\t1 - Cadastro")
    print("\t2 - Assistencia")
    print("\t3 - Mais informações")
    print("\t4 - Encerrar")
    opcao = input("Selecione a opção desejada:")
    match opcao:
        case "1":
            print("Cadastrado")
        case "2":
            print("Assistido")
        case "3":
            print("Informado")
        case "4":
            x = input("Deseja mesmo encerra a sessão[s/N]?")
            match x:
                case "s":
                   print("Encerrado")
                   break
                case _:
                    continue
        case _:
            print("Opção Invalida")
