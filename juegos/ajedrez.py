import pygame
import sys
# Dimensiones de la pantalla
ancho = 480
alto = 480

# Tamaño de los cuadrados del tablero
tamanio_casilla = ancho // 8

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Inicializar Pygame
pygame.init()
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Ajedrez')

reloj = pygame.time.Clock()

# Tablero de juego
tablero = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

# Dibujar el tablero de ajedrez
def dibujar_tablero():
    for fila in range(8):
        for columna in range(8):
            color = blanco if (fila + columna) % 2 == 0 else negro
            pygame.draw.rect(pantalla, color, (columna * tamanio_casilla, fila * tamanio_casilla, tamanio_casilla, tamanio_casilla))

# Dibujar las piezas en el tablero
def dibujar_piezas():
    for fila in range(8):
        for columna in range(8):
            pieza = tablero[fila][columna]
            if pieza != ' ':
                x = columna * tamanio_casilla + tamanio_casilla // 2
                y = fila * tamanio_casilla + tamanio_casilla // 2

                # Dibujar pieza en el centro de la casilla
                if pieza.isupper():
                    # Pieza blanca
                    color_pieza = blanco
                else:
                    # Pieza negra
                    color_pieza = negro

                # Dibujar círculo para representar la pieza
                pygame.draw.circle(pantalla, color_pieza, (x, y), tamanio_casilla // 2 - 5)

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(negro)
    dibujar_tablero()
    dibujar_piezas()

    pygame.display.flip()
    reloj.tick(60)