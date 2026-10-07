class PokemonNode:
    def __init__ (self, nombre, siguiente):
        self.nombre = nombre
        self.siguiente = None

    def buscar_pokemon (nodo, nombre_pokemon):
        if nodo == None:
            return False
        elif nodo.nombre == nombre_pokemon:
            return True
        return buscar_pokemon (nodo.siguiente, nombre_pokemon)

#tiempo de ejecucion estimado depende de cuantos pokemons tengo en la lista, mientras mas tenga mas va a tardar logicamente.