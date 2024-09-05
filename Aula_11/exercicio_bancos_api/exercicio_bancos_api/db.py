import json

from functools import cache
from pathlib import Path


import requests


DADOS_DIR = Path(__file__).parent / "dados"
DADOS_DIR.mkdir(exist_ok=True)
BANCOS_FILE = DADOS_DIR / "bancos.json"
PIX_PARTICIPANTES_FILE = DADOS_DIR / "pix_participantes.json"

METADATA = {
    "bancos": {
        "url": "https://brasilapi.com.br/api/banks/v1",
        "filename": BANCOS_FILE,
    },
    "pix_participantes": {
        "url": "https://brasilapi.com.br/api/pix/v1/participants",
        "filename": PIX_PARTICIPANTES_FILE,
    },
}


def get_dados(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    with open(filename, "w") as f:
        json.dump(data, f)
    return data


def load(filename):
    with open(filename) as f:
        return json.load(f)


def load_or_create(key):
    try:
        return load(METADATA[key]["filename"])
    except FileNotFoundError:
        return get_dados(**METADATA[key])


@cache
def load_data():
    return {
        "bancos": load_or_create("bancos"),
        "pix_participantes": load_or_create("pix_participantes"),
    }


def load_bancos():
    return load_data()["bancos"]


def load_pix_participantes():
    return load_data()["pix_participantes"]
