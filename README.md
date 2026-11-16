# Calculadora en Python

## Descripción
Calculadora de consola desarrollada en Python. Permite realizar operaciones aritméticas y matemáticas desde un menú, valida las entradas del usuario para evitar errores y permite encadenar varias operaciones sin reiniciar el programa.

## Operaciones y estados

| N.º | Operación | Descripción | Estado |
|----:|-----------|-------------|:------:|
| 1 | Potencia | Base elevada a un exponente | ✅ Completada |
| 2 | Módulo | Residuo de una división (divisor ≠ 0) | ✅ Completada |
| 3 | Raíz cuadrada | No acepta negativos | ✅ Completada |
| 4 | Porcentaje | Porcentaje de una cantidad | ✅ Completada |
| 5 | Valor absoluto | \|x\| | ✅ Completada |
| 6 | Factorial | Enteros no negativos | ✅ Completada |
| 7 | Promedio | Media de varios números | ✅ Completada |
| 8 | Redondeo | A los decimales indicados | ✅ Completada |
| 9 | Validación de entradas | Rechaza texto no numérico | ✅ Completada |
| 10 | División por cero | También en el módulo | ✅ Completada |
| 11 | Menú mejorado | Menú numerado y claro | ✅ Completada |
| 12 | Repetir operaciones | Sin reiniciar el programa | ✅ Completada |
| 13 | Historial de operaciones | Lista lo calculado en la sesión | ✅ Completada |
| 14 | Limpiar historial | Borra el historial | ✅ Completada |
| 15 | Mejorar documentación | Ejemplos y README | ✅ Completada |

## Tecnologías
- Python 3
- Git
- GitHub (Issues)
- Markdown

## Instalación y ejecución

```bash
git clone https://github.com/yasminkadiaz-wq/Calculadora.git
cd Calculadora
python calculadora.py
```

## Ejemplo de uso

```text
=========== CALCULADORA ===========
 1. Suma             8. Porcentaje
 ...
Elige una opción: 8
Porcentaje: 15
Cantidad: 200
Resultado: 15% de 200 = 30

¿Realizar otra operación? (s/n): s
```

## Estructura

```text
Calculadora/
├── README.md
├── calculadora.py   # menú e interacción con el usuario
└── operaciones.py   # funciones matemáticas
```

## Autor
Díaz Caneza Yasminka