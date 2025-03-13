FILAS = 5
COLUMNAS = 5
META_FILA = FILAS - 1
META_COLUMNA = COLUMNAS - 1

def crear_laberinto():
    """ Crea la estructura del laberinto con la meta establecida. """
    laberinto = [[False] * COLUMNAS for _ in range(FILAS)]
    laberinto[META_FILA][META_COLUMNA] = True  # Meta
    return laberinto

def imprimir_laberinto(laberinto, fila_jugador, columna_jugador):
    """ Muestra el laberinto con la posición del jugador. """
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if i == fila_jugador and j == columna_jugador:
                print("X ", end="")  # Jugador
            elif laberinto[i][j]:
                print("O ", end="")  # Meta
            else:
                print(". ", end="")  # Espacio vacío
        print()

def mover_jugador(fila, columna, movimiento):
    """ Actualiza la posición del jugador según el movimiento ingresado. """
    if movimiento == 'w' and fila > 0:
        fila -= 1
    elif movimiento == 's' and fila < FILAS - 1:
        fila += 1
    elif movimiento == 'a' and columna > 0:
        columna -= 1
    elif movimiento == 'd' and columna < COLUMNAS - 1:
        columna += 1
    else:
        print("Movimiento no válido.")
    return fila, columna

def main():
    laberinto = crear_laberinto()
    fila_jugador, columna_jugador = 0, 0

    while True:
        imprimir_laberinto(laberinto, fila_jugador, columna_jugador)

        if fila_jugador == META_FILA and columna_jugador == META_COLUMNA:
            print("\n¡Has alcanzado la meta! ¡Felicidades!")
            break

        movimiento = input("\nIngrese movimiento (w: arriba, s: abajo, a: izq, d: der): ")
        fila_jugador, columna_jugador = mover_jugador(fila_jugador, columna_jugador, movimiento)

if __name__ == "__main__":
    main()

#Hola chaval