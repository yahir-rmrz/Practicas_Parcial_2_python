

# Importa todos los elementos del m�dulo tkinter
# Imports all elements from the tkinter module
from tkinter import *
# Importa la librer�a messagebox para mostrar cuadros de di�logo
# Imports the messagebox library to display dialog boxes
from tkinter import messagebox


# Funci�n principal que crea la ventana
# Main function that creates the window
def ventana():
    
    # Funci�n interna que revisa el usuario y contrase�a ingresados
    # Inner function that checks the entered username and password
    def revisar():
        try:
            # Obtiene el texto ingresado en el campo "Usuario"
            # Gets the text entered in the "Usuario" field
            u = str(us.get())
            # Obtiene el texto ingresado en el campo "Password"
            # Gets the text entered in the "Password" field
            p = str(pas.get())

            # Verifica si el usuario y la contrase�a son correctos
            # Checks if username and password are correct
            if u == 'admin' and p == '1234':
                # Muestra un mensaje de �xito
                # Displays a success message
                messagebox.showinfo('Validaci�n', 'Usuario y contrase�a correctos\n(User and password correct)')
            else:
                # Muestra un mensaje de error si los datos no coinciden
                # Displays an error message if credentials are incorrect
                messagebox.showinfo('Error', 'Usuario y/o contrase�a incorrectos\n(User and/or password incorrect)')
        
        # Captura un error si ocurre al procesar los datos
        # Catches an error if something goes wrong during input processing
        except ValueError:
            messagebox.showerror('Error', 'Introduce datos v�lidos\n(Please enter valid data)')


    # Crea la ventana principal
    # Creates the main window
    ven = Tk()
    ven.title('Programa 1 con ventanas')  # T�tulo de la ventana / Window title
    ven.geometry('400x200')               # Tama�o de la ventana / Window size

    # Etiqueta y campo de entrada para el usuario
    # Label and entry for username
    Label(ven, text='Usuario:').pack(pady=10)
    us = Entry(ven)
    us.pack(pady=3)

    # Etiqueta y campo de entrada para la contrase�a
    # Label and entry for password
    Label(ven, text='Contrase�a:').pack(pady=10)
    pas = Entry(ven, show='*')  # Se ocultan los caracteres del password
    pas.pack(pady=3)

    # Bot�n para ejecutar la validaci�n
    # Button to execute the validation
    Button(ven, text='Aceptar', command=revisar).pack(pady=10)

    # Inicia el bucle principal de la ventana
    # Starts the main loop of the window
    ven.mainloop()


# Verifica que el script se ejecute directamente (no importado)
# Checks that the script is being run directly (not imported)
if __name__ == '__main__':
    ventana()
