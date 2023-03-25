from tkinter import *
from tkinter import ttk #Widget extendidos
import database as db
import helpers
from tkinter.messagebox import askokcancel, WARNING

# mixin, para centrar la ventana del programa, al centro de la pantalla
class CenterWidgetMixin:
    def center (self):
        """
        Centra la ventana en la pantalla
        "WIDTHxHEIGTH+OFFSET_X+OFFSET_Y"
        de modo automatico
        w: ancho de la ventana de la aplicacion
        h: alto de la ventana de la aplicacion
        ws: ancho del monitor
        hs: altura del monitor
        """       
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws/2 - w/2)
        y = int(hs/2 - h/2)
        self.geometry (f"{w}x{h}+{x}+{y}")

#Ventana de creacion de Alumnos
class CreateClientWindow(Toplevel, CenterWidgetMixin):
    def __init__ (self, parent):#quien es el padre de la ventana
        super().__init__(parent)#este es el padre de la ventana
        self.title("Crear alumno")
        self.build()
        self.center()
        #Obligar al usuario a interactuar con la subventana:
        self.transient(parent)
        self.grab_set()
        
        
    def build (self):
        """
        Constructor de la ventana para agregar un nuevo alumno
        """        
        frame = Frame(self)
        frame.pack(padx=20, pady=10)
        #Nombre de los campos:
        Label(frame, text="DNI (2 ints y 1 upper char)").grid(row=0, column=0)
        Label(frame, text="Nombre (2 ints y 30 char)").grid(row=0, column=1)
        Label(frame, text="Apellido (2 ints y 30 char)").grid(row=0, column=2)
        Label(frame, text="Nota primer semestre (2 ints)").grid(row=0, column=3)
        Label(frame, text="Nota segundo semestre (2 ints)").grid(row=0, column=4)
        
        #Creamos los campos de texto para ingresar los datos:
        dni = Entry(frame)
        dni.grid(row=1, column=0)
        #Configuramos un evento para validar el dni:
        dni.bind('<KeyRelease>', lambda event: self.validate(event, 0))
        nombre = Entry(frame)
        nombre.grid(row=1, column=1)
        #Configuramos un evento para validar el nombre:
        nombre.bind('<KeyRelease>', lambda event: self.validate(event,1))
        apellido = Entry(frame)
        apellido.grid(row=1, column=2)
        #Configuramos un evento para validar el apellido:
        apellido.bind('<KeyRelease>', lambda event: self.validate(event,2))
        #Configuramos un evento para validar "Nota primer semestre":
        nombre.bind('<KeyRelease>', lambda event: self.validate(event,3))
        nota_1er_semestre = Entry(frame)
        nota_1er_semestre.grid(row=1, column=3)
        #Configuramos un evento para validar "Nota segundo semestre":
        nombre.bind('<KeyRelease>', lambda event: self.validate(event,4))
        nota_2do_semestre = Entry(frame)
        nota_2do_semestre.grid(row=1, column=4)
        
        
        frame = Frame(self)
        frame.pack(pady=10)
        
        crear = Button(frame, text="Crear", command=self.create_student)
        crear.configure(state=DISABLED)
        crear.grid(row=0, column=0)
        Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)
        
        #Lista de validaciones:
        self.validaciones = [0, 0]  # False, False, False
        self.crear = crear
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.nota_1er_semestre = nota_1er_semestre
        self.nota_2do_semestre = nota_2do_semestre
        
        
        
        
    def create_student(self):
        self.master.treeview.insert(
            parent= "", index= "end", iid= self.dni.get(),
            values= (self.dni.get(), self.nombre.get(), self.apellido.get(), self.nota_1er_semestre.get(), self.nota_2do_semestre.get()))
        db.Alumnos.crear(self.dni.get(), self.nombre.get(), self.apellido.get(), self.nota_1er_semestre.get(), self.nota_2do_semestre.get())
        self.close()
    
    def close(self):
        self.destroy()
        self.update ()
    
    def validate(self, event, index):
        """
        Valida los datos ingresados en los campos
        Verde = OK
        Red = "ERROR" formato incorrecto
        Args:
            event (_type_): _description_
            index (_type_): _description_
        """        
        valor = event.widget.get()
        # Validar el dni si es el primer campo o textual para los otros dos
        valido = helpers.dni_valido(valor, db.Alumnos.lista) if index == 0 \
            else (valor.isalpha() and len(valor) >= 2 and len(valor) <= 30)
        event.widget.configure({"bg": "Green" if valido else "Red"})
        #Cambiar estado del boton en base a las validaciones:
        self.validaciones[index] = valido
        self.crear.config(state=NORMAL if self.validaciones == [1, 1, 1] #TRUE, TRUE, TRUE
                            else DISABLED)

