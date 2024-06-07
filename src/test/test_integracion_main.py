import pytest
from src.main import suma, resta, cuadrado_binomio

## Prueba Integración: Entre la función suma, resta y cuadrado de un binomio
def test_cuadrado_binomio_integracion():
    a = 2
    b = 3
    suma_ab = suma(a, b)
    resta_ab = resta(a, b)
    cuadrado_ab = cuadrado_binomio(a, b)

    assert suma_ab == 5
    assert resta_ab == -1
    assert cuadrado_ab == 25
