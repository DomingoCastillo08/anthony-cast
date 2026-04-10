#!/usr/bin/env python3
"""Calculadora básica en línea de comandos."""


def sumar(a: float, b: float) -> float:
    return a + b


def restar(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b


def calcular(opcion: str, a: float, b: float) -> float:
    operaciones = {
        "1": sumar,
        "2": restar,
        "3": multiplicar,
        "4": dividir,
    }

    if opcion not in operaciones:
        raise ValueError("Operación no válida.")

    return operaciones[opcion](a, b)


def main() -> None:
    print("=== Calculadora ===")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")

    opcion = input("Elige una operación (1-4): ").strip()

    try:
        a = float(input("Ingresa el primer número: ").strip())
        b = float(input("Ingresa el segundo número: ").strip())
        resultado = calcular(opcion, a, b)
    except ValueError as error:
        print(f"Error: {error}")
        return

    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
