
# Importa todos los elementos del m�dulo tkinter
# Imports all elements from the tkinter module
from tkinter import *
# Importa la librer�a messagebox para mostrar cuadros de di�logo
# Imports messagebox to display dialog boxes
from tkinter import messagebox


# Clase que crea una ventana con validaci�n de usuario y contrase�a
# Class that creates a window with username and password validation
class Ventana:

    # Constructor de la clase: crea la ventana principal
    # Class constructor: creates the main window
    def __init__(self):
        self.ven = Tk()                             # Crea la ventana principal / Creates the main window
        self.ven.title('Programa 1 con ventanas')   # T�tulo de la ventana / Window title
        self.ven.geometry('400x200')                # Tama�o de la ventana / Window size
        self.inicio()                               # Llama al m�todo que agrega los elementos / Calls the setup method

    # M�todo que construye los elementos gr�ficos (entradas, etiquetas, botones)
    # Method that builds the graphical elements (entries, labels, buttons)
    def inicio(self):
        Label(self.ven, text='Usuario:').pack(pady=10)   # Etiqueta para el nombre de usuario / Label for username
        self.us = Entry(self.ven)                        # Campo de entrada para el usuario / Input field for username
        self.us.pack(pady=3)

        Label(self.ven, text='Contrase�a:').pack(pady=10)  # Etiqueta para la contrase�a / Label for password
        self.pas = Entry(self.ven, show='*')               # Campo de contrase�a (oculta el texto) / Password field (hides text)
        self.pas.pack(pady=3)

        # Bot�n que llama al m�todo revisar cuando se presiona
        # Button that calls the 'revisar' method when clicked
        Button(self.ven, text='Aceptar', command=self.revisar).pack(pady=10)

        # Inicia el bucle principal de la interfaz gr�fica
        # Starts the main loop of the GUI
        self.ven.mainloop()

    # M�todo que valida los datos ingresados
    # Method that validates entered data
    def revisar(self):
        try:
            # Obtiene los valores de los campos de texto
            # Gets the values from the text fields
            u = str(self.us.get())
            p = str(self.pas.get())

            # Verifica si el usuario y la contrase�a son correctos
            # Checks if username and password are correct
            if u == 'admin' and p == '1234':
                messagebox.showinfo('Validaci�n', 'Usuario y contrase�a correctos\n(User and password correct)')
            else:
                messagebox.showwarning('Error', 'Usuario y/o contrase�a incorrectos\n(User and/or password incorrect)')
        
        # Captura errores de tipo o valor
        # Catches value or type errors
        except ValueError:
            messagebox.showerror('Error', 'Introduce datos v�lidos\n(Please enter valid data)')


# Punto de entrada del programa: crea la ventana al ejecutar el script directamente
# Entry point of the program: creates the window when the script is run directly
if __name__ == '__main__':
    app = Ventana()
