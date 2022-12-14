# Importamos la biblioteca Pygame
import pygame

# Inicializamos Pygame
pygame.init()

# Creamos la ventana del juego
ventana = pygame.display.set_mode((800, 600))

# Creamos los objetos del juego: la raqueta izquierda, la raqueta derecha y la pelota
raqueta_izquierda = pygame.Rect(20, 250, 20, 100)
raqueta_derecha = pygame.Rect(760, 250, 20, 100)
pelota = pygame.Rect(390, 290, 20, 20)

# Creamos las variables para el movimiento de la pelota
velocidad_x = 5
velocidad_y = 5

# Bucle principal del juego
while True:
    # Recorremos todos los eventos que ocurren en el juego
    for event in pygame.event.get():
        # Si se presiona la tecla de cierre de la ventana, salimos del juego
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizamos la posición de la pelota
    pelota.x += velocidad_x
    pelota.y += velocidad_y

    # Si la pelota choca contra un borde, cambiamos su dirección
    if pelota.top <= 0 or pelota.bottom >= 600:
        velocidad_y *= -1
    if pelota.left <= 0 or pelota.right >= 800:
        velocidad_x *= -1

    # Dibujamos los objetos en la pantalla
    ventana.fill((0, 0, 0))  # Limpiamos la pantalla
    pygame.draw.rect(ventana, (255, 255, 255), raqueta_izquierda)
    pygame.draw.rect(ventana, (255, 255, 255), raqueta_derecha)
    pygame.draw.rect(ventana, (255, 255, 255), pelota)

    # Actualizamos la pantalla
    pygame.display.flip()
