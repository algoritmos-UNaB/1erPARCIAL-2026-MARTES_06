class PokemonNode: 
    def__init__(sel, nombre:str):
        self.nombre = nombre
        sel.siguiente = None  #flechita al siguiente pokemon o a None


def buscar_pokemon(nodo: PokemonNode, nombre_pokemon:str) ->bool:
    
    #caso bASE 1 el nodo actual es None (fin de la lista)
    if nodo is None:
        return False

    #caso base 2: el nombre del nodo coincide con el buscado
    if nodo.nombre.lower() == nombre_pokemon.lower():
        return True

    #buscar en el siguiente nodo de la lista
    return buscar_pokemon(nodo.siguiente, nombre_pokemon)


    