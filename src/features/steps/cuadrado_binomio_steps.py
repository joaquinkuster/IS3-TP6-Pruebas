from behave import given, when, then
from main import cuadrado_binomio

@given('los números {a:d} y {b:d}')
def step_given_los_numeros(context, a, b):
    context.a = a
    context.b = b

@when('calculamos el cuadrado del binomio con los números dados')
def step_when_calculamos_cuadrado_binomio(context):
    context.resultado = cuadrado_binomio(context.a, context.b)

@then('el resultado debe ser {resultado:d}')
def step_then_el_resultado_debe_ser(context, resultado):
    assert context.resultado == resultado
