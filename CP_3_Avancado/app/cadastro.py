from models import Autentication,User
from validations.validations import validate_user_data,validar_senha

BD: dict[str, list[Autentication | User]] = {
    "auth": [],
    "users": [],
}

def new_user(username,email,nome,rg,cpf,data_de_nascimento,endereco,role,*args,**kwargs) -> User:
    user = {
        "id": len(BD["users"]),
        "username": username,
        "email": email,
        "nome": nome,
        "rg": rg,
        "cpf": cpf,
        "data_de_nascimento": data_de_nascimento,
        "endereco": endereco,
        "role": role,
    }
    if not validate_user_data(user):
        raise ValueError("Dados do usuário invalidos")
    return user
    
def new_auth(user_id,password,*args,**kwargs) -> Autentication:
    if not validar_senha(user_data.get("senha", "")):
        raise ValueError("Senha inválida")
    auth = Autentication(
        {
            "user_id": user["id"],
            "password": user_data["senha"],
        }
    )
    return auth

def create_new_user(user_data:dict):
    user = new_user(**user_data)
    auth = new_auth(user["id"], user_data.get())
    BD["auth"].append(auth)
    BD["users"].append(user)