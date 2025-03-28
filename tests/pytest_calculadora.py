import pytest
from src.calculadora import fatorial, soma, divisao, subtracao, multiplicacao, potencia

def test_fatorial_positivo():
    assert fatorial(5) == 120

def test_fatorial_zero():
    assert fatorial(0) == 1

def test_fatorial_maior_que_zero():
    assert fatorial(5) > 0

def test_fatorial_nao_negativo():
    assert not fatorial(5) < 0

def test_soma_positiva():
    assert soma(20, 10) == 30

def test_soma_negativo():
    assert soma(-15, -7) == -22

def test_subtracao_positiva():
    assert subtracao(13, 5) == 8

def test_subtracao_negativo():
    assert subtracao(-21, 8) == -29

def test_multiplicacao_positivo():
    assert multiplicacao(10, 3) == 30

def test_multiplicacao_negativo():
    assert multiplicacao(-7, -5) == 35

def test_divisao_decimal():
    assert divisao(7, 2) == 3.5

def test_divisao_negativo():
    assert divisao(-6, 3) == -2

def test_divisao_por_zero():
    assert divisao(5, 0) == "Não é possível fazer divisão por zero!"

def test_potencia_positiva():
    assert potencia(2, 3) == 8

def test_potencia_expoente_zero():
    assert potencia(5, 0) == 1

def test_potencia_negativa():
    assert potencia(2, -2) == 0.25
    assert potencia(-2, 3) == -8
