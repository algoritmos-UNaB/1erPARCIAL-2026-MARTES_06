class Pokemon:

    def __init__ (self, nombre: str, tipo: str, nivel: int) :

        self.nombre = nombre
        self.tipo = tipo

        self.nivel = max (1, min (100, nivel))


    def subir_nivel (self):

        if self.nivel < 100:

            self.nivel += 1


    def __str__ (self) :

        return f"Nombre: {self.nombre} | Tipo: {self.tipo} | Nivel: {self.nivel}"


class Entrenador:

    maximo_equipo = 6

    def __init__ (self, nombre: str) :

        self.nombre = nombre
        self.lista_equipo = []


    def agregar_pokemon (self, pokemon: Pokemon) :

        if len (self.lista_equipo) >= self.maximo_equipo :

            print (f"No se pueden tener mas de {self.maximo_equipo} pokemones en el equipo.")

        else :

            self.lista_equipo.append (pokemon)

    def mostrar_equipo (self) :

        print (f"Entrenador: {self.nombre}")

        for pokemon in self.lista_equipo :

            print (pokemon)

    def nivel_promedio (self) :

        if not self.lista_equipo:

            promedio = 0

            return f"Tu promedio es: {promedio}"

        for x in self.lista_equipo :

            promedio = x.nivel / len (self.lista_equipo)

        return f"Tu promedio es: {promedio}"


app = Entrenador ("Rodrigo")
app.agregar_pokemon (Pokemon ("Pikachu", "Electrico", 40))
app.agregar_pokemon (Pokemon ("Charizard", "Fuego", 50))
app.agregar_pokemon (Pokemon ("Squirtle", "Agua", 30))
app.agregar_pokemon (Pokemon ("Rookidee", "Aire", 20))

app.mostrar_equipo ()

print (app.nivel_promedio ())