#Ventana de edicion de Alumnos
class EditClientWindow(Toplevel, CenterWidgetMixin):
    def __init__ (self, parent):#quien es el padre de la ventana
        super().__init__(parent)#este es el padre de la ventana
        self.title("Actualizar alumno")
        self.build()
        self.center()
        #Obligar al usuario a interactuar con la subventana:
        self.transient(parent)
        self.grab_set()
        
        
    def build (self):
        """
        Constructor de la ventana para agregar un nuevo alumno
        """        
        frame = Frame(self)
        frame.pack(padx=10, pady=5)
        #Nombre de los campos:
        Label(frame, text="DNI (No editable)").grid(row=0, column=0)
        Label(frame, text="Nombre (2 ints y 30 char)").grid(row=0, column=1)
        Label(frame, text="Apellido (2 ints y 30 char)").grid(row=0, column=2)
        Label(frame, text="Nota 1er semestre (2 ints)").grid(row=0, column=3)
        Label(frame, text="Nota 2do semestre (2 ints)").grid(row=0, column=4)
        
        #Creamos los campos de texto para ingresar los datos:
        dni = Entry(frame)
        dni.grid(row=1, column=0)
        #Configuramos un evento para validar el dni:
        nombre = Entry(frame)
        nombre.grid(row=1, column=1)
        #Configuramos un evento para validar el nombre:
        nombre.bind('<KeyRelease>', lambda event: self.validate(event,0))
        apellido = Entry(frame)
        apellido.grid(row=1, column=2)
        #Configuramos un evento para validar el apellido:
        apellido.bind('<KeyRelease>', lambda event: self.validate(event,1))
        #Configuramos un evento para validar "Nota primer semestre":
        nombre.bind('<KeyRelease>', lambda event: self.validate(event,2))
        nota_1er_semestre = Entry(frame)
        nota_1er_semestre.grid(row=1, column=3)
        #Configuramos un evento para validar "Nota segundo semestre":
        nombre.bind('<KeyRelease>', lambda event: self.validate(event,3))
        nota_2do_semestre = Entry(frame)
        nota_2do_semestre.grid(row=1, column=4)
        
        
        alumno = self.master.treeview.focus()
        campos = self.master.treeview.item(alumno, "values")
        dni.insert(0, campos[0])
        dni.config(state=DISABLED)
        nombre.insert(0, campos[1])
        apellido.insert(0, campos[2])
        nota_1er_semestre.insert(0, campos[3])
        nota_2do_semestre.insert(0, campos[4])
        
        
        
        frame = Frame(self)
        frame.pack(pady=10)
        
        actualizar = Button(frame, text="Actualizar", command=self.edit_client)
        actualizar.grid(row=0, column=0)
        Button(frame, text="cancelar", command=self.close).grid(row=0, column=1)
        
        
        #TODO
        #Lista de validaciones:
        self.validaciones = [1, 1, 1]  # False, False, False 
        self.actualizar = actualizar
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.nota_1er_semestre = nota_1er_semestre
        self.nota_2do_semestre = nota_2do_semestre
        
        
        
    def edit_client(self):
        alumno = self.master.treeview.focus()
        self.master.treeview.item(alumno, values=(self.dni.get(), self.nombre.get(), self.apellido.get(), self.nota_1er_semestre.get(), self.nota_2do_semestre.get()))
        db.Alumnos.modificar(self.dni.get(), self.nombre.get(), self.apellido.get(), self.nota_1er_semestre.get(), self.nota_2do_semestre.get())
        self.close()
        
        
        
    def close(self):
        self.destroy()
        self.update ()
    
    def validate(self, event, index):
        """
        Valida los datos ingresados en los campos
        Verde = OK
        Red = "ERROR" formato incorrecto
        Args:
            event (_type_): _description_
            index (_type_): _description_
        """        
        valor = event.widget.get()
        # Validar el dni si es el primer campo o textual para los otros dos
        valido = (valor.isalpha() and len(valor) >= 2 and len(valor) <= 30)
        event.widget.configure({"bg": "Green" if valido else "Red"})
        #Cambiar estado del boton en base a las validaciones:
        self.validaciones[index] = valido
        self.actualizar.config(state=NORMAL if self.validaciones == [1, 1] else DISABLED)

