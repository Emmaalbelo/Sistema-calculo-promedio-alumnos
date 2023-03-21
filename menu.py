#La interfaz de la aplicación
import os
import helpers
import database as db




def inciar():
    while True:
        helpers.limpiar_pantalla()
        #os.system('cls')
        
        print ("==========================")
        print ("Bienvenido a la aplicación")
        print ("==========================")
        print ("[1] Listar los Alumnos")
        print ("[2] Buscar un alumno")
        print ("[3] Añadir un alumno")
        print ("[4] Modificar un alumno")
        print ("[5] Borrar un alumno")
        print ("[6] Cerrar el gestor")
        print ("==========================")
        
        opcion = input ('> ')
        helpers.limpiar_pantalla()
        #os.system('cls')
        
        if opcion == '1':
            print ("Listando los Alumnos...\n")
            for alumno in db.Alumnos.lista:
                print (alumno)
            
            
        if opcion == '2':
            print ("buscando un alumno...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
            alumno = db.Alumnos.buscar(dni)
            print (alumno) if alumno else print ("alumno no encontrado.")
            
        if opcion == '3':
            print ("Añadiendo un alumno...\n")
            dni = None
            while True:
                dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
                if helpers.dni_valido(dni, db.Alumnos.lista):
                    break
            nombre = helpers.leer_texto(2, 30, "Nombre (2 y 30 char)").capitalize()
            apellido = helpers.leer_texto(2, 30, "Apellido (2 y 30 char)").capitalize()
            db.Alumnos.crear(dni, nombre, apellido)
            print ("alumno añadido correctamente.")
            
        if opcion == '4':
            print ("Modificando un alumno...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
            alumno = db.Alumnos.buscar(dni)
            if alumno:
                nombre = helpers.leer_texto (
                    2, 30, f"Nombre (2 y 30 char) [{alumno.nombre}]").capitalize()
                apellido = helpers.leer_texto(
                    2, 30, f"Apellido (2 y 30 char)[{alumno.apellido}]").capitalize()
            db.Alumnos.modificar(alumno.dni, nombre, apellido)
            print ("alumno modificado correctamente")
        else:
            print ("alumno no encontrado")
            
            
        if opcion == '5':
            print ("Borrando un alumno...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
            print ("alumno borrado correctamente") if db.Alumnos.borrar(
                dni) else print ("alumno no encontrado")
            
            
            
        if opcion == '6':
            print ("Cerrando el gestor...\n")
            break
        
        input ("\nPresione cualquier tecla para continuar...")
        
        
        
