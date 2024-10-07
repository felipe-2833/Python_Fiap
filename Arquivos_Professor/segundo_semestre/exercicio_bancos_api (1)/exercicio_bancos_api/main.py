# Com base na [Brasil API](https://brasilapi.com.br/docs), vamos:
# - Capturar todos bancos disponíveis
# - Capturar todos participantes do PIX
# - Oferecer para o usuário uma alternativa para buscar se um banco é ou não participante do PIX


from db import load_bancos, load_pix_participantes


def listar_bancos():
    bancos = load_bancos()
    for banco in bancos:
        print(f"{banco['code']} - {banco.get('name', 'Nome não disponível')}")


def listar_pix_participantes():
    pix_participantes = load_pix_participantes()
    for p in pix_participantes:
        print(f"{p.get('nome', 'Nome não disponível')}")


def mapa_banco_ispb(lista_bancos):
    mapa = {}
    for banco in lista_bancos:
        if "name" in banco:
            mapa[banco["ispb"]] = banco["name"]
        elif "nome" in banco:
            mapa[banco["ispb"]] = banco["nome"]
    return mapa


def verificar_banco_pix(cod_banco):
    bancos = load_bancos()

    for banco in bancos:
        if banco["code"] == cod_banco:
            ispb = banco["ispb"]
            break
    else:
        print("Banco não encontrado")
        return False

    pix_participantes = load_pix_participantes()
    mapa_bancos = mapa_banco_ispb(bancos)
    mapa_pix = mapa_banco_ispb(pix_participantes)
    return ispb in mapa_pix and ispb in mapa_bancos


def menu():
    print("=====================================================")
    print("\nMenu")
    print("1 - Verificar se um banco é participante do PIX")
    print("2 - Listar todos os bancos disponíveis")
    print("3 - Listar todos os participantes do PIX")
    print("4 - Sair")
    print("=====================================================")
    return input("Escolha uma opção: ")


print("Bem-vindo ao sistema de consulta de bancos e participantes do PIX")

while True:
    choice = menu()
    match choice:
        case "1":
            cod_banco = int(input("Digite o código do banco: "))
            print("\n\n\n")
            print("=====================================================")
            print(f"Verificando se o banco {cod_banco} é participante do PIX...")
            if verificar_banco_pix(cod_banco):
                print("Banco é participante do PIX")
            else:
                print("Banco não é participante do PIX")
            print("=====================================================\n\n")
        case "2":
            listar_bancos()
        case "3":
            listar_pix_participantes()
        case "4":
            break
        case _:
            print("Opção inválida")
            continue
