from string import ascii_letters, digits, ascii_numeric, ascii_lowercase, ascii_uppercase
from utils import is_in_chars, validar_dominio, count_chars_in_patter
from models import User
import re

def validar_user_name(uname: str) -> bool:
    return all(map(is_in_chars, uname))

def validar_email(email:str) -> bool:
    if "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    user,domain = parts
    return validar_user_name(user) and validar_dominio(domain)

def validar_cpf(cpf:str) -> bool:
    return any(
        (
            re.match(r"\d{3}\.\d{3}\.\d{3}-d{2}",cpf),
            re.match(r"\d{11}",cpf)
        )
    )

def validar_rg(rg:str) -> bool:
    return any(
        (
            re.match(r"\d{2}\.\d{3}\.\d{3}-d",rg),
            re.match(r"\d{9}",rg)
        )
    )
    
def validar_senha(senha:str) -> bool:
    
    if len(senha) <= 15:
        return False
    return all(map(lambda pattern: count_chars_in_patter(senha,pattern) >= 3, (
        digits, ascii_uppercase,ascii_lowercase,r"!@#$%&*()[]{};.,:/\|"
    )))
    
User_validations = {
    "email": validar_email,
    "cpf": validar_cpf,
    "rg": validar_rg,
}

def validate_user_data(user: User) -> bool:
    return all(map(lambda key: User_validations[key](user[key],User_validations,)))


