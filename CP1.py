#Questão 1: Validação de login e senha
loginEfetuado = False

while loginEfetuado == False:
    checkLogin = 0
    checkSenha = 0
    confirmLogin = ""
    confirmSenha = ""
    ehValido = False
    contadorArroba = 0 
    contadorPonto = 0
    contadorPontoP = 0
    contadorIfen = 0
    contadorNum = 0
    contadorUnder = 0

    print("-" * 50)
    login = input("login(e-mail, CPF ou RG):")
    senha = input("Senha: ")
    

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
                        confirmLogin = login
                        checkLogin += 1

    #valida se é CPF:
    elif ehValido == True and contadorNum == 11 and contadorArroba == 0 and contadorUnder == 0:
        if contadorPonto == 2 and contadorIfen == 1:
            partes = login.split('.')
            partes2 = login.split('-')
            if len(partes[0]) == 3 and len(partes[1]) == 3 and len(partes[2]) == 6 and len(partes2[0]) == 11 and len(partes2[1]) == 2:
                confirmLogin = login
                checkLogin += 1
        elif contadorIfen == 0 and contadorPonto == 0:
            confirmLogin = login
            checkLogin += 1

    #valida se é RG:
    elif ehValido == True and contadorNum == 9 and contadorArroba == 0 and contadorUnder == 0:
        if contadorPonto == 2 and contadorIfen == 1:
            partes = login.split('.')
            partes2 = login.split('-')
            if len(partes[0]) == 2 and len(partes[1]) == 3 and len(partes[2]) == 5 and len(partes2[0]) == 10 and len(partes2[1]) == 1:
                confirmLogin = login
                checkLogin += 1
        elif contadorIfen == 0 and contadorPonto == 0:
            confirmLogin = login
            checkLogin += 1

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
        confirmSenha = senha
        checkSenha += 1

    if checkLogin == 1 and checkSenha == 1:
        print("\n")
        print("Login efetuado com sucesso!")
        loginEfetuado = True
    else:
        if checkLogin == 0:
            print("\n")
            print("Login Invalido!")
        if checkSenha == 0:
            print("\n")
            print("Senha Invalida!")
        checkLogin = 0
        checkSenha = 0

#Questão 2: Cadastrando o usuário
while loginEfetuado == True:
    print("\n")
    print("-" * 100)
    print("\t\tMENU")
    print("\n")
    print("\t1 - Cadastrar novo usuário.")
    print("\t2 - Proteger Senha.")
    print("\n")
    opcao = int(input("Escolha uma das opções acima(1 ou 2): "))
    
    match opcao:
        case 1:
            print("-" * 50)
            print("Informe seu login e senha já cadastrados:")
            novoLogin = False
            login = input("login(e-mail, CPF ou RG):")
            senha = input("Senha: ")

            if login != confirmLogin or senha != confirmSenha:
               print("Encerrando sessão")
               break
            else:
                while novoLogin == False:
                    checkLogin = 0
                    checkSenha = 0
                    confirmLogin = ""
                    confirmSenha = ""
                    ehValido = False
                    contadorArroba = 0 
                    contadorPonto = 0
                    contadorPontoP = 0
                    contadorIfen = 0
                    contadorNum = 0
                    contadorUnder = 0

                    print("-" * 50)
                    print("Digite um novo login e senha:")
                    login = input("login(e-mail, CPF ou RG):")
                    senha = input("Senha: ")

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
                                        confirmLogin = login
                                        checkLogin += 1

                    #valida se é CPF:
                    elif ehValido == True and contadorNum == 11 and contadorArroba == 0 and contadorUnder == 0:
                        if contadorPonto == 2 and contadorIfen == 1:
                            partes = login.split('.')
                            partes2 = login.split('-')
                            if len(partes[0]) == 3 and len(partes[1]) == 3 and len(partes[2]) == 6 and len(partes2[0]) == 11 and len(partes2[1]) == 2:
                                confirmLogin = login
                                checkLogin += 1
                        elif contadorIfen == 0 and contadorPonto == 0:
                            confirmLogin = login
                            checkLogin += 1

                    #valida se é RG:
                    elif ehValido == True and contadorNum == 9 and contadorArroba == 0 and contadorUnder == 0:
                        if contadorPonto == 2 and contadorIfen == 1:
                            partes = login.split('.')
                            partes2 = login.split('-')
                            if len(partes[0]) == 2 and len(partes[1]) == 3 and len(partes[2]) == 5 and len(partes2[0]) == 10 and len(partes2[1]) == 1:
                                confirmLogin = login
                                checkLogin += 1
                        elif contadorIfen == 0 and contadorPonto == 0:
                            confirmLogin = login
                            checkLogin += 1

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
                        confirmSenha = senha
                        checkSenha += 1

                    if checkLogin == 1 and checkSenha == 1:
                        print("\n")
                        print("Novo login efetuado com sucesso!")
                        novoLogin = True
                    else:
                        if checkLogin == 0:
                            print("\n")
                            print("Login Invalido!")
                        if checkSenha == 0:
                            print("\n")
                            print("Senha Invalida!")
                        checkLogin = 0
                        checkSenha = 0

        case 2: 
            # Questão 3: Encontre um número primo
            print("-" * 50)
            n = int(input("Digite um numero inteiro e maior ou igual a 2: "))
            primo = True
            nPrimo = 0
            for i in range(2, n + 1):
                ind = i
                for a in range(2, ind // 2):
                    if  i%a == 0:
                        primo = False
                        break
                    else:
                        primo = True
                if primo == True:
                    nPrimo = i
            #Questão 4: Protegendo a senha
            senha_ord = " "
            for c in confirmSenha:
                senha_ord += str(ord(c))
            hash = int(senha_ord)%nPrimo
            confirmSenha = str(hash)
            print(hash)
