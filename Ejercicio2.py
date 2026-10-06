class PokemonNode():
    def __init__(self, nombre:str, siguiente = None):
        
        if type(nombre) != str:
            raise TypeError("El nombre debe ser un string..")
        self.nombre = nombre
        self.sig = siguiente


def buscar_pokemon(nodo:PokemonNode, nombre_pokemon :str):
    if nodo is None:
        return False
    
    elif nodo.nombre == nombre_pokemon:
        return True

    return buscar_pokemon(nodo.sig, nombre_pokemon)
    