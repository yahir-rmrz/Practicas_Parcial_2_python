# Importa todos los componentes del módulo tkinter
# Imports all components from the tkinter module
from tkinter import *
# Importa messagebox para mostrar mensajes emergentes
# Imports messagebox to show pop-up messages
from tkinter import messagebox


# Clase principal que gestiona la interfaz y la lógica del programa
# Main class that manages the interface and program logic
class Principal:
    # Constructor: configura la ventana principal
    # Constructor: sets up the main window
    def __init__(self):
        self.ven = Tk()                               # Crea la ventana / Creates the window
        self.ven.title('Programa 9 con ventanas')      # Título de la ventana / Window title
        self.ven.geometry('600x300')                   # Tamaño de la ventana / Window size

        # Variables principales
        # Main variables
        self.lista = []     # Lista para almacenar los números / List to store numbers
        self.aux1 = 0       # Variable auxiliar (no usada actualmente) / Auxiliary variable (not used)
        self.aux2 = 0       # Variable auxiliar para inicializar menor / Auxiliary variable for min value
        self.cont = 0       # Contador (no usado en esta versión) / Counter (not used in this version)

        # Llama al método que construye la interfaz
        # Calls the method that builds the interface
        self.inicio()

    # Método que crea los elementos de la interfaz gráfica
    # Method that creates the GUI elements
    def inicio(self):
        # Etiquetas y campos de entrada / Labels and input fields
        Label(self.ven, text="Programa 9").grid(row=1, column=2, pady=10)
        Label(self.ven, text="Escribe un número:").grid(row=3, column=1, padx=15, pady=10)
        self.n1 = Entry(self.ven)
        self.n1.grid(row=3, column=2)

        Label(self.ven, text="Escribe otro número:").grid(row=5, column=1, padx=15, pady=10)
        self.n2 = Entry(self.ven)
        self.n2.grid(row=5, column=2)

        # Botones de acción / Action buttons
        Button(self.ven, text="AGREGAR", command=self.agregar).grid(row=6, column=1, padx=10)
        Button(self.ven, text="MAYOR", command=self.mayor).grid(row=6, column=2, padx=10)
        Button(self.ven, text="MENOR", command=self.menor).grid(row=6, column=3, padx=10)
        Button(self.ven, text="SALIR", command=self.salir).grid(row=6, column=4, padx=10)

        # Listbox para mostrar los elementos agregados
        # Listbox to display added elements
        self.listview = Listbox(self.ven, height=10, width=15, bg='lightgrey', activestyle="dotbox")
        self.listview.grid(row=2, column=4, rowspan=5, padx=20)

        # Etiqueta para mostrar la lista actual
        # Label to display the current list
        self.listaElementos = Label(self.ven, text="")
        self.listaElementos.grid(row=8, column=2, pady=15)

        # Inicia el bucle principal de la ventana
        # Starts the main loop of the window
        self.ven.mainloop()

    # Método para agregar los números a la lista
    # Method to add numbers to the list
    def agregar(self):
        try:
            # Convierte los valores ingresados a enteros
            # Converts entered values to integers
            a = int(self.n1.get())
            b = int(self.n2.get())

            # Agrega ambos números a la lista
            # Adds both numbers to the list
            self.lista.extend([a, b])

            # Muestra los números en la lista visual (Listbox)
            # Displays numbers in the visual list (Listbox)
            self.listview.insert(END, a)
            self.listview.insert(END, b)

            # Limpia los campos de texto
            # Clears the input fields
            self.n1.delete(0, END)
            self.n2.delete(0, END)

            # Actualiza la etiqueta con la lista actual
            # Updates the label with the current list
            self.listaElementos.config(text=f'Lista actual: {self.lista}')

        except ValueError:
            # Muestra un error si los datos no son válidos
            # Shows an error if input data are invalid
            messagebox.showerror("Error", "Algún dato no es un número / Some input is not a number")

    # Método para mostrar el número mayor
    # Method to display the largest number
    def mayor(self):
        if self.lista:
            mayor_valor = max(self.lista)
            messagebox.showinfo("Resultado", f'El número mayor es: {mayor_valor}\n(The largest number is: {mayor_valor})')
        else:
            messagebox.showerror("Error", "La lista está vacía / The list is empty")

    # Método para mostrar el número menor
    # Method to display the smallest number
    def menor(self):
        if self.lista:
            menor_valor = min(self.lista)
            messagebox.showinfo("Resultado", f'El número menor es: {menor_valor}\n(The smallest number is: {menor_valor})')
        else:
            messagebox.showerror("Error", "La lista está vacía / The list is empty")

    # Método para cerrar la ventana
    # Method to close the window
    def salir(self):
        self.ven.destroy()


# Punto de entrada principal del programa
# Main entry point of the program
if __name__ == '__main__':
    Principal()
