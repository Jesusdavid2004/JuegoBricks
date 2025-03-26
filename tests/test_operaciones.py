import pytest
from src.operaciones import cuadrado, es_par, saludar

def test_cuadrado():
    assert cuadrado(2) == 4
    assert cuadrado(-3) == 9
    assert cuadrado(0) == 0

def test_es_par():
    assert es_par(2) is True
    assert es_par(3) is False
    assert es_par(0) is True

def test_saludar():
    assert saludar("Juan") == "Hola, Juan!"
    assert saludar("María") == "Hola, María!"
    assert saludar("") == "Hola, !"
