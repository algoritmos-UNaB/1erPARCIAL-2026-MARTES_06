class Pokemon: 
    def __init__  (self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        if nivel < 1 or nivel > 100:
            print ("El nivel debe ser entre 1 y 100, te asigno nivel 1 automaticamente")
            self.nivel = 1
        else:
            self.nivel = nivel

        
    def subir_nivel (self):
        if self.nivel >= 100:
            print ("Nivel Maximo")
        else:
            self.nivel = self.nivel + 1
            
    def __str__ (self):
        return f"Nombre: {self.nombre} Tipo: {self.tipo} Nivel: {self.nivel}"

    
class Entrenador:
    def __init__ (self, nombre, equipo): 
        self.nombre = nombre    
        self.equipo = []


    def agregar_pokemon (self, pokemon):
        if len(self.equipo) == 6:
            print ("Equipo completo no se puede agregar mas Pokemons")
        else:
            self.equipo.append (pokemon)

    def mostrar_equipo (self):
        for x in self.equipo:
            print (x)
        
    def nivel_promedio (self):
        if len(self.equipo) == 0:
            return 0
        else:
            suma = 0
            for x in self.equipo:
                suma = suma + x.nivel
            return suma / len (self.equipo)