import customtkinter as Ctk
from CTkMessagebox import CTkMessagebox
from tkinter import *
from PIL import ImageTk
from helpers import bind_enter_to_button
from tkinter import messagebox
import ui

Ctk.set_appearance_mode("white")
Ctk.set_default_color_theme("dark-blue")

#Creamos una funcion de login
def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror (message='Error Los campos no pueden estar vacios')
    elif usernameEntry.get() == 'admin' and passwordEntry.get() == 'admin':
        messagebox.showinfo (message=F'Bienvenido {usernameEntry.get()}')
        root.destroy()
        ui.MainWindow()
    else:
        messagebox.showerror (message='Nombre de usuario y/o password incorrectos')

#Centramos la ventana del programa, al centro de la pantalla
def center(root, width, height):
    """Centra la ventana en la pantalla"""
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")


#Creamos la ventana
root = Ctk.CTk()
#Configuramos el tamaño y ubicacion de la ventana
center(root, 950, 645)
#Configuramos el nombre de la ventana
root.title("Login System of SMS") 
#Restringimos la posibilidad de aplificar la ventana. En este caso no es necesaria esta accion.
root.resizable(False,False)


#Cargarmos como background una imagen
backgroundImage = ImageTk.PhotoImage(file='static/fondo.jpg')

#Creamos una etiqueta para poder cargar la imagen
bgLabel= Label(root, image=backgroundImage)
bgLabel.place(x=0,y=0)

#creamos una sub ventana para el sistema de login
loginFrame = Ctk.CTkFrame(root, fg_color= "white",bg_color="white")
#loginFrame.pack(pady=20, padx=60 , fill="both", expand=True)
# Establecemos la ubicacion de la ventana
loginFrame.place(x=255,y=170)

#Agregamos un logo para nuestro login
logoImage = PhotoImage (file='static/student_t.png')
logoLabel = Ctk.CTkLabel(master=loginFrame, text=None, image=logoImage,fg_color= "white")
logoLabel.grid(pady=12, padx=10)

#Importamos el icono para username
usernameImage = PhotoImage (file='static/user.png')
#Creamos el campo de usuario
usernameLabel = Ctk.CTkLabel (master=loginFrame, image=usernameImage, text=None)
usernameLabel.grid(row=1,column=0, pady=5, padx= 5)
#Creamos el campo de entrada
usernameEntry = Ctk.CTkEntry(master=usernameLabel, placeholder_text='Username', font=('Caslon', 15, 'bold'))
usernameEntry.grid(row=0, column=1, pady=5, padx= 5)

#Importamos el icono para password
passwordImage = PhotoImage (file='static/password.png')
#Creamos el campo de usuario
passwordLabel = Ctk.CTkLabel (master=loginFrame, image=passwordImage, text=None)
passwordLabel.grid(row=2,column=0, pady=5, padx= 5)
#Creamos el campo de entrada
passwordEntry = Ctk.CTkEntry(master=passwordLabel, placeholder_text='Password', font=('Caslon', 15, 'bold'))
passwordEntry.grid(row=0, column=1, pady=5, padx= 5)


#creamos un boton para realizar el login
loginButton = Ctk.CTkButton (master=loginFrame, text="Login", fg_color= "navy",
                    font=('Caslon', 15, 'bold'), cursor="hand2", command=login)
loginButton.grid(row=3, column=0, pady=10, padx= 50)
#Aplicamos al boton de login, la accion de funcionar con tecla "ENTER"
bind_enter_to_button(loginFrame, loginButton)

#creamos un botón con tilde de Recordar usuario
checkbox = Ctk.CTkCheckBox(master=loginFrame, text="Recuerdame", border_color= "navy", checkmark_color= "green2",
                        font=('Caslon', 12, 'bold'), fg_color= "navy", text_color= "navy")
checkbox.grid(row=4, column=0, pady=12, padx=10)

#Campo de olvidaste tu contraseña
forgetButton = Ctk.CTkButton (master=loginFrame, text="Olvidaste tu contraseña?", fg_color= "white",
                    font=('Caslon', 12, 'bold'), cursor="hand2", text_color="blue2", hover_color= "white",
                    text_color_disabled= "blue4")
forgetButton.grid(row=5, column=0, pady=10, padx= 50, sticky= "w")
#Aplicamos al boton de login, la accion de funcionar con tecla "ENTER"
bind_enter_to_button(loginFrame, loginButton)

root.mainloop()