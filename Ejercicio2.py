class PokemonNodo:
    def __init__(self,nombre):
    self.nombre=nombre
    self.siguiente= None

def buscar_pokemon(nodo,nombre_pokemon):
    if nodo is None:
        return False
    if nodo.nombre==nombre_pokemon:
        return True
    return buscar_pokemon(nodo.siguiente,nombre_pokemon)

amoonguss=PokemonNodo("Amoonguss")
jigglypuff=PokemonNodo("Jigglypuff")
charmander=PokemonNodo("Charmander")

amoonguss.siguiente= jigglypuff
jigglypuff.siguiente=charmander
print(buscar_pokemon(amoonguss,"Charmander"))

