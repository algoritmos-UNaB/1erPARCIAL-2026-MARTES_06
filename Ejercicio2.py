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


#Respuesta a pregunta teoria:
#el tiempo de ejecucion estimado de buscar_pokemon() es O(n), ya que en el peor caso debe
#revisar todos los nodos de la lista.