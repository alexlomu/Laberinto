# Laberinto
La dirección de GitHub de este reposoitorio es: [Github](https://github.com/alexlomu/Laberinto)
https://github.com/alexlomu/Laberinto

Hemos hecho un juego del laberinto en el que el camino esta predefinido y el jugador tendrá que averiguar como salir de él.
El diagrama de flujo es el siguiente:
![figma_laberinto](https://user-images.githubusercontent.com/91721507/145279603-9b53109b-c53b-4fbc-9d90-425bcb8fc924.JPG)
El código del juego es el siguiente:
```
#Introducimos el laberinto resuelto
mapa_resuelto = [
    " ", "X", "X", "X", "X",
    " ", "X", "X", "X", "X",
    " ", "X", " ", " ", "S",
    " ", "X", " ", "X", "X",
    " ", " ", " ", "X", "X",
]

orden_salida = ["ABAJO", "ABAJO", "ABAJO", "ABAJO", "DERECHA", "DERECHA", "ARRIBA", "ARRIBA", "DERECHA", "DERECHA"]
#posicion de columnas
posicion_x = 0
#posicion de filas
posicion_y = 0
#Funcion que nos servira para movernos dentro del laberinto
def mover():
    global posicion_x
    global posicion_y
    print("1: ARRIBA")
    print("2: ABAJO")
    print("3: DERECHA")
    print("4: IZQUIERDA")
    movimiento = int(input("Selecciona un movimiento(1-4)"))
    if movimiento == 1:
        posicion_y -= 1
        if posicion_y > 0 and posicion_y < 5:
            return posicion_y
        else:
            "Te has salido del mapa"
    if movimiento == 2:
        posicion_y += 1
        return posicion_y
    if movimiento == 3:
        posicion_x += 1
        return posicion_x
    if movimiento == 4:
        posicion_x -= 1
        if posicion_x > 0 and posicion_x < 5:
            return posicion_x
        else:
            "Te has salido del mapa"
    
#Funcion para jugar al laberinto
def play():
    global posicion_x
    global posicion_y
    #Le mostramos al jugador como es el laberinto sin conocer el camino
    mapa_inicial = [
    "0", "?", "?", "?", "?",
    "?", "?", "?", "?", "?",
    "?", "?", "?", "?", "?",
    "?", "?", "?", "?", "?",
    "?", "?", "?", "?", "?",
    ]
    print("El 0 es tu posición, los ? pueden ser un muro o el camino para salir del laberinto")
    print(mapa_inicial)
    while True:
        #Para encontrar la posición de la lista a cambiar usaremos
        posicion_total = (5*posicion_y) + posicion_x
        #Cambiamos la posicion en la que nos encontrabamos por "" para marcar el camino bueno
        mapa_inicial[posicion_total] = ""
        mover()
        posicion_total = (5*posicion_y) + posicion_x
        #Si la posicion nueva es un muro
        if mapa_resuelto[posicion_total] == "X":
            print("Te has encontrado un muro, has vuelto a la posición inicial")
            mapa_inicial[posicion_total] = "M"
            posicion_x = 0
            posicion_y = 0
            print(mapa_inicial)
        #Si la posicion nueva es camino
        elif mapa_resuelto[posicion_total] == " ":
            print("Vas en el buen camino, sigue así")
            mapa_inicial[posicion_total] = "0"
            print(mapa_inicial)
        #Si la posición nueva es la salida
        elif mapa_resuelto[posicion_total] == "S":
            print("Enhorabuena, has conseguido salir del laberinto!")
            print("El orden de salida era:")
            print(orden_salida)
            break
        #Si se sale del mapa o hay algun error vuelve al principio
        else:
            posicion_x = 0
            posicion_y = 0
            print("Has introducido un movimiento erróneo, has vuelto a la posición inicial")
            print(mapa_inicial)
#LLamamos a la función de jugar                
play()
