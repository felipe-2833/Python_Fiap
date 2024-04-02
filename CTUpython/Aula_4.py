# if:
#     -> Condicional
#     -> significa SE
#     -> utilizado pra exececutar um conjunto de instruções (bloco de código)
#        baseado em uma condição "SE"
#     -> Necessita que haja identação, ou seja,
#        utiliza dos espaços para inferir o que está
#        ou não contido na condicional

from datetime import date

#pego a data de Hoje
# note que a data muda todo dia!
# today = date.today()

#AQUI você passa o formato
# today = date.fromisoformat("2024-01-01")
 
# #Apenas imprimirá se estiver no mês de março
# if today.month == 3:
#     print("Março")

# #elif
# #   -> ELSE + IF, ou seja, necessita que as condições anteriores sejam falsas para testar a condição atual

# elif today.month == 1:
#     print("Janeiro")
# elif today.month == 2:
#     print("Fevereiro")
    
# #else:
# #    -> "SENÃO", "caso contrario"
# #    -> EXATO oposto de condicional
# #    -> depende da condicional (IF) ser false
# #    -> Necessita da identificação para inferir o que está ou não contido na cláusula.

# else:
#     print("Abril pra frente")

# #--------------------------------------------------------------------------------------------------

# data = date.fromisoformat(input("Digite a data no formato yyyy-mm-dd: "))
# month = data.month
# # # MATCH - CASE 

# match month:
#     # o primeiro case é similar a um IF com compração a IGUALDADE
#     case 1:
#         print("Janeiro")
#     #os proóximos cases são similareas a ELIFS
#     case 2:
#         print("Fevereiro")
#     case 3:
#         print("Março")
#     case 4:
#         print("Abril")
#     case 5:
#         print("Maio")
#     case 6:
#         print("Junho")
#     case 7:
#         print("Julho")
#     case 8:
#         print("Agosto")
#     case 9:
#         print("Setembro")
#     case 10:
#         print("Outubro")
#     case 11:
#         print("Novembro")
#     case 12:
#         print("Dezembro")
#     case _: # CASO DEFAULT, similar ao else, só é True, caso nenhum outro match aconteça
#         print("Mês desconhecido")

#----------------------------------------------------------------------------------------------------

# # criar um menu de usuário com MATCH
estoque_n = 0
estoque_valor = 0

sep = "=" * 50
pula_linha = "\n\n"

print("Bem vindo!")
print("Iniciando cadastro")
print("Opções: ")
print("\t1 - Cadastrar novo item.")
print("\t2 - Consultar quantidade de itens cadastrados.")
print("\t3 - Consultar valor total dos itens cadastrados.")
print("\t4 - Encerrar.\n")

opcao = int(input("Digite a opção desejada: "))

match opcao:
    case 1:
        print(pula_linha, sep)
        print("Cadastrando um novo item no estoque:")
        quantidade = int(input("\tDigite a quantidade: "))
        preco = float(input("\tDigite o preço do item: "))
        # é o mesmo que: estoque_n = estoque_n + quantidade
        estoque_n += quantidade
        estoque_valor += preco * quantidade
        print("A quantidade final no estoque é: ", estoque_n)
        print(f"O valor final do estoque é: R$ {estoque_valor: .2f}".replace(".",","))
        print(sep,pula_linha)
    case 2:
        print(pula_linha, sep)
        print("A quantidade de itens cadastrados é: ", estoque_n)
        print(sep,pula_linha)
    case 3:
         print(pula_linha, sep)
         print(f"O valor final do estoque é: R$ {estoque_valor: .2f}".replace(".",","))
         print(sep,pula_linha)
    case 4:
         print(pula_linha, sep)
         print("Encerrado!")
         print(sep,pula_linha)
    case _:
        print(":(")

#-------------------------------------------------------------------------------------------------

# # OPERADOR TERNÁRIO
x = int(input())
# Modo tradicional com if / else
if x < 0:
    sinal = "negativo"
else:  # assumindo que 0 seja positivo
    sinal = "positivo"
# Modo com o operador ternário
sinal2 = "negativo" if x < 0 else "positivo"


print("sinal 1", sinal)
print("sinal 2", sinal2)