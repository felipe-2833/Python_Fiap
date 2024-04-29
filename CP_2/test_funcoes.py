from funcoes import *


def test_conversor_temperatura():
    input_caso1 = -273.15
    input_caso2 = -173.15

    expected_caso1 = 0
    expected_caso2 = 100

    result_1 = conversor_temperatura(input_caso1, "C", "K")
    result_2 = conversor_temperatura(input_caso2, "C", "K")

    assert result_1 == expected_caso1
    assert result_2 == expected_caso2


def test_conversor_temperatura_fails():
    input_caso3 = 0
    expected_caso3 = 273.15
    result_3 = conversor_temperatura(input_caso3, "C", "K")
    assert result_3 == expected_caso3


def test_valida_email():
    input1 = "nome_sobre.nome@dominio.com"
    input2 = "nome_sobre.nome@"

    expected1 = True
    expected2 = False

    result1 = valida_email(input1)
    result2 = valida_email(input2)

    assert result1 == expected1
    assert result2 == expected2


def test_valida_email_fails():
    input3 = "nome_sobre.nome@dominio.com.br"
    expected3 = True
    result3 = valida_email(input3)
    assert result3 == expected3


def test_palindromo():
    texto = "12321"
    expected = True

    result = eh_palindromo(texto)

    assert result == expected


def test_palindromo_fails():
    texto = "123214"
    expected = False

    result = eh_palindromo(texto)

    assert result == expected


def test_soma_quadrados():
    n = 1
    expected = 1
    result = soma_quadrados(n)

    assert expected == result


def test_soma_quadrados_fails():
    n = 2
    expected = 5
    result = soma_quadrados(n)

    assert expected == result


def test_conta_palavras():
    texto = ""
    expected = 0
    result = conta_palavras(texto)

    assert expected == result


def test_conta_palavras_fails():
    texto = "bom dia cremoso, como está?"
    expected = 5
    result = conta_palavras(texto)

    assert expected == result
