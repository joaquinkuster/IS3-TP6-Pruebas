# Escenarios con Formalismo Gherkin

Feature: Suma de dos números

  # Escenario para la Función Suma
  Scenario: Sumar dos números enteros positivos
    Given los números 2 y 3
    When se suman
    Then el resultado debe ser 5