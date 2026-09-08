# LISTAS

# una lista sirve para guardar varios datos
# los elementos de una lista se pueden modificar

lista = ["adrian sanchez", "soy adrian", True, 1.85]

print(lista)

# puedo cambiar un elemento de la lista
# los indices empiezan desde 0

lista[3] = "maquinola"

print(lista)

# aqui cambie el dato que estaba en la posicion 3
# antes era 1.85 y ahora es "maquinola"


# TUPLAS

# una tupla tambien sirve para guardar varios datos
# pero los elementos de una tupla no se pueden modificar

tupla = ("adrian sanchez", "soy adrian", True, 1.85)

print(tupla)

# esto no se puede hacer porque la tupla no se puede modificar

# tupla[3] = "maquinola"


# CONJUNTOS (SET)

# un conjunto sirve para guardar varios elementos
# no permite tener elementos repetidos
# no puedo acceder a los elementos usando un indice

conjunto = {"adrian sanchez", "soy adrian", True, 1.85}

print(conjunto)

# ejemplo de que no guarda elementos repetidos

numeros = {1, 2, 3, 3, 3, 4}

print(numeros)

# aunque puse el numero 3 varias veces
# solo aparece una vez


# DICCIONARIO (DICT)

# un diccionario guarda los datos usando una clave y un valor
# por ejemplo "nombre" es la clave
# y "adrian sanchez" es el valor

diccionario = {
    "nombre": "adrian sanchez",
    "descripcion": "soy adrian",
    "activo": True,
    "altura": 1.85
}

print(diccionario)

# puedo buscar un dato usando su clave

print(diccionario["nombre"])
print(diccionario["altura"])

# tambien puedo cambiar un valor del diccionario

diccionario["nombre"] = "jeancarlos"

print(diccionario)


# RESUMEN

# list = se puede modificar
# tuple = no se puede modificar
# set = no permite elementos repetidos
# dict = guarda datos usando clave y valor