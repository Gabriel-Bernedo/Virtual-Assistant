import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego del Ahorcado")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuente
font = pygame.font.Font(None, 36)

# Palabras para adivinar
palabras = ["PYTHON", "PROGRAMACION", "VIDEOJUEGO", "AHORCADO", "GITHUB", "INTELIGENCIA"]

# Seleccionar una palabra al azar
palabra_secreta = random.choice(palabras)
letras_adivinadas = ["_"] * len(palabra_secreta)
intentos = 0
max_intentos = 6

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Dibujar fondo
    screen.fill(WHITE)

    # Dibujar palabra oculta
    palabra_oculta = " ".join(letras_adivinadas)
    texto_palabra = font.render(palabra_oculta, True, BLACK)
    screen.blit(texto_palabra, (250, 300))

    # Dibujar intentos restantes
    texto_intentos = font.render(f"Intentos restantes: {max_intentos - intentos}", True, BLACK)
    screen.blit(texto_intentos, (250, 400))

    # Verificar si se adivinó la palabra
    if "_" not in letras_adivinadas:
        texto_ganar = font.render("¡Ganaste!", True, BLACK)
        screen.blit(texto_ganar, (250, 500))
    elif intentos >= max_intentos:
        texto_perder = font.render("¡Perdiste! La palabra era: " + palabra_secreta, True, BLACK)
        screen.blit(texto_perder, (250, 500))
    else:
        # Dibujar teclado
        for i in range(26):
            letra = chr(ord("A") + i)
            pygame.draw.rect(screen, BLACK, (50 + i * 30, 100, 25, 25), 2)
            texto_letra = font.render(letra, True, BLACK)
            screen.blit(texto_letra, (60 + i * 30, 105))

        # Obtener teclas presionadas
        keys = pygame.key.get_pressed()
        for i in range(26):
            if keys[pygame.K_a + i]:
                letra = chr(ord("A") + i)
                if letra not in palabra_secreta:
                    intentos += 1
                else:
                    for j, letra_palabra in enumerate(palabra_secreta):
                        if letra == letra_palabra:
                            letras_adivinadas[j] = letra

    # Actualizar pantalla
    pygame.display.flip()

    # Ajustar la velocidad de actualización
    pygame.time.Clock().tick(30)
