class PokemonNode:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

def buscar_pokemon(nodo, nombre_pokemon):

    if nodo is None:
        return False

    if nodo.nombre == nombre_pokemon:
        return True

    return buscar_pokemon(nodo.siguiente, nombre_pokemon)

# Cual es el tiempo de ejecucion estimado de la funcion:
# Para n pokemon  T(n) = T(n-1) + c. En cada llamada la funcion avanza
# un nodo. El big O es O(n).