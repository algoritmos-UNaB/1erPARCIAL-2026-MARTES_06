class PokemonNode:
    def __init__(self,nombre:str):
        #  Que inicializa el nombre del Pokémon y establece al siguiente como None (puntero)
        self.nombre = nombre
        self.siguiente = None

    def buscar_pokemon(nodo: PokemonNode, nombre_pokemon : str) -> bool:
        # Función recursiva
        if nodo is None:
            return False
            # Caso de llegar al final de la lista de pokemones
        if nodo.nombre == nombre_pokemon:
            # Si encuentra al pokemon devuelve True
            return True
        
        return buscar_pokemon(nodo.siguiente, nombre_pokemon)
        # Se llama a sí misma para avanzar una posición y volver a buscar

        """Teoría:
        Tomando sólo la parte práctica lineal porque no puedo ver más de un pokemon por posicion, o forma de acceder a sublistas
        Peor escenario: no existe el pokemon, y la funcion tiene n llamadas recursivas
        Mejor escenario: pokemon en primera posición, sin llamada recursiva
        El tiempo estará dado por: o(n) donde n es o bien dónde está el pokemon en la lista o bien la longitud (len) de la lista en caso de no estar
        """