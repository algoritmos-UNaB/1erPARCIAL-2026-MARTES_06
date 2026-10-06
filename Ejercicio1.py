class Pokemon:
    def __init__(self, nombre, tipo, nivel = 1):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def subir_nivel(self):
        """
        Metodo que incrementa el nivel del Pokemon en 1, siempre y cuando no supere el nivel 100.
        """

        #Incrementa el nivel en 1 si no supera el nivel 100
        NIVEL_MAXIMO = 100

        if self.nivel >= NIVEL_MAXIMO:
            raise ValueError("ERROR: El Pokemon ya alcanzo el nivel 100.")

        self.nivel = self.nivel + 1


    def __str__(self):
        return ("Nombre: " + self.nombre
                + ", Tipo: " + self.tipo
                + ", Nivel:" + str(self.nivel))

    
class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipo = []

    def agregar_pokemon(self, pokemon):
        """
         Metodo que agrega un Pokemon al equipo. Si ya hay 6 Pokemon en el equipo, debe mostrar un mensaje indicando que no se pueden tener mas Pokemon.
        """
        if len(self.equipo) >= 6:
            raise ValueError("ERROR: No se puede tener mas de 6 pokemones")
        else:
            self.equipo.append(pokemon)

    def mostrar_equipo(self):
        """
        Metodo que imprime todos los Pokemon del equipo utilizando el metodo str de la clase Pokemon.
        """
        for pokemon in self.equipo:
            print(pokemon)

    def nivel_promedio(self):
        """
        Metodo que calcula y devuelve el nivel promedio de los Pokemon en el equipo. Si no hay Pokemon en el equipo, debe devolver 0.
        """
        if len(self.equipo) == 0:
            return 0

        suma_niveles = 0

        for pokemon in self.equipo:
            suma_niveles += pokemon.nivel

        return suma_niveles / len(self.equipo)




