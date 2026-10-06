class Pokemon:

    def __init__ (self, nombre: str, tipo: str, nivel: int) :
        #atributos del pokemon
        self.nombre = nombre
        self.tipo = tipo
        #defino nivel minimo (1) y maximo 100
        self.nivel = max (1, min (100, nivel))


    def subir_nivel (self):

        if self.nivel < 100:
            #sube de nivel mientras que no llegue al nivel maximo (100)
            self.nivel += 1


    def __str__ (self) :
        #devuelvo el objeto cuando se usa print
        return f"Nombre: {self.nombre} | Tipo: {self.tipo} | Nivel: {self.nivel}"


class Entrenador:
    #nivel maximo de equipo
    maximo_equipo = 6

    def __init__ (self, nombre: str) :

        self.nombre = nombre
        self.lista_equipo = [] #lista vacia donde se guardan los objetos pokemon


    def agregar_pokemon (self, pokemon: Pokemon) :
        #verifico que el equipo no sea el maximo permitido
        if len (self.lista_equipo) >= self.maximo_equipo :

            print (f"No se pueden tener mas de {self.maximo_equipo} pokemones en el equipo.")

        else :
            #si hay lugar en la lista se agrega un pokemon
            self.lista_equipo.append (pokemon)

    def mostrar_equipo (self) :
        #muestro el nombre del entrenador y su equipo
        print (f"Entrenador: {self.nombre}")

        for pokemon in self.lista_equipo :

            print (pokemon)

    def nivel_promedio (self) :
        #si el equipo esta vacio (lista) devuelve 0 para no dividir por 0
        if not self.lista_equipo:

            return "Tu promedio es: 0"

        suma = 0 
        #sumamos todos niveles de los pokemones para sacar el promedio
        for poke in self.lista_equipo :

            suma += poke.nivel

        promedio = x.nivel / len (self.lista_equipo)

        return f"Tu promedio es: {promedio}"


"""Nombre y Apellido: RODRIGO MATIAS LOPEZ
Email: rodlopez003@gmail.com
Comisión: 1"""