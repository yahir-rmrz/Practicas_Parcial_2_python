
# Definimos una función llamada inicio que recibe un número (contador)
# Define a function called inicio that receives a number (counter)
def inicio(num):
    
    # Pedimos al usuario que escriba una calificación y la convertimos a entero
    # Ask the user to enter a grade and convert it to integer
    a = int(input('escribe una calificacion \n'))
    
    # Incrementamos el contador en 1
    # Increase the counter by 1
    num += 1
    
    # Agregamos la calificación a la lista
    # Add the grade to the list
    lista.append(a)
    
    # Si ya hay 5 o más calificaciones, imprimimos la lista
    # If there are 5 or more grades, print the list
    if num >= 5:
        print(lista)
    else:
        # Si no hay 5 aún, llamamos la función otra vez (recursión)
        # If there are not 5 yet, call the function again (recursion)
        return inicio(num)


# Creamos una lista vacía para guardar las calificaciones
# Create an empty list to store the grades
lista = []

# Declaramos la variable global num
# Declare the global variable num
global num

# Iniciamos el contador en 0
# Initialize the counter at 0
num = 0

# Si este archivo se ejecuta directamente, iniciamos el programa
# If this file is run directly, start the program
if _name_ == '_main_':
    inicio(num)