class PokemonNode:
    def __int__(self, nombre: str)
        self.nombre = nombre
        self.siguiente = None
    
    def buscar_pokemon(nodo, nombre_pokemon):
        if nodo is None:
            return False
        
        if nodo.nombre == nombre_pokemon:
            return True

        return buscar_pokemon(nodo.siguiente, nombre_pokemon)

lucario = PokemonNode("Lucario")
victini = PokemonNode("Victini")
gengar = PokemonNode("Gengar")

lucario.siguiente = gengar
gengar.siguiente = victini

#el tiempo estimado de la funcion es segun la entidad de pokemons/nodos que hay que seguir para encontrar al pokemon que buscamos