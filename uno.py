# Perdirle al usuario que ingrese n cantidades de edades

n = int(input("Inserta tu cantidad de edades "))

# Definir la lista
edades = []

# Iterar n cantidad de veces
for edad in range(n):
    # Agregar lo que el usuario ingrese usando el metodo input
    edades.append( int( input("Inserta tu edad ") ) )

# Ordenar la lista
edades.sort()

# Imprimir la lista
print(edades)