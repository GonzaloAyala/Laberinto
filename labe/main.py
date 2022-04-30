from laberinto import moverDerecha, moverIzquierda, moverArriba, moverAbajo, obtenerTecla, juegoFinalizado, obtenerTiempo

#recordar que cuando termina el juego deberemos mostrar la cantidad de movimientos que se hizo y el tiempo que llevó

def principal():
  # completa la condición
  # cuando debemos detenernos? cuando lleguemos al    #     fin del juego
  while <condicion>:
    #con obtenerTecla sabremos si apretó alguna tecla
    tecla = obtenerTecla()

    #si la tecla es "DERECHA", entonces hacemos que el         #personaje se mueva a la derecha
    if tecla == "DERECHA":
      moverDerecha()

      #ok, ahora falta completar el resto!
      

principal()