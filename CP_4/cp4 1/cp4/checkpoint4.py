__author__ = {
    "nome": "Felipe Levy Stephens Fidelix",
    "rm": "RM556426",
}


# Questão 1: Filtrar estudantes
def filtrar_estudantes(pessoas, target=True):
    """
    Filtra as pessoas que são estudantes ou não-estudantes,
    com base no parâmetro 'target'.

    :param pessoas: lista de dicionários representando as pessoas
    :param target: booleano, True para filtrar estudantes, False para não-estudantes
    :return: lista filtrada de dicionários com nome e idade
    """
    # Comece a implementação aqui
    estudantes = [] # Lista que armazenará as pessoas filtradas
    for pessoa in pessoas:
        if pessoa.get("estudante") == target:
            estudantes.append({"nome":pessoa.get("nome"), "idade":pessoa.get("idade")})
    return estudantes

lista_estudantes = [
                  {"nome": "Mark", "idade": 21, "estudante": True},
                  {"nome": "Tom", "idade": 35, "estudante": False},
                  {"nome": "Eva", "idade": 19, "estudante": True},
                  {"nome": "Lucy", "idade": 32, "estudante": False},
                  {"nome": "Alice", "idade": 25, "estudante": True},
                  {"nome": "Carlos", "idade": 30, "estudante": False},
                  {"nome": "Bianca", "idade": 22, "estudante": True},
                  {"nome": "Daniel", "idade": 28, "estudante": False}
                 ]

print(filtrar_estudantes(lista_estudantes))


# Questão 2: Calcular média de idade dos estudantes
def calcular_media_idade(pessoas):
    """
    Calcula a média de idade das pessoas filtradas como estudantes.

    :param pessoas: lista de dicionários representando as pessoas
    :return: média da idade dos estudantes ou None se não houver estudantes
    """
    # A função deverá obrigatoriamente chamar a função filtrar_estudantes
    estudantes = filtrar_estudantes(pessoas)

    # Comece a implementação aqui
    soma = 0
    if estudantes == []:
        return None
    for estudante in estudantes:
        soma += estudante["idade"]
    media = soma / len(estudantes)
    return media
    
print(calcular_media_idade(lista_estudantes))

# Questão 3: Adicionar novo estudante se a média de idade for menor que 25
def adicionar_novo_estudante(pessoas, nome, idade, estudante=True):
    """
    Adiciona um novo estudante à lista de pessoas se a média de idade dos
    estudantes existentes for menor que 25.

    :param pessoas: lista de dicionários representando as pessoas
    :param nome: string, nome do novo estudante
    :param idade: inteiro, idade do novo estudante
    :param estudante: booleano, status de estudante (True por padrão)
    """
    # A função deverá obrigatoriamente chamar a função calcular_media_idade
    media_estudantes = calcular_media_idade(pessoas)

    # Comece a implementação aqui
    ...
    if media_estudantes < 25:
        pessoas.append({"nome":nome, "idade":idade, "estudante":estudante})
    
    # Não retorna nada, pois apenas modifica a lista pessoas


# Questão 4: Atualizar estudantes ou adicionar novo estudante
def atualizar_estudantes(pessoas, novo_estudante):
    """
    Atualiza as informações de um estudante na lista de pessoas ou
    adiciona um novo estudante se ele não estiver presente.

    :param pessoas: lista de dicionários representando as pessoas
    :param novo_estudante: dicionário com as informações do novo estudante
    """

    # comece a implementação aqui
    try:
        for pessoa in pessoas:
            if pessoa["nome"] == novo_estudante["nome"]:
                pessoa["idade"] = novo_estudante["idade"]
                pessoa["estudante"] = novo_estudante["estudante"]
            else:
                # deverá chamar a função adicionar_novo_estudante,
                # caso atenda aos critérios
                adicionar_novo_estudante(
                    pessoas,
                    novo_estudante["nome"],
                    novo_estudante["idade"],
                    novo_estudante["estudante"],
                )
    except KeyError as e:
        print("Chave requerida não encontrada:\t", e)
    # Não retorna nada, pois apenas modifica a lista pessoas

nA = {"nome":"Claubin","idade":0}
atualizar_estudantes(lista_estudantes,nA)

# Questão 5: Calcular média de idade por status de estudante
def calcular_media_por_status(pessoas):
    """
    Calcula a média de idade separadamente para estudantes e não-estudantes.

    :param pessoas: lista de dicionários representando as pessoas
    :return: dicionário com as médias de idade dos estudantes e não-estudantes
    """
    # Comece a implementação aqui

    # A função deverá obrigatoriamente chamar a função filtrar_estudantes,
    # atentando-se aos parâmetros
    estudantes = filtrar_estudantes(pessoas)
    nao_estudantes = filtrar_estudantes(pessoas, False)
    soma1 = 0
    soma2 = 0 
    if estudantes == [] or nao_estudantes == []:
        media1 = None
        media2 = None
    for pessoa in estudantes:
        soma1 += pessoa["idade"]
    media1 = soma1 / len(estudantes)
    for pessoa in nao_estudantes:
        soma2 += pessoa["idade"]
    media2 = soma2 / len(nao_estudantes)

    return {
        "media_estudantes": media1,
        "media_nao_estudantes": media2,
    }

print(calcular_media_por_status(lista_estudantes))
