import pytest
from src.texto_util import contar_letras, convertir_mayusculas, invertir_texto

def test_contar_letras():
    assert contar_letras("Hola") == 4
    assert contar_letras("") == 0
    assert contar_letras("Python") == 6

def test_convertir_mayusculas():
    assert convertir_mayusculas("hola") == "HOLA"
    assert convertir_mayusculas("Python") == "PYTHON"
    assert convertir_mayusculas("") == ""

def test_invertir_texto():
    assert invertir_texto("Hola") == "aloH"
    assert invertir_texto("Python") == "nohtyP"
    assert invertir_texto("") == ""