import random

def intro():

    print("Juguemos un juego!")
    print("Vamos a mezclar, y debes adivinar la posición de la pelotita")
    print("Juguemos!")

def obtener_bola_escondida ():
    
    d = [" ", "O", " "]
    
    random.shuffle(d)
    return d


def obtener_respuesta_jugador():
  rs = '' 
  while rs not in ["0", "1", "2"]:
    rs = input("Elige un número: 0, 1 o 2? ")
  
  return int(rs) 


def juego(bola_escondida, respuesta_jugador):
    
    print(bola_escondida)
        
    if bola_escondida[respuesta_jugador] == "O":
        print("Ganaste!")
    else:
        print("Oh, perdiste :( ")
    
    return input("Jugamos de nuevo? :) ").lower()


RESPUESTAS_VALIDAS = ["s", "si", "y", "yes", "no", "n"]
intro()
jugar_de_nuevo = True

while jugar_de_nuevo:

  bola_escondida = obtener_bola_escondida()
  respuesta_jugador = obtener_respuesta_jugador()

  jugar_de_nuevo = juego(bola_escondida, respuesta_jugador)
    
  while jugar_de_nuevo not in RESPUESTAS_VALIDAS:
    print('Elegiste una opcion no valida... va de nuevo')
    jugar_de_nuevo = input("Jugamos de nuevo? :) ").lower()
  
  if jugar_de_nuevo in ['n', 'no']:
    break


print('Bueno, adiós :( ')  
