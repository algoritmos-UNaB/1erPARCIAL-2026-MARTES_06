class PokemonNode:
    def __init__(self,nombre:str):
        #Constructor que inicializa el nombre del Pokémon y establece al siguiente como None (puntero)
        self.nombre = nombre
        self.siguiente = None

    def buscar_pokemon(nodo: PokemonNode, nombre_pokemon : str) -> bool:
        #función recursiva
        if nodo.nombre == nombre_pokemon:
            #Si encuentra al pokemon devuelve True
            return True
        
        return buscar_pokemon(nodo.siguiente, nombre_pokemon)
        #se llama a sí misma para avanzar una posición y volver a buscar