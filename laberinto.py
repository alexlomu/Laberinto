mapa_resuelto = [
    " ", "X", "X", "X", "X",
    " ", "X", "X", "X", "X",
    " ", "X", " ", " ", "S",
    " ", "X", " ", "X", "X",
    " ", " ", " ", "X", "X",
]
orden_salida = ["ABAJO", "ABAJO", "ABAJO", "ABAJO", "DERECHA", "DERECHA", "ARRIBA", "ARRIBA", "DERECHA", "DERECHA"]
posicion_x = 0
posicion_y = 0

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
    

def play():
    global posicion_x
    global posicion_y
    mapa_inicial = [
    "0", "?", "?", "?", "?",
    "?", "?", "?", "?", "?",
    "?", "?", "?", "?", "?",
    "?", "?", "?", "?", "?",
    "?", "?", "?", "?", "?",
    ]
    print(mapa_inicial)
    while True:
        posicion_total = (5*posicion_y) + posicion_x
        mapa_inicial[posicion_total] = ""
        mover()
        posicion_total = (5*posicion_y) + posicion_x
        if mapa_resuelto[posicion_total] == "X":
            print("Te has encontrado un muro, has vuelto a la posición inicial")
            mapa_inicial[posicion_total] = "M"
            posicion_x = 0
            posicion_y = 0
            print(mapa_inicial)
        elif mapa_resuelto[posicion_total] == " ":
            print("Vas en el buen camino, sigue así")
            mapa_inicial[posicion_total] = "0"
            print(mapa_inicial)
        elif mapa_resuelto[posicion_total] == "S":
            print("Enhorabuena, has conseguido salir del laberinto!")
            print("El orden de salida era:")
            print(orden_salida)
            break
        else:
            posicion_x = 0
            posicion_y = 0
            print("Has introducido un movimiento erróneo, has vuelto a la posición inicial")
            print(mapa_inicial)
                
play()