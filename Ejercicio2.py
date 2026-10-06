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

Teoría: Cuál es el tiempo de ejecución estimado de la función buscar_pokemon()?
Es del orden de n, siendo n la cantidad de Pokémon de la lista. El peor caso es que no esté, porque ahí la función recorre toda la lista para darse cuenta.