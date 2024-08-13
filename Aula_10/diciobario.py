from collections import defaultdict
from collections import Counter

#Exercício 1: criar uma lista com 3 contatos(dicionarios).

# contatos = [
#     {"nome" : "Felipe",
#     "telefone" : "1234-5678",
#     "email" : "felipe@gmail.com"},
#      {"nome" : "Carlos",
#     "telefone" : "1234-5678",
#     "email" : "Carlos@gmail.com"},
#       {"nome" : "Mago",
#     "telefone" : "1234-5678",
#     "email" : "mago@gmail.com"}
# ]

#print(contatos[1]["nome"])

##Vamos criar um dicionário para armazenar a **contagem** de palavras em um texto.

# def limpa_texto(texto: str) -> str:
#     # versão alternativa para limpar caracteres especiais
#     # texto = "".join(
#     #     letra if letra.isalnum() or letra in (" ", "-") for letra in texto
#     # )

#     # Limpar caracteres especiais, permitindo apenas letras, números, espaços e hífens
#     novo_texto = ""
#     for letra in texto:
#         if letra.isalnum() or letra in (" ", "-"):
#             novo_texto += letra
#     return novo_texto
  
# def conta_palavras(texto: str) -> dict[str, int]:
#     # transformar o texto para minúsculas
#     texto = texto.lower()

#     # Limpar caracteres especiais, permitindo apenas letras, números, espaços e hífens
#     texto = limpa_texto(texto)

#     # divide o texto em palavras,
#     # utilizando o critério de espaços em branco
#     # em que uma palavra é uma sequência de caracteres sem espaços
#     palavras = texto.split()

#     contagem = {}
#     for palavra in palavras:
#         # não é possível acessar a chave palavra diretamente,
#         # pois ela pode não existir
#         # contagem[palavra] += 1
#         contagem[palavra] = contagem.get(palavra, 0) + 1
#     return contagem
  
# texto = """
# Python é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991. Python é conhecida por sua sintaxe clara e legível, o que a torna uma excelente escolha para iniciantes e profissionais. A linguagem suporta múltiplos paradigmas de programação, incluindo programação procedural, orientada a objetos e funcional. Além disso, Python possui uma vasta biblioteca padrão e uma comunidade ativa que contribui com uma infinidade de pacotes e módulos, facilitando o desenvolvimento de aplicações complexas.

# Python é amplamente utilizada em diversas áreas, como desenvolvimento web, ciência de dados, inteligência artificial, automação de tarefas, entre outras. Sua popularidade cresceu significativamente nos últimos anos devido à sua versatilidade e facilidade de uso. A linguagem é compatível com diferentes sistemas operacionais, como Windows, macOS e Linux, e pode ser integrada com outras linguagens de programação.

# A filosofia do Python enfatiza a legibilidade do código e a simplicidade, seguindo o princípio de que "há apenas uma maneira óbvia de fazer algo". Isso ajuda os desenvolvedores a escreverem código mais limpo e eficiente. Com uma curva de aprendizado suave e uma comunidade acolhedora, Python continua a ser uma das linguagens de programação mais populares e influentes do mundo.
# """
# #print(conta_palavras(texto))

# def conta_palavras_com_defaultdict(texto: str) -> dict[str, int]:
#     # transformar o texto para minúsculas
#     texto = texto.lower()

#     # Limpar caracteres especiais, permitindo apenas letras, números, espaços e hífens
#     texto = limpa_texto(texto)

#     # divide o texto em palavras,
#     # utilizando o critério de espaços em branco
#     # em que uma palavra é uma sequência de caracteres sem espaços
#     palavras = texto.split()

#     contagem = defaultdict(int)
#     for palavra in palavras:
#         # como utilizamos o defaultdict,
#         # não é necessário verificar se a chave existe,
#         # nem utilizar o método get
#         contagem[palavra] += 1
#     return contagem
  
# texto = """ Python é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991. Python é conhecida por sua sintaxe clara e legível, o que a torna uma excelente escolha para iniciantes e profissionais. A linguagem suporta múltiplos paradigmas de programação, incluindo programação procedural, orientada a objetos e funcional. Além disso, Python possui uma vasta biblioteca padrão e uma comunidade ativa que contribui com uma infinidade de pacotes e módulos, facilitando o desenvolvimento de aplicações complexas. Python é amplamente utilizada em diversas áreas, como desenvolvimento web, ciência de dados, inteligência artificial, automação de tarefas, entre outras. Sua popularidade cresceu significativamente nos últimos anos devido à sua versatilidade e facilidade de uso. A linguagem é compatível com diferentes sistemas operacionais, como Windows, macOS e Linux, e pode ser integrada com outras linguagens de programação. A filosofia do Python enfatiza a legibilidade do código e a simplicidade, seguindo o princípio de que "há apenas uma maneira óbvia de fazer algo". Isso ajuda os desenvolvedores a escreverem código mais limpo e eficiente. Com uma curva de aprendizado suave e uma comunidade acolhedora, Python continua a ser uma das linguagens de programação mais populares e influentes do mundo. """
# #print(conta_palavras_com_defaultdict(texto))

