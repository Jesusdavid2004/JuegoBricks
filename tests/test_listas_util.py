import pytest
from src.listas_util import obtener_maximo, obtener_minimo, promedio

def test_obtener_maximo():
    assert obtener_maximo([1, 2, 3, 4]) == 4
    assert obtener_maximo([-1, -5, -3]) == -1
    assert obtener_maximo([]) is None

def test_obtener_minimo():
    assert obtener_minimo([1, 2, 3, 4]) == 1
    assert obtener_minimo([-1, -5, -3]) == -5
    assert obtener_minimo([]) is None

def test_promedio():
    assert promedio([1, 2, 3, 4]) == 2.5
    assert promedio([-1, -5, -3]) == -3
    assert promedio([]) == 0
