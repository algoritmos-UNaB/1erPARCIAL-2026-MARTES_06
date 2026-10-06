class PokemonNode:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.siguiente = None


def buscar_pokemon(nodo: PokemonNode, nombre_pokemon: str) -> bool:
    if nodo is None:
        return False
    if nodo.nombre == nombre_pokemon:
        return True
    return buscar_pokemon(nodo.siguiente, nombre_pokemon)

    #El tiempo estimado dependera si el pokemon que se busca esta al final o si no existe, porque la funcion busca nodo por nodo haciendo N cantidad de pasos. si la lsita crece el tiempo tambien