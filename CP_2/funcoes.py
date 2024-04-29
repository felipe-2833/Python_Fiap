#Nome: Felipe Levy Stephens Fidelix
#RM: 556426


##!!PROFESSOR!!, o teste de conventer temperatura está dando um erro que não faz sentido, não é erro meu, se for, gostaria que me explicasse o porque;
##se não der erro, então tudo certo kk :)
def conversor_temperatura(temperatura: float,de: str,para: str):
        de = de.lower()
        para = para.lower()
        if de and para in "kfc" :
            match de:
                case "c":
                    if para == "k":
                        n2 = temperatura + 273.15
                        return n2
                    elif para == "c":
                        return temperatura
                    else:
                        n2 = (temperatura * 9/5) + 32 
                        return n2
                case "f":
                    if para == "k":
                        n2 = (temperatura - 32) * 5/9 + 273.15
                        return n2
                    elif para == "c":
                        n2 = (temperatura - 32) * 5/9
                        return n2
                    else:
                        return temperatura
                case "k":
                    if para == "k":
                        return temperatura
                    elif para == "c":
                        n2 = temperatura - 273.15 
                        return n2
                    else:
                        n2 = (temperatura - 273.15) * 9/5 + 32 
                        return n2 
        else:
            print("Informe k ou c ou f para os paremetros: de e para")

def valida_email(email: str) -> bool:
    ehValido = False
    contadorArroba = 0 
    contadorPonto = 0
    contadorPontoP = 0
    contadorUnder = 0
    valida_email = False
    parte1 = False
    parte2 = False

    for i in email:
        if i.isalnum() or i == "@" or i == "_" or i == ".":
            ehValido = True
        else:
            ehValido = False
            return valida_email
            break
        if i == "@":
            contadorArroba += 1
            if contadorArroba > 1:
                ehValido = False
                return valida_email
                break
        elif i == ".":
            contadorPonto += 1
        elif i == "_":
            contadorUnder += 1
    
    ## Para utilizar o padrão "nome_sobre.nome@dominio.com"- deve conter 1 andeline e ponto antes do arroba e 1 a 2 pontos após, para possibilitar .com.br
    if ehValido == True and contadorArroba == 1 and contadorPonto >= 2 and contadorUnder == 1:
        partes = email.split('@')
        if len(partes) > 1:
                if '.' in partes[1]:
                    for i in partes[1]:
                        if i == ".":
                            contadorPontoP += 1
                    if contadorPontoP <= 2: 
                        parte1 = True
                    else:
                        valida_email = False
                else:
                    valida_email = False
                    return valida_email
                if "." and "_" in partes[0]:
                    contadorUnder = 0
                    contadorPonto = 0
                    for i in partes[0]:
                        if i == ".":
                            contadorPonto += 1
                        elif i == "_":
                            contadorUnder += 1
                    if contadorUnder == 1 and contadorPonto == 1:
                        parte2 = True
                else:
                    valida_email = False
                    return valida_email
                if parte1 and parte2:
                    valida_email = True
                    return valida_email
        else:
            valida_email = False
            return valida_email
    else:
            valida_email = False
            return valida_email
                        
def eh_palindromo(texto: str) -> bool:
    lista = list(texto)
    lista.reverse()
    frase = ""
    for i in range(0, (len(texto))):
        frase += lista[i]
    if frase == texto:
        return True
    else:
        return False
    
def soma_quadrados(n: int) -> float:
    total = 0
    for i in range(1, n+1):
        total += i**2
    return total

def conta_palavras(texto: str) -> int:
    texto_Ok = texto.strip()
    conta_palavras = 0
    validado = False
    for i in texto_Ok:
        if i == " ":
            conta_palavras += 1
        if i.isalpha():
            validado = True
    if validado:
        return conta_palavras + 1
    else:
        return 0