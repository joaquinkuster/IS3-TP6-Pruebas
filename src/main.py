import math

## Función Suma: Suma dos valores enteros.
def suma (a, b):
    try:
        num_a = int(a)
        num_b = int(b)
        return num_a + num_b
    except(TypeError, ValueError):
        return None

# Función Resta: Resta dos valores enteros.
def resta(a, b):
    try:
        num_a = int(a)
        num_b = int(b)
        return num_a - num_b
    except(TypeError, ValueError):
        return None

# Función Cuadrado de un Binomio: Calcula el cuadrado de la suma de 
# dos valores enteros utilizando la fórmula (a + b)² = a² + 2ab + b².
def cuadrado_binomio(a, b):
    try:
        num_a = int(a)
        num_b = int(b)
        return math.pow(num_a, 2) + 2*num_a*num_b + math.pow(num_b, 2)
    except(TypeError, ValueError):
        return None