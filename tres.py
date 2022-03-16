#            0       1       2    De izq a derecha
#            -3      -2      -1   De recha a izq
nombres = ['Luis', 'Fer', 'Juan']

# len devuelve la cantida de elementos en la lista
print(len(nombres))

# Recordemos que los indices comienzan en 0, aqui obtenemos el último valor
print(nombres[ len(nombres) - 1 ])

# También podemos acceder a los elementos de la lista, de forma inverza comenzando con -1
print(nombres[-2])

# Recordemos que extend sirve para agregar otra lista a la lista inicial, en este caso estamos agregando 2 elementos mas
nombres.extend(['Vilma','Araceli'])

# Imprimimos la lista de nombres, en este caso tendria 5 elementos
print(nombres)

# Accedemos al último valor de la lista en este caso es Araceli
print(nombres[-1])

# Ordenamos con el metodo sort
nombres.sort()

# Imprimimos la list
print(nombres)