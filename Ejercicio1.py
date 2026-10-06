class Pokemon:
    #clase pokemon con nombre, tipo y nivel
    def __init__ (self, nombre: str, tipo: str, nivel: int) :
        #atributos basicos del pokemon
        self.nombre = nombre
        self.tipo = tipo

        self.nivel = max (1, min (100, nivel)) #nivel maximo del pokemon (100), minimo (1)


    def subir_nivel (self):

        if self.nivel < 100: #sube nivel si no llego al nivel maximo (100)

            self.nivel += 1


    def __str__ (self) :
        #devuelve como se muestra objeto cuando se hace print
        return f"Nombre: {self.nombre} | Tipo: {self.tipo} | Nivel: {self.nivel}"


class Entrenador:

    maximo_equipo = 6

    def __init__ (self, nombre: str) :

        self.nombre = nombre
        self.lista_equipo = [] #lista vacia donde se guardan los pokemones


    def agregar_pokemon (self, pokemon: Pokemon) :
        #verificamos si no se alcanzaron los maximos pokemones seteados
        if len (self.lista_equipo) >= self.maximo_equipo :

            print (f"No se pueden tener mas de {self.maximo_equipo} pokemones en el equipo.")

        else :
            #si hay lugar en la lista se agrega un pokemon
            self.lista_equipo.append (pokemon)

    def mostrar_equipo (self) :
        #muestra el entrenador y su equipo
        print (f"Entrenador: {self.nombre}")

        for pokemon in self.lista_equipo :

            print (pokemon)

    def nivel_promedio (self) :

        if not self.lista_equipo: #si el equipo esta vacio devuelve 0

            return "Tu promedio es: 0"

        suma = 0
        #suma los niveles de todos los pokemones y sasca el promedio
        for poke in self.lista_equipo :

            suma += poke.nivel

        promedio = suma / len (self.lista_equipo)

        return f"Tu promedio es: {promedio}"


"""Nombre y Apellido: RODRIGO MATIAS LOPEZ
Email: rodlopez003@gmail.com
Comisión: 1"""