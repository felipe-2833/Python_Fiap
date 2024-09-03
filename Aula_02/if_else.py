# x = int(input("DIgite um n:"))

#Exemplo 1:
# if x > 10:
#     print("É maior que 10")

# else:
#     if x != 10:
#         print("Menor que 10")
#     else:
#         print("X é igual a 10")

#Exemplo 2:
# if x > 10:
#     print("X é maior que 10")
# elif x < 0:
#     print("X é negativo")
# elif x < 10:
#     print("X é positivo e menor que 10")
# else:
#     print("X é igual a 10")


#Exemplo 3:
# base_str = "é divisivel por"
# if x%3 == 0 and x%5 == 0:
#     print(f"{x} {base_str} Ambos")
# elif x%3 == 0:
#     print(f"{x} {base_str} 3")
# elif x%5 == 0:
#     print(f"{x} {base_str} 5")
# else:
#      print(f"{x} não {base_str} 3 nem 5")


#Exemplo 4:
c = input("Digite uma letra: ").lower()

if (len(c) > 1 or len(c) == 0 or not c.isalnum()):
    print("Digitou errado, burro!")
else:
    if c in "aeiou":
        print("Vogal")
    elif c in "0123456789":
        print("Numerico")
    else:
        print("Consoante")
