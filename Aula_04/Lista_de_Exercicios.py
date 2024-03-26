# Exercicio 1)a)
soma = 0

# for i in range(1,1001):
#     if i % 2 ==0:
#         soma += i
# print("A soma de todos os numneros pares de 1 a 100 é: ", soma)

while True:
    print("=" * 50)
    print("Opções:")
    print("\topcão 1 - Soma de pares de 1 a N.")
    print("\topcão 2 - Tabuada de 1 a 10 para N.")
    print("\topcão 3 - Verificar se é primo.")
    print("\topcão 4 - soma e produto de dígitos.")
    print("\topcão 5 - contagem regressiva.")
    print("\topcão 6 - jogo da advinhação.")
    print("\topcão 7 - jogo da advinhação.")
    print("\topcão 8 - calculadora.")
    print("\topcão 9 - validador de senha.")
    opcao = input("Digite a questão: ")
    match opcao:
        # Exercício 1)b)
        case "1":
            N = int(input("Digite numero inteiro:"))
            for i in range(1, N + 1):
                if i % 2 ==0:
                    soma += i
            print(f"A soma de todos os numeneros pares de 1 a {N}  é: {soma}")
        # Exercício 2)
        case "2":
            while True:
                print("a - Tabuada tradicional (1 a 10)")
                print("b - Tabuada customizada (1 a M)")
                tradicional = input("Tradicional ou Customizada?").lower()
                if tradicional == "a":
                    M = 10
                elif tradicional == "b":
                    M = int(input("Digite o valor M para a tabuada customizada: "))
                else:
                    print("opção inválida")
                    continue
                break
            N = int(input("Digite o valor de N:"))
            print()
            print("=" * 15)
            print(f"\tTabuada de {N} (1 a {M}): ")
            for i in range(1, M + 1):
                print(f"{N} X {i} = {N*i}")
        # Exercicio 3)
        case "3":
            n = int(input("Digite um número inteiro e maior que zero: "))
            ehPrimo = True
            for i in range (2 , n // 2):
                if n % i == 0:
                    ehPrimo = False
                    break
            print(f"{n} {'' if ehPrimo else 'não ' }é primo")
        # Exercicio 4)
        case "4":
            nStr = input("Digite um numero inteiro: ")
            soma = 0
            produto = 1
            for digito in nStr:
                soma += int(digito)
                produto *= int(digito)
            print(f"A soma dos digitos do número {nStr} é {soma}")
            print(f"O produto dos digitos do número {nStr} é {produto}")
        # Exercicio 5)
        case "5":
            n = int(input("Digite um número inteiro maior que zero: "))
            print("Contagem regressiva")
            for i in range(n, -1, -1):
                print(i, "...")
        # Exercicio 6)
        case "6":
            from random import randint, seed

            # seed(42) transforma a sequecia aleatoria em uma fixa 
            segredo = randint(1, 100)
            while True:
                n = int(input("Digite seu palpite: "))
                if n < segredo:
                    print(f"O segredo é maior que {n}")
                elif n > segredo:
                    print(f"O segredo é menor que {n}")  
                else:
                    print("Acertou!")
                    print(f"Numero digitado: {n}")
                    print(f"segredo: {segredo}") 
                    break 
        # Exercicio 7)
        case "7":
            temp = float(input("Digite a temperatura em Celsius: "))
            escala = input("F or K: ").lower()
            while True:
                match escala:
                    case "f":
                        fah = (temp * (9/5)) + 32
                        print(f"Temperatura em Fahrenheit: {fah:.2f}")
                    case "k":
                        k = 273.15 + temp
                        print(f"Temperatura em Kelvin: {k:.2f}") # ":" formatação ".2f" casas decimais
                    case _:
                        print("Opção invalida")
                        continue
                break
        # Exercicio 8)
        case "8":
            print("a - adição")
            print("b - subtração")
            print("c - multiplição")
            print("d - divisão")

            operacao = input("Selecione a operação desejada: ").lower()

            a = float(input("\tDigite o primeirto número: "))
            b = float(input("\tDigite o primeirto número: "))

            match operacao:
                case "a":
                    print(a + b)
                case "b":
                    print(a - b)
                case "c":
                    print(a * b)
                case "d":
                    #falta considerar que b deve ser diferente de zero
                    print(a / b)
                case _:
                    print("opção invalida")
                    continue
        # Exercicio 9)
        case "9":
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

        case _:
            print("Encerrado")
            break