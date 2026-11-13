print("Ejemplo 1:")
print("Hola, soy Emir y voy a comprar playeras")
i = 1
while i <= 4:
    print(i)
    i += 1
print("Emir compro 4 playeras")

print()
print("Ejemplo 2:")

numero = int(input("Introduce una edad mayor a  cero: "))
while numero < 0:
    print("la edad debe ser mayor a cero")
    numero = int(input("Introduce un edad valida: "))
print("Edad registrada correctamente")

print()
print("Ejemplo 3:")
print("Este ciclo mostrara los numeros del 1 al 50")
print("El ciclo termina al llegar al numrto 50")
i = 1
while i < 50:
      print(i, end=" ")
      i += 1




print()
print("Ejemplo 4:")
print("En este ciclo multiplicaremos el numero por 2")
print("El ciclo se detendra cuando el resutado sea mayor a 100")

i = 1
while i <=100:
    print(i)
    i = 2 * i + 1
print("El ciclo se detuvo porque el resultado supero 100")

print()
print("Ejemplo 5:")
print("Voy a ahorrar dinero durante 7 dias")
print()
i = 1
while i <=7:
    print("Dia", i, "Ahorre 20 pesos") 
    i += 1
    print()
    print("Termine de ahorrar durante 7 dias")
print("Logre ahorrar 140 pesos")