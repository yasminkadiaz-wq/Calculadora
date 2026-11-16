"""Funciones matemáticas de la calculadora."""
import math


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b


def potencia(base, exponente):
    if base == 0 and exponente < 0:
        raise ValueError("0 elevado a un exponente negativo no está definido.")
    return base ** exponente


def modulo(a, b):
    if b == 0:
        raise ValueError("El divisor del módulo no puede ser cero.")
    return a % b


def raiz_cuadrada(n):
    if n < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(n)


def porcentaje(porcentaje, cantidad):
    return porcentaje * cantidad / 100


def valor_absoluto(n):
    return abs(n)


def factorial(n):
    if n != int(n) or n < 0:
        raise ValueError("El factorial solo se define para enteros no negativos.")
    return math.factorial(int(n))


def promedio(numeros):
    if len(numeros) == 0:
        raise ValueError("Debes ingresar al menos un número.")
    return sum(numeros) / len(numeros)


def redondeo(numero, decimales):
    if decimales != int(decimales) or decimales < 0:
        raise ValueError("Los decimales deben ser un entero no negativo.")
    return round(numero, int(decimales))

