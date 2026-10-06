class PokemonNode:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

def buscar_pokemon(nodo, nombre_pokemon):
    if nodo is None:
        return False
    if nodo.nombre == nombre_pokemon:
        return True
    return buscar_pokemon(nodo.siguiente, nombre_pokemon)

# Respuesta teórica: El tiempo depende de la posición de N de la cual arrancamos, puede tocar el primer valor y buscar el último generando el máximo tiempo de busqueda posible. Tambien importa el tamaño de la lista