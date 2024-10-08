from typing import TypedDict
from datetime import date
from enum import StrEnum


class Role(StrEnum):
    ADMIN = "admin"
    USER = "user"

class Endereco(TypedDict):
    rua: str
    numero: int
    complemento: str
    cep: str
    cidade: str
    estado: str
    pais: str

class User(TypedDict):
    id: int
    username: str
    password: str
    email: str
    nome: str
    rg: str
    cpf: str
    data_de_nascimento: date
    #TODO: criar classe base para endereco e role
    endereco: Endereco
    role: Role

    