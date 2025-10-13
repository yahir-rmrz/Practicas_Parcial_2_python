import tkinter as tk                     # EN: Import Tkinter library for GUI | ES: Importar la librería Tkinter para interfaz gráfica
from tkinter import messagebox, simpledialog   # EN: Import dialog boxes and messages | ES: Importar cuadros de diálogo y mensajes

lista2 = []  # EN: This list will store all people with their grades | ES: Esta lista guardará todas las personas con sus calificaciones


def pedir_datos():
    # EN: Ask for the name of the person | ES: Pedir el nombre de la persona
    nom = simpledialog.askstring('Entrada', 'Escribe un nombre:')

    if not nom:  # EN: If no name is entered, exit the function | ES: Si no se escribe nombre, salir de la función
        return

    # EN: Ask for 3 grades and convert them to integers | ES: Pedir 3 calificaciones y convertirlas a enteros
    try:
        c1 = int(simpledialog.askstring('Entrada', 'Escribe una calificacion:'))
        c2 = int(simpledialog.askstring('Entrada', 'Escribe una calificacion:'))
        c3 = int(simpledialog.askstring('Entrada', 'Escribe una calificacion:'))
    except:
        # EN: If the user types something that is not a number, show an error | ES: Si el usuario escribe algo que no es número, mostrar error
        messagebox.showerror('Error', 'Debes escribir numeros enteros')
        return

    # EN: Sort grades from highest to lowest | ES: Ordenar las calificaciones de mayor a menor
    calificaciones = sorted([c1, c2, c3], reverse=True)

    # EN: Create a list with name and grades | ES: Crear una lista con el nombre y las calificaciones
    lista1 = [nom] + calificaciones

    # EN: Add the list to the global list of people | ES: Agregar la lista a la lista global de personas
    lista2.append(lista1)

    # EN: Show a message that the record was added | ES: Mostrar un mensaje de que se agregó el registro
    messagebox.showinfo('Registro agregado', f'Se agrego:\n{lista1}')


def mostrar_lista():
    # EN: If the list is empty, show a message | ES: Si la lista está vacía, mostrar mensaje
    if not lista2:
        messagebox.showinfo('Lista', 'No hay datos todavia.')
    else:
        # EN: Convert the list into text to display | ES: Convertir la lista en texto para mostrar
        texto = '\n'.join([str(p) for p in lista2])
        messagebox.showinfo('Lista de Personas', texto)


def salir():
    # EN: Close the program window | ES: Cerrar la ventana del programa
    root.destroy()


# ---------- MAIN WINDOW / VENTANA PRINCIPAL ----------
root = tk.Tk()                           # EN: Create the main window | ES: Crear la ventana principal
root.title('Registro de Calificaciones') # EN: Set the window title | ES: Poner título a la ventana
root.geometry('300x200')                 # EN: Define window size | ES: Definir el tamaño de la ventana

# ---------- BUTTONS / BOTONES ----------
btn_agregar = tk.Button(root, text='Agregar Persona', command=pedir_datos, width=20)  # EN: Button to add a person | ES: Botón para agregar persona
btn_agregar.pack(pady=10)  # EN: Place button with vertical margin | ES: Colocar el botón con margen vertical

btn_mostrar = tk.Button(root, text='Mostrar Lista', command=mostrar_lista, width=20)  # EN: Button to show all data | ES: Botón para mostrar todos los datos
btn_mostrar.pack(pady=10)

btn_salir = tk.Button(root, text='Salir', command=salir, width=20)  # EN: Button to exit | ES: Botón para salir
btn_salir.pack(pady=10)

# ---------- LOOP / BUCLE PRINCIPAL ----------
root.mainloop()  # EN: Start the window loop to keep program running | ES: Iniciar el bucle de la ventana para mantener el programa abierto
