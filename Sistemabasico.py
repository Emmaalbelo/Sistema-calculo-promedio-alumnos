print ('Sistema para calcular el promedio de un alumno')
name = input ("cual es tu nombre?: ")

matematicas = float (input (f"{name} cual es tu calificacion en matematica?: "))
quimica = float (input (f"{name} cual es tu calificacion en quimica? "))
biologia = float (input (f"{name} cual es tu calificacion en biologia?: "))
promedio = (matematicas + quimica + biologia) / 3
if promedio >= 6:
    print (f'felicitaciones, aprobaste {name} "APROBASTE" con un promedio de: ', promedio)
    print (f'felicitaciones, aprobaste {name} "APROBASTE" con un promedio de: ', round (promedio,2))
else:
    print (f'Eres un fracaso {name}, reprobaste con: ', promedio)
    print (f'Eres un fracaso {name}, reprobaste con: ', round (promedio,2))

print ("Fin.")
