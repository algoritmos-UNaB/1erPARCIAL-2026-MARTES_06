class Pokemon:
    
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        if nivel >= 1 and nivel <= 100:
            self.nivel = nivel
        else:
            self.nivel = 1
            print("Nivel Invalido, se defaultea a 1 para no lanzar excepcion")
            #Sé que es mala práctica poner lógica en un constructor, pero al no tener lugar donde instanciar un pokemon y arrojar la excepción correspondiente, decidí ir por este camino

    def subir_nivel(self):
        if self.nivel < 100:
            self.nivel = self.nivel + 1

    def __str__(self):
         return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"


class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipo = []

    def agregar_pokemon(self, pokemon):
        if len(self.equipo) < 6:
            self.equipo.append(pokemon)
            return
        print("Ya posee 6 pokemones en su equipo")

    def mostrar_equipo(self):
        for pokemon in self.equipo:
            print(pokemon)    

    def nivel_promedio(self):
        suma = 0
        tamaño_equipo = len(self.equipo)
        if tamaño_equipo == 0:
            return suma 
        for pokemon in self.equipo:
            suma += pokemon.nivel
        promedio = suma / tamaño_equipo
        return promedio
        
