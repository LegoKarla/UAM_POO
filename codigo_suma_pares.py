def suma_pares(n, m):
    suma = 0
    for i in range (n, m+1):
        if i % 2 == 0:
            suma += i
    return suma

n = int(input("Ingrese el valor de n: "))
m = int(input("Ingrese el valor de m: "))

if n % 2 != 0:
    n+=1
if m % 2 != 0:
    m-=1

resultado = suma_pares(n, m)

print("La suma de los números pares entre", n, "y", m, "es: ", resultado)

