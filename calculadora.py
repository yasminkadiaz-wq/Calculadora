"""Menú e interacción con el usuario."""
import operaciones as op


def main():
    print("=== CALCULADORA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
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
        else:
            print("Opción no válida.")
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
