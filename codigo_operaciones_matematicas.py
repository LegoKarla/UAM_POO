def suma(a, b):
    return a + b

def resta (a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        print("No se puede dividir entre cero")
        return None


print("\nSeleccione una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = int(input("Ingrese el número de la operación deseada: "))

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

if opcion == 1:
    resultado = suma(a, b)
    print("La suma de", a, "y", b, "es: ", resultado)

elif opcion == 2:
    resultado = resta(a, b)
    print("La resta de", a, "y", b, "es: ", resultado)

elif opcion == 3:
    resultado = multiplicacion(a, b)
    print("La multiplicacion de", a, "y", b, "es: ", resultado)

elif opcion == 4:
    resultado = division(a, b)
    if resultado is not None:
        print("La division  de", a, "y", b, "es: ", resultado)

else:
    print("Opción inválida.")

