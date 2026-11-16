"""Menú e interacción con el usuario."""
import operaciones as op


def leer_numero(mensaje):
    """Pide un número hasta que la entrada sea válida."""
    while True:
        try:
            return float(input(mensaje).replace(",", "."))
        except ValueError:
            print("  Entrada no válida. Ingresa un número.")


def leer_lista(mensaje):
    """Pide varios números separados por espacios."""
    while True:
        try:
            numeros = [float(x.replace(",", ".")) for x in input(mensaje).split()]
            if numeros:
                return numeros
            print("  Ingresa al menos un número.")
        except ValueError:
            print("  Entrada no válida. Usa solo números separados por espacios.")


def mostrar_menu():
    print("\n=========== CALCULADORA ===========")
    print(" 1. Suma             7. Raíz cuadrada")
    print(" 2. Resta            8. Porcentaje")
    print(" 3. Multiplicación   9. Valor absoluto")
    print(" 4. División        10. Factorial")
    print(" 5. Potencia        11. Promedio")
    print(" 6. Módulo          12. Redondeo")
    print(" 0. Salir")
    print("===================================")


def main():
    mostrar_menu()
    opcion = input("Elige una opción: ").strip()

    try:
        if opcion == "1":
            a = leer_numero("Primer número: ")
            b = leer_numero("Segundo número: ")
            print("Resultado:", op.suma(a, b))
        elif opcion == "2":
            a = leer_numero("Primer número: ")
            b = leer_numero("Segundo número: ")
            print("Resultado:", op.resta(a, b))
        elif opcion == "3":
            a = leer_numero("Primer número: ")
            b = leer_numero("Segundo número: ")
            print("Resultado:", op.multiplicacion(a, b))
        elif opcion == "4":
            a = leer_numero("Primer número: ")
            b = leer_numero("Segundo número: ")
            print("Resultado:", op.division(a, b))
        elif opcion == "5":
            base = leer_numero("Base: ")
            exponente = leer_numero("Exponente: ")
            print("Resultado:", op.potencia(base, exponente))
        elif opcion == "6":
            a = leer_numero("Primer número: ")
            b = leer_numero("Segundo número: ")
            print("Resultado:", op.modulo(a, b))
        elif opcion == "7":
            n = leer_numero("Número: ")
            print("Resultado:", op.raiz_cuadrada(n))
        elif opcion == "8":
            p = leer_numero("Porcentaje: ")
            c = leer_numero("Cantidad: ")
            print("Resultado:", op.porcentaje(p, c))
        elif opcion == "9":
            n = leer_numero("Número: ")
            print("Resultado:", op.valor_absoluto(n))
        elif opcion == "10":
            n = leer_numero("Entero no negativo: ")
            print("Resultado:", op.factorial(n))
        elif opcion == "11":
            numeros = leer_lista("Números separados por espacios: ")
            print("Resultado:", op.promedio(numeros))
        elif opcion == "12":
            n = leer_numero("Número: ")
            d = leer_numero("Cantidad de decimales: ")
            print("Resultado:", op.redondeo(n, d))
        elif opcion == "0":
            print("Hasta luego...")
        else:
            print("Opción no válida.")
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
