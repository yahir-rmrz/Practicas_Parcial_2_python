# Importa todos los elementos del módulo tkinter
# Imports all elements from the tkinter module
from tkinter import *
# Importa messagebox para mostrar cuadros de diálogo
# Imports messagebox to display dialog boxes
from tkinter import messagebox


# Clase principal que controla la interfaz gráfica y la lógica del programa
# Main class that controls the GUI and program logic
class Principal:
    def __init__(self):
        # Crea la ventana principal / Creates the main window
        self.ven = Tk()
        self.ven.title('Programa 10 con ventanas')  # Título de la ventana / Window title
        self.ven.geometry('600x300')                # Tamaño de la ventana / Window size

        # Variables para almacenar datos / Variables to store data
        self.lista = []     # Lista de números / List of numbers
        self.aux1 = 0       # Variables auxiliares (no se usan actualmente) / Auxiliary variables (not used)
        self.aux2 = 0
        self.cont = 0

        # Llama al método que construye la interfaz / Calls the method that builds the interface
        self.inicio()

    # Método que coloca los elementos gráficos en la ventana
    # Method that places the graphical elements in the window
    def inicio(self):
        # Etiquetas y campos de entrada / Labels and entry fields
        Label(self.ven, text="Programa 10").place(x=10, y=10)
        Label(self.ven, text="Escribe un número:").place(x=10, y=50)
        self.n1 = Entry(self.ven)
        self.n1.place(x=150, y=50)

        Label(self.ven, text="Escribe otro número:").place(x=10, y=90)
        self.n2 = Entry(self.ven)
        self.n2.place(x=150, y=90)

        # Botones con funciones asociadas / Buttons with their respective functions
        Button(self.ven, text="AGREGAR", command=self.agregar).place(x=10, y=130)
        Button(self.ven, text="MAYOR", command=self.mayor).place(x=110, y=130)
        Button(self.ven, text="MENOR", command=self.menor).place(x=210, y=130)
        Button(self.ven, text="SALIR", command=self.salir).place(x=310, y=130)

        # Listbox para mostrar los elementos agregados / Listbox to show added numbers
        self.listview = Listbox(
            self.ven, height=10, width=15, bg='lightgrey', activestyle="dotbox"
        )
        self.listview.place(x=450, y=30)

        # Etiqueta para mostrar la lista actual / Label to show the current list
        self.listaElementos = Label(self.ven, text="")
        self.listaElementos.place(x=150, y=180)

        # Inicia el ciclo principal de la interfaz / Starts the GUI main loop
        self.ven.mainloop()

    # Método para agregar los números a la lista / Adds the entered numbers to the list
    def agregar(self):
        try:
            # Convierte los valores de entrada a enteros / Converts input values to integers
            a = int(self.n1.get())
            b = int(self.n2.get())

            # Agrega ambos números a la lista / Adds both numbers to the list
            self.lista.extend([a, b])

            # Inserta los valores en el Listbox / Inserts values into the Listbox
            self.listview.insert(END, a)
            self.listview.insert(END, b)

            # Limpia los campos de entrada / Clears the entry fields
            self.n1.delete(0, END)
            self.n2.delete(0, END)

            # Actualiza la etiqueta con la lista actual / Updates label with the current list
            self.listaElementos.config(text='Lista actual: ' + str(self.lista))

        except ValueError:
            # Muestra un error si el dato no es numérico / Shows error if data is not numeric
            messagebox.showerror("Error", "Algún dato no es un número / Some data is not a number")

    # Método que muestra el número mayor / Shows the largest number
    def mayor(self):
        if self.lista:
            mayor_valor = max(self.lista)
            messagebox.showinfo("Resultado", f'El número mayor es: {mayor_valor}\n(The largest number is: {mayor_valor})')
        else:
            messagebox.showerror("Error", "La lista está vacía / The list is empty")

    # Método que muestra el número menor / Shows the smallest number
    def menor(self):
        if self.lista:
            menor_valor = min(self.lista)
            messagebox.showinfo("Resultado", f'El número menor es: {menor_valor}\n(The smallest number is: {menor_valor})')
        else:
            messagebox.showerror("Error", "La lista está vacía / The list is empty")

    # Método para cerrar la ventana / Closes the window
    def salir(self):
        self.ven.destroy()


# Punto de entrada del programa / Program entry point
if __name__ == '__main__':
    Principal()
