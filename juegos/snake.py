import pygame
import time
import random

# Inicialización del juego
pygame.init()

# Dimensiones de la ventana del juego
width = 800
height = 600

# Colores RGB
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Configuración de la ventana del juego
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Velocidad del juego
fps = pygame.time.Clock()

# Tamaño del bloque de la serpiente y velocidad de movimiento
block_size = 20
snake_speed = 15

# Fuentes de texto
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)


# Función para mostrar el puntaje en la pantalla
def our_score(score):
    value = score_font.render("Puntos: " + str(score), True, white)
    window.blit(value, [0, 0])


# Función para dibujar la serpiente en la pantalla
def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], block_size, block_size])


# Función principal del juego
def gameLoop():
    game_over = False
    game_close = False

    # Posición inicial de la serpiente
    x1 = width / 2
    y1 = height / 2

    # Cambios en las coordenadas
    x1_change = 0
    y1_change = 0

    # Cuerpo de la serpiente
    snake_list = []
    length_of_snake = 1

    # Posición aleatoria de la comida
    foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            window.fill(black)
            message = font_style.render("¡Perdiste! Presiona Q-Salir o C-Jugar de nuevo", True, white)
            window.blit(message, [width / 6, height / 3])
            our_score(length_of_snake - 1)
            pygame.display.update()

            # Loop para el manejo de eventos del juego
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Loop para el manejo de eventos del juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Lógica para mantener la serpiente dentro de los límites de la ventana
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        pygame.draw.rect(window, red, [foodx, foody, block_size, block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(block_size, snake_list)
        our_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            length_of_snake += 1

        fps.tick(snake_speed)

    pygame.quit()
    quit()


# Ejecutar el juego
gameLoop()
