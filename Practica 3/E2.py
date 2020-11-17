'''2) Realiza un programa que pida al usuario el espacio recorrido 
por un coche y el tiempo que ha tardado en horas y que calcule 
a qué velocidad media había realizado el recorrido.'''

espacio = float(input("Introduzca el espacio recorrido en metros: "))
tiempo = float(input("Introduzca el tiempo en horas: "))
velocidad = float((espacio/1000)/tiempo)
print("Su coche se desplazaba a1",velocidad,"Km/h")
