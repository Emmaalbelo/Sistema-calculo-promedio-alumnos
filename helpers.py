#Este fichero contiene funciones auxiliares de uso general comunes

import re
import os
import platform


def limpiar_pantalla():
    """
    Function: Limpia la pantalla, 
    identificando el sistema operativo
    """    
    os.system ('cls') if platform.system() == "Windows" else os.system("clear")

def leer_texto(longitud_min=0,longitud_max=100,mensaje=None):
    print (mensaje) if mensaje else None
    while True:
        texto= input("> ")
        if len(texto)>=longitud_min and len(texto)<=longitud_max:
            return texto

#Validación del campo DNI
def dni_valido(dni, lista):
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print ("DNI incorrecto, debe cumplir el formato.")
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print ("DNI ya registrado.")
            return False
    return True

#Calculo de promedio de los estudiantes
def calculate_average(nota_1er_semestre, nota_2do_semestre):
    avg = sum([nota_1er_semestre, nota_2do_semestre]) / 2
    return avg



