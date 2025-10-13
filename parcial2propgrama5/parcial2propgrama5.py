from tkinter import *
from tkinter import messagebox

# Clase principal de la aplicación
# Main application class
class principal():
    def _init_(self):
        # Crear ventana principal
        # Create main window
        self.ven = Tk()
        self.ven.title('Programa 5 con ventana')
        self.ven.geometry('600x300')
        
        # Lista para guardar los promedios individuales
        # List to store individual averages
        self.lista = []
        
        # Llamamos al método que arma la interfaz
        # Call method that builds the UI
        self.inicio()

    # Función para sumar todos los elementos de la lista
    # Function to sum all elements in the list
    def sumar(self):
        s = 0
        for i in self.lista:
            s += i
        return s

    # Función para calcular el promedio de 4 números ingresados
    # Function to calculate the average of 4 input numbers
    def promediar(self):
        try:
            # Obtener valores de las cajas de texto
            # Get values from entry boxes
            a = float(self.n1.get())
            b = float(self.n2.get())
            c = float(self.n3.get())
            d = float(self.n4.get())

            # Calcular promedio individual
            # Calculate individual average
            pro = (a + b + c + d) / 4

            # Mostrar promedio individual
            # Show individual average
            self.l6.config(text=str(pro))

            # Guardar promedio en la lista
            # Store average in the list
            self.lista.append(pro)

            # Mostrar lista de promedios
            # Show list of averages
            self.l7.config(text=str(self.lista))

            # Limpiar entradas
            # Clear entry boxes
            self.n1.delete(0, END)
            self.n2.delete(0, END)
            self.n3.delete(0, END)
            self.n4.delete(0, END)

            # Calcular promedio general si hay elementos
            # Calculate general average if list has elements
            if len(self.lista) > 0:
                suma = self.sumar()
                p = suma / len(self.lista)
                self.l8.config(text=f'Promedio general: {str(p)}')

        except ValueError:
            # Error si algún dato no es número
            # Error if any value is not a number
            messagebox.showerror("Error", "Algún dato no es número")
            self.n1.delete(0, END)
            self.n2.delete(0, END)
            self.n3.delete(0, END)
            self.n4.delete(0, END)

    # Función para cerrar la ventana
    # Function to close the window
    def salir(self):
        self.ven.destroy()

    # Función que crea y posiciona todos los widgets en la ventana
    # Function that creates and places all widgets in the window
    def inicio(self):
        # Etiquetas y entradas (Labels and entries)
        Label(self.ven, text="Escribe un número").place(y=10, x=20)
        Label(self.ven, text="Escribe un número").place(y=50, x=20)
        Label(self.ven, text="Escribe un número").place(y=90, x=20)
        Label(self.ven, text="Escribe un número").place(y=130, x=20)

        self.n1 = Entry(self.ven)
        self.n1.place(y=10, x=130)

        self.n2 = Entry(self.ven)
        self.n2.place(y=50, x=130)

        self.n3 = Entry(self.ven)
        self.n3.place(y=90, x=130)

        self.n4 = Entry(self.ven)
        self.n4.place(y=130, x=130)

        # Etiqueta para promedio individual (individual avg)
        Label(self.ven, text="Promedio").place(y=160, x=130)
        self.l6 = Label(self.ven, text="0.0")
        self.l6.place(y=160, x=200)

        # Botón para calcular el promedio individual
        # Button to calculate the individual average
        Button(self.ven, text="Promedio", command=self.promediar).place(y=50, x=300)
        
        # Botón para salir
        # Button to exit
        Button(self.ven, text="Salir", command=self.salir).place(y=90, x=300)

        # Etiqueta para mostrar lista de promedios
        # Label to display list of averages
        self.l7 = Label(self.ven, text="[]")
        self.l7.place(y=190, x=200)

        # Etiqueta para promedio general
        # Label for general average
        self.l8 = Label(self.ven, text="Promedio general: 0.0")
        self.l8.place(y=220, x=150)

        # Iniciar la ventana
        # Start the window loop
        self.ven.mainloop()


# Punto de entrada del programa
# Program entry point
if _name_ == '_main_':
    app = principal()
