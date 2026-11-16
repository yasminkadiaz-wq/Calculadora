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
    print(" 1. Suma              8. Porcentaje")
    print(" 2. Resta             9. Valor absoluto")
    print(" 3. Multiplicación   10. Factorial")
    print(" 4. División         11. Promedio")
    print(" 5. Potencia         12. Redondeo")
    print(" 6. Módulo           13. Ver historial")
    print(" 7. Raíz cuadrada")
    print("  ")
    print(" 0. Salir")
    print("===================================")


historial = []


def registrar(descripcion, resultado):
    print("Resultado:", resultado)
    historial.append(f"{descripcion} = {resultado}")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if opcion == "0":
                print("Hasta luego....")
                break

        try:
            if opcion == "1":
                a = leer_numero("Primer número: ")
                b = leer_numero("Segundo número: ")
                registrar(f"{a:g} + {b:g}", op.suma(a, b))
            elif opcion == "2":
                a = leer_numero("Primer número: ")
                b = leer_numero("Segundo número: ")
                registrar(f"{a:g} - {b:g}", op.resta(a, b))
            elif opcion == "3":
                a = leer_numero("Primer número: ")
                b = leer_numero("Segundo número: ")
                registrar(f"{a:g} * {b:g}", op.multiplicacion(a, b))
            elif opcion == "4":
                a = leer_numero("Primer número: ")
                b = leer_numero("Segundo número: ")
                registrar(f"{a:g} / {b:g}", op.division(a, b))
            elif opcion == "5":
                base = leer_numero("Base: ")
                exponente = leer_numero("Exponente: ")
                registrar(f"{base:g} ^ {exponente:g}", op.potencia(base, exponente))
            elif opcion == "6":
                a = leer_numero("Primer número: ")
                b = leer_numero("Segundo número: ")
                registrar(f"{a:g} % {b:g}", op.modulo(a, b))
            elif opcion == "7":
                n = leer_numero("Número: ")
                registrar(f"raíz({n:g})", op.raiz_cuadrada(n))
            elif opcion == "8":
                p = leer_numero("Porcentaje: ")
                c = leer_numero("Cantidad: ")
                registrar(f"{p:g}% de {c:g}", op.porcentaje(p, c))
            elif opcion == "9":
                n = leer_numero("Número: ")
                registrar(f"|{n:g}|", op.valor_absoluto(n))
            elif opcion == "10":
                n = leer_numero("Entero no negativo: ")
                registrar(f"{n:g}!", op.factorial(n))
            elif opcion == "11":
                numeros = leer_lista("Números separados por espacios: ")
                registrar(f"promedio({', '.join(f'{x:g}' for x in numeros)})", op.promedio(numeros))
            elif opcion == "12":
                n = leer_numero("Número: ")
                d = leer_numero("Cantidad de decimales: ")
                registrar(f"redondeo({n:g}, {d:g})", op.redondeo(n, d))
            elif opcion == "13":
                if not historial:
                    print("El historial está vacío.")
                for i, linea in enumerate(historial, 1):
                    print(f"{i}. {linea}")
            else:
                    print("Opción no válida.")
        except ValueError as error:
            print("Error:", error)

        if input("\n¿Realizar otra operación? (s/n): ").strip().lower() != "s":
            print("Hasta luego....")
            break


if __name__ == "__main__":
    main()
