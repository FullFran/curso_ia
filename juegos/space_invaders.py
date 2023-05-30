import pygame
import random
import sys

# Dimensiones de la pantalla
ancho = 800
alto = 600

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
morado = (128, 0, 128)

# Inicializar Pygame
pygame.init()
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Space Invaders')

reloj = pygame.time.Clock()
fuente = pygame.font.Font(None, 36)

# Jugador
jugador_caracter = '^'
jugador_ancho = 32
jugador_alto = 32
jugador_x = ancho // 2 - jugador_ancho // 2
jugador_y = alto - jugador_alto - 10
jugador_velocidad = 5

# Proyectil del jugador
proyectil_ancho = 8
proyectil_alto = 16
proyectil_x = jugador_x + jugador_ancho // 2 - proyectil_ancho // 2
proyectil_y = jugador_y
proyectil_velocidad = 10
proyectil_disparado = False

# Enemigos
enemigo_caracter = 'V'
enemigo_ancho = 32
enemigo_alto = 32
num_enemigos = 6  # Número de enemigos en pantalla
enemigos = []  # Lista para almacenar instancias de enemigos
for _ in range(num_enemigos):
    enemigo_x = random.randint(0, ancho - enemigo_ancho)
    enemigo_y = random.randint(50, 200)
    enemigos.append((enemigo_x, enemigo_y))

# Proyectiles del enemigo
enemigo_proyectil_ancho = 8
enemigo_proyectil_alto = 16
enemigo_proyectiles = []  # Lista para almacenar instancias de proyectiles del enemigo
enemigo_proyectil_velocidad = 2
# Estado del juego
game_over = False

# Función para verificar colisión entre rectángulos


def colision(rect1, rect2):
    return rect1.colliderect(rect2)


# Bucle principal del juego
while not game_over:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and not proyectil_disparado:
                proyectil_x = jugador_x + jugador_ancho // 2 - proyectil_ancho // 2
                proyectil_y = jugador_y
                proyectil_disparado = True

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a] and jugador_x > 0:
        jugador_x -= jugador_velocidad
    if teclas[pygame.K_d] and jugador_x < ancho - jugador_ancho:
        jugador_x += jugador_velocidad

    # Movimiento del proyectil del jugador
    if proyectil_disparado:
        proyectil_y -= proyectil_velocidad
        if proyectil_y < 0:
            proyectil_disparado = False

    # Movimiento de los enemigos
    for i in range(num_enemigos):
        enemigo_x, enemigo_y = enemigos[i]
        enemigo_x += jugador_velocidad // 2  # Movimiento hacia la derecha
        enemigos[i] = (enemigo_x, enemigo_y)
        if enemigo_x <= 0 or enemigo_x >= ancho - enemigo_ancho:
            jugador_velocidad *= -1

        # Disparo de los enemigos
        if random.randint(0, 200) < 1 and not enemigo_proyectiles:
            enemigo_proyectiles.append(
                (enemigo_x + enemigo_ancho // 2 - enemigo_proyectil_ancho // 2, enemigo_y))

    # Movimiento de los proyectiles del enemigo
    for i in range(len(enemigo_proyectiles)):
        enemigo_proyectil_x, enemigo_proyectil_y = enemigo_proyectiles[i]
        enemigo_proyectil_y += enemigo_proyectil_velocidad
        if enemigo_proyectil_y > alto:
            del enemigo_proyectiles[i]
            break

        # Colisión entre proyectil del enemigo y jugador
        enemigo_proyectil_rect = pygame.Rect(
            enemigo_proyectil_x, enemigo_proyectil_y, enemigo_proyectil_ancho, enemigo_proyectil_alto)
        jugador_rect = pygame.Rect(
            jugador_x, jugador_y, jugador_ancho, jugador_alto)
        if colision(enemigo_proyectil_rect, jugador_rect):
            game_over = True

    # Colisión entre proyectil del jugador y enemigos
    proyectil_rect = pygame.Rect(
        proyectil_x, proyectil_y, proyectil_ancho, proyectil_alto)
    for i in range(num_enemigos):
        enemigo_x, enemigo_y = enemigos[i]
        enemigo_rect = pygame.Rect(
            enemigo_x, enemigo_y, enemigo_ancho, enemigo_alto)
        if colision(proyectil_rect, enemigo_rect):
            enemigos[i] = (random.randint(
                0, ancho - enemigo_ancho), random.randint(50, 200))
            proyectil_disparado = False
            break

    pantalla.fill(negro)
    pygame.draw.rect(pantalla, azul, (jugador_x, jugador_y,
                     jugador_ancho, jugador_alto))
    pygame.draw.rect(pantalla, rojo, (proyectil_x, proyectil_y,
                     proyectil_ancho, proyectil_alto))
    for enemigo_x, enemigo_y in enemigos:
        pygame.draw.rect(pantalla, morado, (enemigo_x,
                         enemigo_y, enemigo_ancho, enemigo_alto))
    for enemigo_proyectil_x, enemigo_proyectil_y in enemigo_proyectiles:
        pygame.draw.rect(pantalla, rojo, (enemigo_proyectil_x, enemigo_proyectil_y,
                         enemigo_proyectil_ancho, enemigo_proyectil_alto))
    pygame.draw.rect(pantalla, rojo, (ancho - 40, 10, 30, 30)
                     )  # Botón de salida

    if game_over:
        texto = fuente.render("GAME OVER", True, rojo)
        texto_rect = texto.get_rect(center=(ancho // 2, alto // 2))
        pantalla.blit(texto, texto_rect)
        texto = fuente.render(
            "Presiona cualquier tecla para reiniciar", True, blanco)
        texto_rect = texto.get_rect(center=(ancho // 2, alto // 2 + 40))
        pantalla.blit(texto, texto_rect)

    pygame.display.flip()
    reloj.tick(60)
