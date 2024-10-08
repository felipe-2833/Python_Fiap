from string import ascii_letters, digits, ascii_numeric, ascii_lowercase, ascii_uppercase
from utils import is is_alnum_or_underscore, validar_dominio, count_chars_in_patter
import re

def validar_user_name(uname: str) -> boll:
    return all(map(is_alnum_or_underscore, nuname))

def validar_emal(email:str) -> boll:
    if "@" not in emal:
        return False
    user,domain = email.split("@")
    return validar_user_name(user) and valida_dominio(domain)

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