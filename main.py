import codigo_suma_pares
import codigo_es_primo
import codigo_operaciones_matematicas

def main():
    while True:
        print("\nSeleccione una opción:")
        print("1. Suma de números pares")
        print("2. Verificar si un número es primo")
        print("3. Operaciones matemáticas básicas")
        print("4. Salir")

        opcion = int(input("Ingrese el número de la opción deseada: "))

        if opcion == 1:
            codigo_suma_pares.main()
        elif opcion == 2:
            codigo_es_primo.main()
        elif opcion == 3:
            codigo_operaciones_matematicas.main()
        elif opcion == 4:
            print("Saliendo...")
            break  # Salir del ciclo
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
