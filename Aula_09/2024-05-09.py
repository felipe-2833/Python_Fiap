from pprint import pprint
from time import sleep

user_bd: list[tuple] = [
    # posicao:
    # - 0: user id
    # - 1: senha
    # - 2: data de nascimento
    # - 3: user name
    # Exemplos
    # ("1", "fgdsfgdf", "2000-01-01"),
    # ("2", "fgdsfkjk", "2000-06-01"),
]
# user_bd[0] = ("1", "fgdsfgdf", "2000-10-01")


def next_user_id() -> str:
    if not user_bd:
        return "1"
    return str(int(user_bd[-1][0]) + 1)


def cadastro() -> None:
    print("Cadastro de usuários:")
    while True:
        user_name = input("\nUser name: ")
        senha = input("Senha: ")
        data_nascimento = input("Data de nascimento: ")

        user_id = next_user_id()

        user_bd.append((user_id, senha, data_nascimento, user_name))

        continuar = input("\nContinuar cadastrando usuários? [S/n]: ")
        print("\n")
        if continuar.lower() != "s":
            return


# def busca_por_id(user_id: int) -> tuple:
#     for user in user_bd:
#         if user[0] == user_id:
#             return user
#     return ()


# def busca_por_data_nascimento(data_nascimento: str) -> tuple:
#     for user in user_bd:
#         if user[3] == data_nascimento:
#             return user
#     return ()


# def busca_por_user_name(user_name: str):
#     for user in user_bd:
#         if user[4] == user_name:
#             return user
#     return ()


def _busca(chave: int, valor: str | int) -> tuple:
    for user in user_bd:
        if user[chave] == valor:
            return user
    return ()


def busca(chave: str, valor: str | int) -> tuple:
    match chave:
        case "0" | "2" | "3":
            return _busca(int(chave), valor)
        case "1":
            print("Busca por senha não é permitida")
        case _:
            print("Opção inválida")
    return ()


while True:
    print("\n\nMenu XPTO")
    print("\t1 - Cadastrar usuários")
    print("\t2 - Imprimir lista de usuários")
    print("\t3 - Buscar um usuário")
    print("\t4 - Encerrar")
    opcao = input("Opção: ")
    match opcao:
        case "1":
            cadastro()
        case "2":
            pprint(user_bd)
        case "3":
            print("\nPor qual campo você deseja buscar?")
            print("\t0 - user id")
            print("\t2 - data de nascimento")
            print("\t3 - user name")
            chave = input("Opção: ")

            valor = input("Qual o valor de busca? ")
            print(busca(chave, valor))
        case "4":
            print("Encerrando", end="", flush=True)
            for i in range(6):
                sleep(1)
                print(".", end="", flush=True)
            print()
            break
        case _:
            print("Opção inválida")

# exemplo de alteração de senha
# uid, senha_velha, nasc, unane = *user_bd[0]
# user_bd[0] = (uid, nova_senha, nasc, unane)
