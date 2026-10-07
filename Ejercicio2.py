class PokemonNode:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


def buscar(PokemonNode, nombre):
    if PokemonNode is None:
        return False

    if PokemonNode.nombre == nombre:
        return True

    return buscar(PokemonNode.siguiente, nombre)

