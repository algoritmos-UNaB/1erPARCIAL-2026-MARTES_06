class PokemonNode:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None
def buscar_pokemon(nodo, nombre_pokemon):
    if nodo is None:
        return false
    if nodo.nombre == nombre_pokemon:
        return true
    return buscar_pokemon (nodo.siguiente, nombre_pokemon)

##Teoría: Cuál es el tiempo de ejecución estimado de la función: el tiempo de ejecución es O(n) porque no sabemos cuantos pokemon hay,
##y e el peor caso, la funcion tiene que recorrer todos los nodos de la lista
