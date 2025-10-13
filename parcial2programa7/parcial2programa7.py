# Importa todos los elementos del m�dulo tkinter
# Imports all elements from the tkinter module
from tkinter import *
# Importa messagebox para mostrar cuadros de di�logo
# Imports messagebox to display dialog boxes
from tkinter import messagebox


# Clase principal que controla la interfaz gr�fica y la l�gica del programa
# Main class that controls the GUI and program logic
class Principal:
    def __init__(self):
        # Crea la ventana principal / Creates the main window
        self.ven = Tk()
        self.ven.title('Programa 10 con ventanas')  # T�tulo de la ventana / Window title
        self.ven.geometry('600x300')                # Tama�o de la ventana / Window size

        # Variables para almacenar datos / Variables to store data
        self.lista = []     # Lista de n�meros / List of numbers
        self.aux1 = 0       # Variables auxiliares (no se usan actualmente) / Auxiliary variables (not used)
        self.aux2 = 0
        self.cont = 0

        # Llama al m�todo que construye la interfaz / Calls the method that builds the interface
        self.inicio()

    # M�todo que coloca los elementos gr�ficos en la ventana
    # Method that places the graphical elements in the window
    def inicio(self):
        # Etiquetas y campos de entrada / Labels and entry fields
        Label(self.ven, text="Programa 10").place(x=10, y=10)
        Label(self.ven, text="Escribe un n�mero:").place(x=10, y=50)
        self.n1 = Entry(self.ven)
        self.n1.place(x=150, y=50)

        Label(self.ven, text="Escribe otro n�mero:").place(x=10, y=90)
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

    # M�todo para agregar los n�meros a la lista / Adds the entered numbers to the list
    def agregar(self):
        try:
            # Convierte los valores de entrada a enteros / Converts input values to integers
            a = int(self.n1.get())
            b = int(self.n2.get())

            # Agrega ambos n�meros a la lista / Adds both numbers to the list
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
            # Muestra un error si el dato no es num�rico / Shows error if data is not numeric
            messagebox.showerror("Error", "Alg�n dato no es un n�mero / Some data is not a number")

    # M�todo que muestra el n�mero mayor / Shows the largest number
    def mayor(self):
        if self.lista:
            mayor_valor = max(self.lista)
            messagebox.showinfo("Resultado", f'El n�mero mayor es: {mayor_valor}\n(The largest number is: {mayor_valor})')
        else:
            messagebox.showerror("Error", "La lista est� vac�a / The list is empty")

    # M�todo que muestra el n�mero menor / Shows the smallest number
    def menor(self):
        if self.lista:
            menor_valor = min(self.lista)
            messagebox.showinfo("Resultado", f'El n�mero menor es: {menor_valor}\n(The smallest number is: {menor_valor})')
        else:
            messagebox.showerror("Error", "La lista est� vac�a / The list is empty")

    # M�todo para cerrar la ventana / Closes the window
    def salir(self):
        self.ven.destroy()


# Punto de entrada del programa / Program entry point
if __name__ == '__main__':
    Principal()
