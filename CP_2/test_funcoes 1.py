import pytest

from funcoes import (
    conversor_temperatura,
    valida_email,
    eh_palindromo,
    soma_quadrados,
    conta_palavras,
)


@pytest.mark.parametrize(
    "temperatura, de, para, expected",
    [
        (0, "C", "F", 32),
        (-50, "C", "F", -58),
        (1000, "C", "K", 1273.15),
        (-50, "C", "K", 223.15),
        (1000, "F", "C", 537.778),
        (-100, "F", "C", -73.333),
        (-100, "F", "K", 199.817),
        (1000, "F", "K", 810.928),
        (0.1, "K", "C", -273.05),
        (400, "K", "C", 126.85),
        (400, "K", "F", 260.33),
        (55, "K", "F", -360.67),
    ],
)
def test_conversor_temperatura(temperatura, de, para, expected):
    result = conversor_temperatura(temperatura, de, para)

    assert pytest.approx(result, rel=1e-2) == expected


@pytest.mark.parametrize(
    "email, expected",
    [
        ("nome_sobr.nome@dominio.com", True),
        ("nome_sobr.nome@dfg.com.br", True),
        ("nomesobre.nome@dominio.tyr.br", True),
        ("nomesobre_nome@dfgdfg.com.fdghj", True),
        ("nome_dfyghfdg.nome@", False),
        ("nome_dfyghfdg.nome@xdfghd", False),
        ("@xdfghd", False),
        ("@xdfghd.com", False),
        ("%^#$@xdfghd.56%4", False),
    ],
)
def test_valida_email(email, expected):
    result = valida_email(email)

    assert result == expected


@pytest.mark.parametrize(
    "texto, expected",
    [
        ("0123210", True),
        ("ovo", True),
        ("radar", True),
        ("reler", True),
        ("arara", True),
        ("Ame o poema", True),
        ("A cara rajada da jararaca", True),
        ("A base do teto desaba", True),
        ("Socorram-me, subi no ônibus em Marrocos", True),
        ("A sacada da casa", True),
        ("A torre da derrota", True),
        ("A dama admirou o rim a dama", True),
        ("A Rita, sobre vovô, verbos atira", True),
        ("0123214", False),
        ("banana", False),
        ("carro", False),
        ("Este não é um palíndromo", False),
        ("Teste unitário", False),
        ("Aqui não tem palíndromo", False),
        ("Isso não é um palíndromo", False),
    ],
)
def test_palindromo(texto, expected):
    assert eh_palindromo(texto) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, 55),
        (10, 385),
        (0, 0),
        (-1, 0),
        (-5, 0),
        (-10, 0),
        (-100, 0),
        (1000, 333833500),
        (10000, 333383335000),
        (100000, 33333833335000),
    ],
)
def test_soma_quadrados(n, expected):
    result = soma_quadrados(n)

    assert expected == pytest.approx(result, rel=1e-0)


@pytest.mark.parametrize(
    "texto, expected",
    [
        ("Olá mundo", 2),
        ("Esta é uma frase.", 4),
        ("Contando palavras, apenas", 3),
        ("PalavrasPalavrasPalavras", 1),  # Uma palavra sem espaços
        ("    ", 0),  # String contendo apenas espaços
        (
            "   Palavras com espaços  ",
            3,
        ),  # Palavras com espaços extras no início e no fim
        ("12345", 1),  # Uma sequência de números
        (
            "   Palavras123 Com Números456   ",
            3,
        ),  # Palavras misturadas com números e espaços extras
    ],
)
def test_conta_palavras(texto, expected):
    result = conta_palavras(texto)

    assert expected == result
