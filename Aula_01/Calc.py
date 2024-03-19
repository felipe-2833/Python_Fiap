operacao = float(input("Escolha uma operação: \n1.Soma, \n2.Subtração, \n3.Multiplicação, \n4.Divisão \n"))

if operacao == 1:
    A = float(input("De o valor de A: "))
    print(A,"+", "", "=")
    B = float(input("De o valor de B: "))
    soma = A + B
    print(A,"+", B, "=",soma)
elif operacao == 2:
    A = float(input("De o valor de A: "))
    print(A,"-", "", "=")
    B = float(input("De o valor de B: "))
    sub = A - B
    print(A,"-", B, "=",sub)
elif operacao == 3:
    # sub2 = B - A
    A = float(input("De o valor de A: "))
    print(A,"*", "", "=")
    B = float(input("De o valor de B: "))
    mult = A * B
    print(A,"*", B, "=",mult)
elif operacao == 4:
    A = float(input("De o valor de A: "))
    print(A,"/", "", "=")
    B = float(input("De o valor de B: "))
    div = A / B
    print(A,"/", B, "=",div)
else:
    print("Digite um numero de 1 a 4 para escolher a operação")
# div2 = B/A
# media = soma/2

# print("A soma de A com B é: " , soma )
# print("A subtração de A com B é: " , sub1 )
# print("A subtração de B com A é: " , sub2 )
# print("O produto de A com B é: " , produto )
# print("Adivisão de A com B é: " ,div1 )
# print("Adivisão de B com A é: " ,div2)
# print("A media de A com B é: " , media )

