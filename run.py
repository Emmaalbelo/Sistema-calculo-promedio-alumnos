#Este es el fichero principal. El mismo se encarga de ejecutar 
# el programa.
import sys
import ui
import menu

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        menu.inciar()
    else:
        app = ui.MainWindow()
        app.mainloop()
        