#repaso examen
from tkinter import *
from tkinter import messagebox


class Principal:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Programa con Tkinter")
        self.ventana.geometry("400x300")

        # Lista para almacenar los datos ingresados
        self.lista = []

        self.inicio()

    def inicio(self):
        Label(self.ventana, text="Programa Python con Tkinter").place(x=100, y=20)
        Label(self.ventana, text="Escribe un dato:").place(x=50, y=50)

        self.dato = Entry(self.ventana)
        self.dato.place(x=150, y=50, width=150)

        Button(self.ventana, text="VALIDAR", command=self.validar_datos).place(x=150, y=90, width=150)

        self.mostrar = Label(self.ventana, text="Esperando datos...")
        self.mostrar.place(x=20, y=130)

        Button(self.ventana, text="SALIR", command=self.ventana.destroy).place(x=150, y=260, width=150)

        self.ventana.mainloop()

    def validar_datos(self):
        val = self.dato.get().strip()  # Elimina espacios
        if val:
            self.revisar(val)
            self.lista.append(val)
            self.dato.delete(0, END)
            self.mostrar.config(text=f"Datos ingresados: {self.lista}")
        else:
            messagebox.showerror("Error", "La caja está vacía")

    def revisar(self, v):
        print(f"Valor recibido: {v}")  # Solo muestra en consola


if __name__ == '__main__':
    app = Principal()
