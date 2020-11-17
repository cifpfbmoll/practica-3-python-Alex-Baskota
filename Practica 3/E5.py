'''Pida un número que como máximo tenga tres cifras (por ejemplo serían válidos 1, 99 i 213 pero no 1001). 
Si el usuario introduce un número de más de tres cifras debe informar con un mensaje de error como este: 
“ERROR: El número 1005 tiene más de tres cifras”.'''

numero = int(input("Introduzca un número de hasta 3 cifras: "))
if numero<999:
    print("Número",numero)
else:
    print("ERROR: El número",numero,"tiene más de 3 cifras")