"""Menú e interacción con el usuario."""
import operaciones as op


def main():
    print("=== CALCULADORA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Módulo")
    print("7. Raíz cuadrada")
    print("8. Porcentaje")
    print("9. Valor absoluto")
    print("10. Factorial")
    print("11. Promedio")
    print("12. Redondeo")
    opcion = input("Elige una opción: ")

    try:
        if opcion == "1":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", op.suma(a, b))
        elif opcion == "2":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", op.resta(a, b))
        elif opcion == "3":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", op.multiplicacion(a, b))
        elif opcion == "4":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", op.division(a, b))
        elif opcion == "5":   # antes del else
            base = float(input("Base: "))
            exponente = float(input("Exponente: "))
            print("Resultado:", op.potencia(base, exponente))
        elif opcion == "6":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", op.modulo(a, b))
        elif opcion == "7":
            n = float(input("Número: "))
            print("Resultado:", op.raiz_cuadrada(n))
        elif opcion == "8":
            p = float(input("Porcentaje: "))
            c = float(input("Cantidad: "))
            print("Resultado:", op.porcentaje(p, c))
        elif opcion == "9":
            n = float(input("Número: "))
            print("Resultado:", op.valor_absoluto(n))
        elif opcion == "10":
            n = float(input("Entero no negativo: "))
            print("Resultado:", op.factorial(n))
        elif opcion == "11":
            numeros = [float(x) for x in input("Números separados por espacios: ").split()]
            print("Resultado:", op.promedio(numeros))
        elif opcion == "12":
            n = float(input("Número: "))
            d = float(input("Cantidad de decimales: "))
            print("Resultado:", op.redondeo(n, d))
        else:
            print("Opción no válida.")
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
