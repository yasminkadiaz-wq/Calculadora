"""Funciones matemáticas de la calculadora."""
import math


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


def potencia(base, exponente):
    if base == 0 and exponente < 0:
        raise ValueError("0 elevado a un exponente negativo no está definido.")
    return base ** exponente


def modulo(a, b):
    return a % b
