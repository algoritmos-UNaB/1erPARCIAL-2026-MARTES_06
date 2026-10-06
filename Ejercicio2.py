class PokemonNode:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.siguiente = None


def buscar_pokemon(nodo: PokemonNode, nombre_pokemon: str):
    if nodo is None:
        return False

    if nodo.nombre == nombre_pokemon:
        return True

    return buscar_pokemon(nodo.siguiente, nombre_pokemon)


# Tiempo de ejecución estimado: O(n)
# En el peor caso, la función debe recorrer todos los nodos
# de la lista hasta encontrar el Pokémon o llegar al final.