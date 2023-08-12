def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

p = int(input("Ingrese un número: "))
if es_primo(p):
    print("El número", p, "es primo.")
else:
    print("El número", p, "no es primo.")

