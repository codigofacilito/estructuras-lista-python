# Lista uno contiene 6 edades
edades = [1,2,3,4,5,6]

# Lista 2 contiene 3 edades
edades2 = [7,8,9]

# extend sirve para combinar la lista que se pasa de parametro
edades.extend(edades2)
# Aqui hacemos otro extends, con este la lista contrendria 12 elementos
edades.extend([1,2,3])

# Imprimimos la lista de edades
print(edades)
# Con la funcion len obtenemos la cantidad de elementos en la lista
print(len(edades))

# print(edades[ len(edades) - 1 ])
# Accedenos al registro 4, tomando encuenta que comienza en 0 1 2 3
print(edades[ 3 ])