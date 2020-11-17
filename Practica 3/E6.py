'''Pide al usuario el precio de un producto y el nombre del producto y muestra el mensaje con el precio del IVA (21%). 
Por ejemplo: “Tu bicicleta vale 100 euros y con el 21 % de IVA se queda en 121 euros en total”.'''

producto = input("Introduzca el nombre del producto: ")
precio = float(input("Introduzca el precio del producto: "))

IVA = precio * 0.21
precio_final = precio + IVA

print("Tu",producto,"vale",precio,"euros y con el 21% de IVA se queda en",precio_final,"euros en total.")