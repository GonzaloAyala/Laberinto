# El Juego del Laberinto [*]

Vamos a construir un juego de un laberinto. Este juego utiliza una librería que se llama Pygame que nos permite hacer juegos fácilmente. La estructura general de un programa que usa Pygame es un while que constantemente está ciclando, esperando por un evento que el jugador realiza (tocar teclas en el teclado, ratón, etc) y según el evento disparando una acción asociada (si el evento fue una tecla para mover al personaje, debe ejecutarse la acción asociada para que el juego reaccione).

En este caso les hemos provisto un esqueleto de programa del laberinto donde ustedes deberán completar el código. El bucle while que constantemente cicla esperando por acciones del jugador es *while SeguirCiclando*


## ¿Qué conocimientos previos aplicaremos con esta actividad?

Para este ejercicio estaremos viendo lo siguiente:

- uso de estructura if-elif-else
- uso de librerías
- como integrar cosas que hemos visto en el curso en un programa con funcionalidades más complejas


## ¿Qué tenemos que saber en cuanto a las librerías y funciones predefinidas que usaremos?

De la librería laberinto ya tenemos definidas las siguientes funciones:

- moverDerecha, moverIzquierda, moverArriba, moverAbajo,- obtenerTecla, juegoFinalizado, obtenerTiempo

Todas estas funciones (por motivos que no nos importan por el momento) no tienen parámetros de entrada, pero sí retornan valores de salida. 

- obtenerTecla() : retorna la tecla que ha apretado el jugador. ¿Cómo indica qué tecla apretó? retornando un string. Si ese string es "DERECHA" significa que el jugador apretó la tecla que indica derecha; lo mismo para "IZQUIERDA", "ARRIBA", "ABAJO"

- moverDerecha() hace que el personaje (un cuadradito) se mueva a la derecha (internamente se encarga de chequear si es un movimiento válido, es decir que no pueda pasar sobre una pared; si no lo es entonces se queda en el mismo lugar). Lo mismo con moverDerecha(), moverArriba()y moverAbajo()

- juegoFinalizado() devuelve True o False según si el personaje llegó a la salida 

- obtenerTiempo() devuelve el tiempo transcurrido desde que se inició la partida


## ¿Qué tenemos que hacer?

1) Ejecutar el código tal como está. IMPORTANTE: Luego de ejecutarlo hacer click en la ventana en el área del laberinto para que todas las acciones de tocar una tecla sean capturadas en el juego y no en la consola.


2) Si ejecutas el código tal como está... ¿Qué hace? ¿Qué sucede? (sucede que no está completo, de modo que el objetivo de este desafío es completar el juego).

3) Arreglar lo del punto 2 para lograr la lógica deseada: completar el juego para que se puedan reconocer todas las teclas de movimiento (arriba, abajo, izquierda, derecha), reconciendo también cuándo se ha logrado salir del laberinto.

4) Agregar un contador que indique cuántos movimientos hizo el jugador para lograr salir del laberinto, y cuando termine la partida imprimirlo.

5) Quisiera imprimir tambén el tiempo que transcurrió desde que empezó el juego hasta que se logró terminar el laberinto (ojo que tenemos una función ya definida para esto!)

6) et voilà! Completamos el código de un juego!

### Algunos datos adicionales:
- laberinto.pyc es un archivo que incluye el código adicional que les hemos provisto para este desafío. ¿por qué cuando quiero ver el archivo veo caracteres raros? Lo que ves es código python que fue transformado a un "lenguaje intermedio" denominado bytecode. Contiene las funciones que les hemos provisto!
- laverinto.svg es el archivo con la imagen del laberinto 
- ¿quieres generar otro laberinto? Ingresando a http://www.mazegenerator.net/ tendrás un generador automático de laberintos. Lo generás, guardás la imagen del laberinto (está en formato .svg), renombrás ese archivo a laberinto.svg y reemplazas el anterior en el proyecto)

[*] actividad diseñada por Bruno Cattáneo