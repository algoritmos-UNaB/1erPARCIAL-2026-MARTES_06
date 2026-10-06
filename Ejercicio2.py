class PokemonNode:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.siguiente = None

def buscar_pokemon(nodo: PokemonNode, nombre_pokemon):
    if nodo is None:
        return False
    if nodo.nombre == nombre_pokemon:
        return True
    return buscar_pokemon(nodo.siguiente, nombre_pokemon)

    # tiempo de ejecución: 0(n) lineal, revisa los pokémon uno por uno, tiene que recorrer toda la lista haciendo tantos pasos como hay pokémon