#creamos una clase, de nombre ventana principal. En lugar de un root
#vamos a heredar de tkinter
class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self):
        #llamamos al constructor de la clase Tk:
        super().__init__()
        self.title ("Gestor de alumnos")
        self.build()
        self.center()
        
        
    def build (self):
        """
        Crea la interfaz principal de la aplicacion
        Define la estructura de la interfaz
        treeview: vista en arbol, para hacer un cuadro
        """
        frame = Frame(self)
        frame.pack()
        
        treeview = ttk.Treeview(frame)#lo creamos en el marco
        treeview['columns'] = ('DNI','Nombre', 'Apellido', 'Nota 1er Semestre', 'Nota 2do Semestre', 'Promedio')
        
        
        #Creamos las columnas
        treeview.column("#0", width=0, stretch=NO)#la primera columna que no contiene datos, la sacamos
        treeview.column("DNI", width=80, anchor=CENTER, )
        treeview.column("Nombre", width=100, anchor=CENTER)
        treeview.column("Apellido", width=100, anchor=CENTER)
        treeview.column("Nota 1er Semestre", width=120, anchor=CENTER)
        treeview.column("Nota 2do Semestre", width=120, anchor=CENTER)
        treeview.column("Promedio", width=60, anchor=CENTER)
        #Nombre de las columnas
        treeview.heading("DNI", text="DNI", anchor=CENTER)
        treeview.heading("Nombre", text="Nombre", anchor=CENTER)
        treeview.heading("Apellido", text="Apellido", anchor=CENTER)
        treeview.heading("Nota 1er Semestre", text="Nota 1er Semestre", anchor=CENTER)
        treeview.heading("Nota 2do Semestre", text="Nota 2do Semestre", anchor=CENTER)
        treeview.heading("Promedio", text="Promedio", anchor=CENTER)
        
        #Creamos una scrollbar
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)#a la derecha rellenada verticalmente "y"
        treeview["yscrollcommand"] = scrollbar.set
        
        #improtamos la base de datos de los Alumnos
        for alumno in db.Alumnos.lista:
            treeview.insert(
                parent= "", index= "end", iid= alumno.dni,
                values= (alumno.dni, alumno.nombre, alumno.apellido, alumno.nota_1er_semestre, alumno.nota_2do_semestre))
        
        treeview.pack()
        
        #Creamos los botones para crear, editar y eliminar Alumnos
        #Para eso creamos un frame
        frame = Frame(self)
        frame.pack(pady=20)
        #Creamos individualmente los botones
        Button(frame, text="Crear", command=self.create).grid(row=0, column=0)
        Button(frame, text="Modificar", command=self.edit).grid(row=0, column=1)
        Button(frame, text="Borrar", command=self.delete).grid(row=0, column=2)
        
        self.treeview = treeview
        
    def delete (self):
        """
        Funcion para eliminar un alumno
        import: WARNING ICON
        focus, marca la posicion en el registro
        """
        alumno = self.treeview.focus()#hace focus (pinta en azul el registro)
        if alumno:
            campos = self.treeview.item(alumno, "values")
            confirmar = askokcancel(
                title="Confirmar borrado",
                message=f"Borrar {campos[1]} {campos [2]}?",
                icon=WARNING)
            if confirmar:
                self.treeview.delete(alumno)
                db.Alumnos.borrar(campos[0])
    
    
    def create (self):
        CreateClientWindow(self)
        
    
    def edit (self):
        if self.treeview.focus():
            EditClientWindow(self)
            


#Para poder ejecutar/iniciar una instancia de la aplicacion:
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
#antes lo haciamos en Tk, ahora lo hacemos en la instacia de la ventana principal




