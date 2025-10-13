# Importa la clase 'validacion' desde el archivo validaciones.py
# Imports the 'validacion' class from the file validaciones.py
from validaciones import validacion

# Crea una instancia de la clase validacion y la guarda en la variable 'val'
# Creates an instance of the 'validacion' class and stores it in 'val'
val = validacion()


# Define la clase principal que gestionará las calificaciones
# Defines the main class that will handle the grades
class principal():
    # Método constructor: se ejecuta al crear un objeto de la clase
    # Constructor method: runs when an object of the class is created
    def __init__(self):
        # Crea una lista vacía para almacenar calificaciones
        # Creates an empty list to store grades
        self.lista = []
        # Inicializa un contador de calificaciones
        # Initializes a counter for the number of grades
        self.num = 0
        # Variable para almacenar temporalmente la calificación ingresada
        # Variable to temporarily store the entered grade
        self.a = ""
    
    # Método principal que pide al usuario las calificaciones
    # Main method that asks the user for grades
    def inicio(self):
        # Solicita una calificación al usuario
        # Asks the user to input a grade
        self.a = input('Escribe una calificación \n')

        # Verifica si la entrada es un número válido usando el método de validación
        # Checks if the input is a valid number using the validation method
        if val.validarnumeros(self.a):
            # Incrementa el contador de calificaciones
            # Increments the grade counter
            self.num += 1

            # Convierte la entrada a entero y la agrega a la lista
            # Converts the input to integer and adds it to the list
            self.lista.append(int(self.a))

            # Si ya se ingresaron 5 calificaciones, las muestra en pantalla
            # If 5 grades have been entered, prints them
            if self.num >= 5:
                print(self.lista)
            # Si no, vuelve a pedir otra calificación
            # Otherwise, asks for another grade
            else:
                self.inicio()
        else:
            # Muestra un mensaje si la entrada no es numérica
            # Displays a message if the input is not a number
            print('No es un número.')
            # Llama nuevamente al método para volver a intentar
            # Calls the method again to retry
            self.inicio()


# Verifica que el script se ejecute directamente (no importado)
# Checks that the script is being run directly (not imported)
if __name__ == '__main__':
    # Crea una instancia de la clase principal
    # Creates an instance of the main class
    app = principal()

    # Llama al método inicio para comenzar el programa
    # Calls the 'inicio' method to start the program
    app.inicio()
