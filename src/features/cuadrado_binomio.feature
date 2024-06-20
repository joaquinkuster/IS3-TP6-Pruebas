# Escenarios con Formalismo Gherkin para la funcion cuadrado_binomio

Feature: Calcular el cuadrado de un binomio

  Scenario: calcular el cuadrado de un binomio conformado por un numero positivo y un numero negativo
    Given los números 1 y -1
    When calculamos el cuadrado del binomio con los números dados
    Then el resultado debe ser 0