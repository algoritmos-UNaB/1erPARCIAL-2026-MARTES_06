# Algoritmos y Estructuras de Datos

# 1erPARCIAL - MARTES - 06/10/26 - Comisión 1 -



- - -

### 📌 **Modalidad**

* 🗓️ **Fecha:** Martes **06/10**
* 🕖 **Disponibilidad:** desde las **18:30 hs** hasta las **01:45 h**.
* ⏱️ **Duración máxima:** **3 horas y 30 minutos (3:30 h)** desde el momento en que bifurcan el repositorio.
* 🧪 **Intentos:** Solo **1 (uno)**. 
* 📢 **Publicación de notas:** a más tardar el **Lunes posterior, después de las hs**.

> ⚠️ **IMPORTANTE:** deben estar conectados al Meet, **SE CONSIDERAN AUSENTES AQUELLOS/AS ALUMNOS/AS QUE NO SE CONECTEN**

> ⚠️ **IMPORTANTE:** Al final del archivo `README.md`, **DEBEN completar sus datos personales** (nombre completo, número de legajo y correo institucional).


- - -

## Estructuras de Datos en el Universo Pokémon

- - -

## Ejercicio 1: Implementación de TADs

En este universo, cada entrenador tiene un equipo Pokémon. Para este ejercicio deberá implementar dos clases en Python: <code>Pokemon</code> y <code>Entrenador</code>.

#### Clases a Implementar 

- Clase <code>Pokemon</code>:
    - Atributos:
        - <code>nombre : str </code>: Nombre del Pokémon.
        - <code>tipo : str</code>: Tipo del Pokémon (por ejemplo, Agua, Fuego, Planta). 
        - <code>nivel : int</code>: Nivel del Pokémon (debe estar entre 1 y 100).
    
    - Métodos:
        - <code>__init__()</code>: Constructor que inicializa los atributos del Pokémon.
        - <code>subir_nivel()</code>: Método que incrementa el nivel del Pokémon en 1, siempre y cuando no supere el nivel 100.
        - <code>__str__()</code>: Método que devuelve una representación en cadena del Pokémon en el formato: "Nombre: Pikachu, Tipo: Electrico, Nivel: 0"

 - Clase Entrenador:
    - Atributos:
        - <code>nombre : str</code>: Nombre del entrenador.
        - <code>equipo : list</code>: Lista que contiene instancias de la clase <code>Pokemon</code>. 
    - Métodos:
        - <code>__init__()</code>: Constructor que inicializa el nombre del entrenador y crea una lista vacía para el equipo.
        - <code>agregar_pokemon()</code>: Método que agrega un Pokémon al equipo. Si ya hay 6 Pokémon en el equipo, debe mostrar un mensaje indicando que no se pueden tener más Pokémon.
        - <code>mostrar_equipo()</code>: Método que imprime todos los Pokémon del equipo utilizando el método  <code>__str__</code> de la clase <code>Pokemon</code>.
        - <code>nivel_promedio():</code> Método que calcula y devuelve el nivel promedio de los Pokémon en el equipo. Si no hay Pokémon en el equipo, debe devolver 0.



## Ejercicio 2: Recursividad en el Universo Pokémon

Los entrenadores a menudo se enfrentan a desafíos que requieren la búsqueda de Pokémones en un área. Para este ejercicio implementar una función recursiva que simula la búsqueda de un Pokémon específico en una lista de Pokémones.

Suponga que tiene una lista donde cada nodo representa un Pokémon en el camino, cada nodo tiene un nombre y puede contener más de un Pokémon. La búsqueda de un Pokémon específico se puede realizar de manera recursiva verificando si el Pokémon se encuentra en el nodo actual o una de sus sublistas.


#### Clases a Implementar

Clase <code>PokemonNode</code>:  

- Atributos:
    - <code>nombre : str</code>: Nombre del Pokémon.
    - <code>siguiente : PokemonNode</code>: (PokemonNode) Siguiente Pokémon en el equipo (puede ser <code>None</code>).

- Métodos:
    - <code>__init__(self, nombre: str)</code>: Constructor que inicializa el nombre del Pokémon y establece al siguiente como <code>None</code>.

Función Recursiva <code>buscar_pokemon()</code>:

- Parámetros:
    - <code>nodo : PokemonNode</code>: Nodo actual donde se realiza la búsqueda.
    - <code>nombre_pokemon : str</code>: Nombre del Pokémon que se busca.

- Retorno:
    - Devuelve <code>True</code> si el Pokémon es encontrado en el equipo, y <code>False</code> si no se encuentra. 

- Lógica:
    - Si el nodo actual es <code>None</code>, devuelve <code>False</code>.
    - Si el nombre del nodo actual coincide con <code>nombre_pokemon</code>, devuelve <code>True</code>.
    - Llama recursivamente a sí misma para buscar en la lista.


- Teoría: Cuál es el tiempo de ejecución estimado de la función <code>buscar_pokemon()</code>?


## Ejercicio 3: Sistema de Evoluciones de Pokémon

Cada Pokémon podría evolucionar a una forma más poderosa, para gestionarlas implementar un sistema utilizando una </code>PilaEnlazada</code>, que permita llevar un registro de las evoluciones en orden inverso ya que la más reciente es la que se aplicará primero.

La pila se utilizará para almacenar las evoluciones de un Pokémon. Cuando uno de ellos evoluciona, se agrega su nueva forma a la pila. Si el entrenador decide revertir la evolución se puede desapilar la forma más reciente.

Queremos recorrer la pila utilizando un ciclo <code>for</code> deberan implementar un Iterador para esta clase.


#### Clases a Implementar

- Clase <code>Evolucion</code>:
    - Atributos:
        - <code>nombre : str</code>: Nombre del Pokémon en su forma evolucionada.

    - Métodos:
        - <code>_init__(self, nombre: str)</code>: Constructor que inicializa el nombre de la evolución.

- Clase <code>PilaEvoluciones:
    - Atributos:
        - <code>evoluciones: list</code>: Lista enlazada que almacena las evoluciones en orden.

    - Métodos:
        - <code>__init__(self)</code>: Constructor que inicializa la lista de evoluciones como vacía.
        - <code>apilar (self, evolucion: Evolucion)</code>: Método que agrega una evolución a la pila.
        - <code>desapilar (self)</code>: Método que elimina y devuelve la última evolución agregada a lapila. Si la pila está vacía debe devolver un mensaje indicando que no hay evoluciones para desapilar.
        - <code>mostrar_evoluciones (self)</code>: Método que imprime todas las evoluciones en el orden en que fueron apiladas.
        - <code>__iter__()</code>: Retorna el iterador.

- Clase <code>IteradorPilaEvoluciones:
    - Atributos:
        - <code>actual: Evolucion</code>: Lista enlazada que almacena las evoluciones en orden.

    - Métodos:
        - <code>__next__(self)</code>: Método que retorna el "siguiente valor" y actualiza el <code>actual</code>.


---
Nombre y Apellido: Lucas Esteban Lopez

Email: lucas77lopez@gmail.com

Comisión: 1

---