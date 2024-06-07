import pytest
from src.main import suma, resta, cuadrado_binomio

## Prueba Unitaria: Función Suma
@pytest.mark.parametrize(
    "num_a, num_b, resultado",
    [
        (2, 3, 5),           
        (2, -3, -1),            
        (0, 5, 5),
        (None, 5, None),     
        (None, None, None),      
        (2, None, None),      
        ('2', 5, 7),
        ('a', 5, None),
        (2, suma(2, 2), 6), 
        (2, suma(2, 2), suma(2, suma(2, 2)))
    ]
)
def test_suma(num_a, num_b, resultado):
    assert suma(num_a, num_b) == resultado

## Prueba Unitaria: Función Resta
@pytest.mark.parametrize(
    "num_a, num_b, resultado",
    [
        (5, 3, 2),           
        (5, -1, 6),        
        (0, 3, -3),
        (None, 1, None),     
        (None, None, None), 
        (7, None, None), 
        ('4', 5, -1),
        ('c', 3, None),
        (3, resta(2, 2), 3),
        (3, resta(2, 2), resta(3, resta(2, 2)))
    ]
)
def test_resta(num_a, num_b, resultado):
    assert resta(num_a, num_b) == resultado

## Prueba Unitaria: Función Cuadrado de un Binomio
@pytest.mark.parametrize(
    "num_a, num_b, resultado",
    [
        (2, 3, 25),           
        (-1, 1, 0),         
        (0, 0, 0),
        (-5, -7, 144),
        (None, 3, None),     
        (None, None, None),      
        (9, None, None),    
        ('3', 2, 25),
        ('b', 12, None),
        (2, cuadrado_binomio(2, 3), 729),
        (5, cuadrado_binomio(-1, 1), cuadrado_binomio(5, cuadrado_binomio(-1, 1)))
    ]
)
def test_cuadrado_binomio(num_a, num_b, resultado):
    assert cuadrado_binomio(num_a, num_b) == resultado
