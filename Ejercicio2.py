class PokemonNode:
    def __init__(self, nombre: str):
         self.nombre = nombre
         self.siguiente = None


def buscar_pokemon(nodo: PokemonNode, nombre_pokemon: str) -> bool:
    if nodo is None:
        return False
    if nodo.Nombre == nombre_pokemon:
        return True
    
    return buscar_pokemon(nodo.siguiente, nombre_pokemon)



if __name__== "__main__":

    primero = PokemonNode("Pikachu")
    primero.siguiente = PokemonNode("Charmander")
    primero.siguiente.siguiente = PokemonNode("Squirtle")

    print(buscar_pokemon(primero, "Squirtle"))
    print(buscar_pokemon, "Bulbasaur")
    print(buscar_pokemon(Node, "Pikachu"))