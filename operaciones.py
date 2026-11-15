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


def raiz_cuadrada(n):
    if n < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(n)


def porcentaje(porcentaje, cantidad):
    return porcentaje * cantidad / 100


def valor_absoluto(n):
    return abs(n)
