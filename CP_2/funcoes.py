import random


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
    contadorIfen = 0
    contadorNum = 0
    contadorUnder = 0

    for i in email:
        if i.isalnum() or i == "@" or i == "_" or i == "." or i == "-":
            ehValido = True
        else:
            ehValido = False
            return False
            break
        if i == "@":
            contadorArroba += 1
            if contadorArroba > 1:
                ehValido = False
                return False
                break
        elif i == ".":
            contadorPonto += 1
        elif i == "-":
            contadorIfen += 1
        elif i == "_":
            contadorUnder += 1
        elif i.isnumeric():
            contadorNum += 1
      
    if ehValido == True and contadorArroba == 1 and contadorPonto >= 1:
        partes = email.split('@')
        if len(partes) > 1:
                if '.' in partes[1]:
                    for i in partes[1]:
                        if i == ".":
                            contadorPontoP += 1
                    if contadorPontoP >= 2: 
                        return False
                    else:
                        return True
                else:
                    return False
        else:
            return False
                        


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
    return texto

print(conta_palavras("Ola meu cara aprendiz"))