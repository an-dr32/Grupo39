numero = int(input("Digite el numero a verificar: "))

cont = 0
for i in range(1,numero + 1):
    if numero % i == 0:
        cont = cont + 1

if cont == 2:
    print("el numero es primo")
else:
    print("el numero no es primo")

print("El numero digitado es: ", numero)