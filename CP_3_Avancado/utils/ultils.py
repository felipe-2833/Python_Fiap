//pydantic
from string import ascii_letters, digits

characters = ascii_letters + digits + "_" + "-" + "."

def is_alnum_or_underscore(c:str) -> bool:
    return c in characters and len(c) == 1

def validar_dominio(domain:str) -> bool:
    if "." not in domain:
        return False
    parts = domain.split(".") 
    for p in parts:
        if not len(p):
            return False
    if not(2 <= len(parts) <= 3):
        return False
    return all(map(lambda x : map(lambda c : c in characters,x) or x in "", parts))  

def count_chars(s:str, pattern: str) -> dict:
    return len(c for c in s if c in pattern)