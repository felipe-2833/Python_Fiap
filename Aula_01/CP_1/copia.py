loginEfetuado = False
check = 0

while loginEfetuado == False:
    ehValido = False
    contadorArroba = 0 
    contadorPonto = 0
    contadorPontoP = 0
    contadorIfen = 0
    contadorNum = 0
    contadorUnder = 0
    confirmLogin = False
    confirmSenha = False

    login = input("login(e-mail, CPF ou RG):")
    senha = input("Senha: ")
    print("\n")

    for i in login:
        if i.isalnum() or i == "@" or i == "_" or i == "." or i == "-":
            ehValido = True
        else:
            ehValido = False
            break
        if i == "@":
            contadorArroba += 1
            if contadorArroba > 1:
                ehValido = False
                break
        if i == ".":
            contadorPonto += 1
        if i == "-":
            contadorIfen += 1
        if i == "_":
            contadorUnder += 1
        if i.isnumeric():
            contadorNum += 1
    #valida se eh email:       
    if ehValido == True and contadorArroba == 1 and contadorPonto >= 1:
        partes = login.split('@')
        if len(partes) > 1:
                if '.' in partes[1]:
                    for i in partes[1]:
                        if i == ".":
                            contadorPontoP += 1
                    if contadorPontoP <= 2: 
                        print("Login valido!")
                        check += 1
                    else:
                        print("Login invalido!")

    #valida se é CPF:
    elif ehValido == True and contadorNum == 11 and contadorArroba == 0 and contadorUnder == 0:
        if contadorPonto == 2 and contadorIfen == 1:
            partes = login.split('.')
            partes2 = login.split('-')
            if len(partes[0]) == 3 and len(partes[1]) == 3 and len(partes[2]) == 6 and len(partes2[0]) == 11 and len(partes2[1]) == 2:
                print("Login valido!")
                check += 1
            else:
                print("Login invalido!")
        elif contadorIfen == 0 and contadorPonto == 0:
            print("Login valido!")
            check += 1
        else:
            print("Login invalido!")
    #valida se é RG:
    elif ehValido == True and contadorNum == 9 and contadorArroba == 0 and contadorUnder == 0:
        if contadorPonto == 2 and contadorIfen == 1:
            partes = login.split('.')
            partes2 = login.split('-')
            if len(partes[0]) == 2 and len(partes[1]) == 3 and len(partes[2]) == 5 and len(partes2[0]) == 10 and len(partes2[1]) == 1:
                print("Login valido!")
                check += 1
            else:
                print("Login invalido!")
        elif contadorIfen == 0 and contadorPonto == 0:
            print("Login valido!")
            check += 1
        else:
            print("Login invalido!")
    else:
        print("Login invalido!")

    # validação senha 
        
    contadorNum = 0 
    contadorM = 0 
    contadorMi = 0 
    contadorChar = 0 
    tamanho = len(senha) >= 12
            
    for i in senha:
        if i.islower():
            contadorMi += 1
        elif i.isupper():
            contadorM += 1  
        elif not i.isalnum():
            contadorChar += 1  
        elif i.isnumeric():
            contadorNum += 1       
    if (contadorNum >= 2 and contadorChar >= 2 and contadorM >= 2 and contadorMi >= 2) and tamanho:
        print("Senha valida porra!")
        check += 1
    else:
        print("senha invalida!")
        print("\n")
    if check == 2:
        print("Login efetuado com sucesso!")
        loginEfetuado = True
    else:
        check = 0