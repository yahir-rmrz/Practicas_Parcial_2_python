from tkinter import *             # Import tkinter for GUI / Importa tkinter para la interfaz grafica
from tkinter import messagebox    # Import messagebox for alerts / Importa messagebox para mostrar alertas


class Principal():                # Define main class / Define la clase principal
    def __init__(self):           # Constructor method / Metodo constructor
        self.ven = Tk()           # Create window / Crea la ventana
        self.ven.title('Examen Caliz')    # Set window title / Establece el titulo de la ventana
        self.ven.geometry('600x300')      # Set window size / Define el tamano de la ventana
        self.lista = []           # Create empty list / Crea una lista vacia
        self.Inicio()             # Call start method / Llama al metodo de inicio

    def Inicio(self):             # Define start method / Define el metodo de inicio
        # Labels for textboxes / Etiquetas para las cajas de texto
        Label(self.ven, text="Letras minusculas:").place(x=20, y=20)   # Label for lowercase / Etiqueta para minusculas
        Label(self.ven, text="Letras MAYUSCULAS:").place(x=220, y=20)  # Label for uppercase / Etiqueta para mayusculas
        Label(self.ven, text="Numeros:").place(x=420, y=20)            # Label for numbers / Etiqueta para numeros

        # Entry boxes / Cajas de texto
        self.min = Entry(self.ven)                     # Create entry for lowercase / Crea entrada para minusculas
        self.min.place(x=20, y=40, width=150)          # Place it in window / La coloca en la ventana

        self.may = Entry(self.ven)                     # Create entry for uppercase / Crea entrada para mayusculas
        self.may.place(x=220, y=40, width=150)         # Place it in window / La coloca en la ventana

        self.num = Entry(self.ven)                     # Create entry for numbers / Crea entrada para numeros
        self.num.place(x=420, y=40, width=150)         # Place it in window / La coloca en la ventana

        # Buttons / Botones
        Button(self.ven, text="VALIDAR", command=self.validar).place(x=180, y=100)  # Validate button / Boton para validar
        Button(self.ven, text="AGREGAR", command=self.agregar).place(x=320, y=100)  # Add button / Boton para agregar

        # Listbox and counter label / Listbox y etiqueta de contador
        self.lista_visual = Listbox(self.ven, width=70)  # Create listbox / Crea un listbox
        self.lista_visual.place(x=50, y=150)             # Place it in window / Lo coloca en la ventana

        self.contador = Label(self.ven, text="Elementos: 0")  # Label to show number of elements / Etiqueta para mostrar cantidad de elementos
        self.contador.place(x=50, y=250)                     # Place it / La coloca en la ventana

        self.ven.mainloop()   # Run the window / Ejecuta la ventana principal

    def validar(self):        # Method to validate inputs / Metodo para validar las entradas
        correcto = True       # Flag variable for validation / Variable de control para validacion

        # Validate lowercase text / Validar texto en minusculas
        texto_min = self.min.get()     # Get lowercase entry / Obtiene texto de minusculas
        if not texto_min.islower() or texto_min == "":   # If not lowercase or empty / Si no es minuscula o esta vacio
            messagebox.showerror("Error", "La primera caja debe contener solo letras minusculas.")  # Show error / Muestra error
            self.min.delete(0, END)     # Clear box / Borra la caja
            correcto = False            # Mark as incorrect / Marca como incorrecto

        # Validate uppercase text / Validar texto en mayusculas
        texto_may = self.may.get()      # Get uppercase entry / Obtiene texto de mayusculas
        if not texto_may.isupper() or texto_may == "":   # If not uppercase or empty / Si no es mayuscula o esta vacio
            messagebox.showerror("Error", "La segunda caja debe contener solo letras MAYUSCULAS.")  # Show error / Muestra error
            self.may.delete(0, END)     # Clear box / Borra la caja
            correcto = False            # Mark as incorrect / Marca como incorrecto

        # Validate number text / Validar texto numerico
        texto_num = self.num.get()      # Get number entry / Obtiene texto de numeros
        if not texto_num.isdigit() or texto_num == "":   # If not number or empty / Si no es numero o esta vacio
            messagebox.showerror("Error", "La tercera caja debe contener solo numeros.")  # Show error / Muestra error
            self.num.delete(0, END)     # Clear box / Borra la caja
            correcto = False            # Mark as incorrect / Marca como incorrecto

        if correcto:                    # If all correct / Si todo es correcto
            messagebox.showinfo("Validacion exitosa", "Todas las entradas son validas.")  # Show success / Muestra mensaje exitoso

    def agregar(self):        # Method to add validated entries / Metodo para agregar las entradas validadas
        texto_min = self.min.get()   # Get lowercase / Obtiene minusculas
        texto_may = self.may.get()   # Get uppercase / Obtiene mayusculas
        texto_num = self.num.get()   # Get number / Obtiene numeros

        # Check that fields are not empty / Verifica que no esten vacios
        if texto_min and texto_may and texto_num:
            # Check they are valid types / Verifica que sean tipos correctos
            if texto_min.islower() and texto_may.isupper() and texto_num.isdigit():
                concatenado = texto_min + texto_may + texto_num   # Concatenate all / Concatena todos los textos
                self.lista.append(concatenado)                    # Add to list / Agrega a la lista
                self.lista_visual.insert(END, concatenado)        # Show in listbox / Lo muestra en el listbox
                self.contador.config(text=f"Elementos: {len(self.lista)}")  # Update count / Actualiza el contador

                # Clear all entries / Limpia todas las cajas
                self.min.delete(0, END)
                self.may.delete(0, END)
                self.num.delete(0, END)
            else:
                messagebox.showerror("Error", "Debe validar correctamente las entradas antes de agregar.")  # Show error / Muestra error
        else:
            messagebox.showerror("Error", "No puede haber campos vacios.")  # Show error if empty / Muestra error si hay vacios


if __name__ == '__main__':   # Main entry point / Punto de entrada principal
    app = Principal()         # Create app instance / Crea una instancia de la aplicacion
