#Este fichero controla los datos y provee una interfaz para crear
#y borrar
import csv
import config


class Alumno:
    def __init__(self, dni, nombre, apellido, nota_1er_semestre, nota_2do_semestre, averange):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.nota_1er_semestre = nota_1er_semestre
        self.nota_2do_semestre = nota_2do_semestre
        self.averange = averange
    #funcion especial STR
    def __str__(self):
        return f"({self.dni}) {self.nombre} {self.apellido}{self.nota_1er_semestre}{self.nota_2do_semestre}{self.averange}"


class Alumnos:
    #Definimos el contenido de la base de datos creando la clase Alumnos
    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for dni, nombre, apellido, nota_1er_semestre, nota_2do_semestre, averange in reader:
            alumno = Alumno(dni, nombre, apellido, nota_1er_semestre, nota_2do_semestre, averange)
            lista.append(alumno)
    
    @staticmethod
    def buscar (dni):
        for alumno in Alumnos.lista:
            if alumno.dni == dni:
                return alumno
    
    
    @staticmethod
    def crear (dni, nombre, apellido, nota_1er_semestre, nota_2do_semestre):
        alumno = Alumno(dni, nombre, apellido, nota_1er_semestre, nota_2do_semestre)
        Alumnos.lista.append(Alumno)
        Alumnos.guardar()
        return alumno
    
    @staticmethod
    def modificar (dni, nombre, apellido, nota_1er_semestre, nota_2do_semestre):
        for indice, alumno in enumerate(Alumnos.lista):
            if alumno.dni == dni:
                Alumnos.lista[indice].nombre = nombre
                Alumnos.lista[indice].apellido = apellido
                Alumnos.lista[indice].nota_1er_semestre = nota_1er_semestre
                Alumnos.lista[indice].nota_2do_semestre = nota_2do_semestre
                Alumnos.guardar()
                return Alumnos.lista[indice]
            
    @staticmethod
    def borrar (dni):
        for indice, alumno in enumerate(Alumnos.lista):
            if alumno.dni == dni:
                alumno = Alumnos.lista.pop(indice)
                Alumnos.guardar()
                return alumno
    #TODO 
    @staticmethod    
    def average (nota_1er_semestre, nota_2do_semestre):
        average = Alumno(nota_1er_semestre + nota_2do_semestre) / 2
        Alumnos.lista.append(Alumno)
        Alumnos.guardar()
        return average
    
    @staticmethod
    def guardar ():
        with open (config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for alumno in Alumnos.lista:
                writer.writerow((alumno.dni, alumno.nombre, alumno.apellido, alumno.nota_1er_semestre, alumno.nota_2do_semestre, alumno.average))




















