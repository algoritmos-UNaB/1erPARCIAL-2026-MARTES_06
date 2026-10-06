class PokemonNode: 
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.siguiente = None

def buscar_pokemon(nodo, nombre_pokemon):
        if  nodo is None:
            return False
        elif nodo.nombre == nombre_pokemon:
            return True
        else: 
            return buscar_pokemon(nodo.siguiente, nombre_pokemon)


# El tiempo de ejecucion seria la cantidad de nodos que se llama + none que seria el final de las cadenas.
# Veces que se llama: N
# None es el final de todos los nodos 
# Conclusion: Tiempo estimado seria: N+1