# def conta_palavras_com_counter(texto: str) -> Counter:
#     # transformar o texto para minúsculas
#     texto = texto.lower()

#     # Limpar caracteres especiais, permitindo apenas letras, números, espaços e hífens
#     texto = limpa_texto(texto)

#     # divide o texto em palavras,
#     # utilizando o critério de espaços em branco
#     # em que uma palavra é uma sequência de caracteres sem espaços
#     palavras = texto.split()

#     # não é mais necessário criar um for loop,
#     # pois o Counter faz isso automaticamente
#     return Counter(palavras)
  
# #print(conta_palavras_com_counter(texto))

# ##2. Crie um dicionário para armazenar a frequência de caracteres numéricos em uma frase.

# #criar texto e variavel para armazenar tamanho do texto(percorrido letra a letra)
# #Limpar o texto para que ele fique sem espaços e caracteres especiais(usando uma função)
# #Criar função para contar os caracteres
# #    1. limpar o texto e deixa-lo em letras minusculas
# #    2. criar um dicionario com defaltdict(da valores default em inteiros para chaves sem valor)
# #    3. criar uma variavel para contar a quantidade de caracteres validos
# #    4. criar um loop de repetição que percorre o texto e adiciona mais 1 para o caracter presente
# #    5. adicionar um encremento na variavel de caracteres
# #    6. criar chave "especiais" e subtrair o numero de caracters validos do numero de caracteres geral do texto(não limpo) 
# #    7. retornar a lista 
# #Criar função que recebe uma lista e o numer de caracteres geral 


# texto = """
# Python é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991. Python é conhecida por sua sintaxe clara e legível, o que a torna uma excelente escolha para iniciantes e profissionais. A linguagem suporta múltiplos paradigmas de programação, incluindo programação procedural, orientada a objetos e funcional. Além disso, Python possui uma vasta biblioteca padrão e uma comunidade ativa que contribui com uma infinidade de pacotes e módulos, facilitando o desenvolvimento de aplicações complexas.
# """

# n = len(texto)
# def limpa_texto2(texto: str) -> str:
#     novo_texto = ""
#     for letra in texto:
#         if letra.isalnum():
#             novo_texto += letra
#         else:
#           novo_texto += ""
#     return novo_texto
  
# def conta_caracteres(texto: str) -> dict[str, int]:
#     texto_limpo = limpa_texto(texto.lower())
#     count = defaultdict(int)
#     total_valid_chars = 0
#     for letra in texto_limpo:
#         count[letra] += 1
#         total_valid_chars += 1
#     count["especiais"] = n - total_valid_chars
#     return count
  
# def count_dict_to_freq_dict(count: dict[str, int], n: int) -> dict[str, float]:
#     # for key, value in count.items():
#     #     count[key] = round(100 * value / n, 2)
#     # return count
#     return {key: round(100 * value / n, 2) for key, value in count.items()}


# contagem_de_caracteres = conta_caracteres(texto)
# frequencia_de_caracteres = count_dict_to_freq_dict(contagem_de_caracteres, n)
# print(frequencia_de_caracteres)

##3. Treinando criando um contador para contar os caracteres especiais

texto = """
A @vida #pode &ser %complicada, mas *nunca +deixe de ~lutar. Às vezes, -as dificuldades vêm ?em momentos que (não) esperamos; [entretanto], é necessário `manter-se firme! "Persistência" e {coragem} são ~qualidades essenciais: utilize-as sempre. Não \permita/ que obstáculos alterem |seu| caminho. Aprender a vencer =desafios é a chave para o sucesso. @$Hoje é o dia de começar: ^trabalhe duro, _dedique-se e ;nunca> desista. Cada <passo> que você dá, cada {esforço}, cada resultado (positivo) deve ser celebrado! Caminhe com &determinação, foque-se em #seus objetivos e *alcançará grandes realizações! Acredite em si, e vá além.```
"""
n = len(texto)

def limpa_texto(texto: str) -> str:
  novo_texto = ""
  for l in texto:
    if l.isalnum() or l == " ":
      novo_texto += ""
    else:
      novo_texto += l
  return novo_texto
      

def conta_caracteres_especiais(texto: str) -> dict[str, int]:
  novo_texto = limpa_texto(texto)
  count = defaultdict(int)
  tamanho = len(novo_texto)
  for schar in novo_texto:
    count[schar] += 1 
  count["letras"] = n - tamanho
  return count

print(conta_caracteres_especiais(texto))
    
    
  


  
  