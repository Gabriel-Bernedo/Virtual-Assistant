import pygame
import sys
import random
import time
from utils_audio import estado

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CELESTE = (85, 201, 245)
clock = pygame.time.Clock()

'''
estado={'enPartida' : False,
        'jugando':True}
'''
# Palabras para adivinar
palabras = ["PYTHON", "PROGRAMACION", "VIDEOJUEGO", "AHORCADO", "GITHUB", "INTELIGENCIA"]
max_intentos = 6

partes = [
    ((140, 105), 15),  # cabeza
    ((140, 120), (140, 170)),  # cuerpo
    ((140, 170), (160, 190)),  # pie der
    ((140, 170), (120, 190)),  # pie izq
    ((140, 130), (160, 150)),  # brazo der
    ((140, 130), (120, 150)),  # b izq

]


def ahorcado():  # INTERFAZ grafica
    fuente = pygame.font.SysFont('segoe print', 20)
    pizarra = pygame.image.load('img/pizarra.png')  # 512x267px
    tamanio = (pizarra.get_width(), pizarra.get_height())
    pantalla = pygame.display.set_mode(tamanio)
    pygame.display.set_caption('AHORCADO')
    pygame.display.set_icon(pizarra)

    def circle(center, r):
        pygame.draw.circle(pantalla, BLACK, center, r, 3)

    def linea(ini, fin):
        pygame.draw.line(pantalla, BLACK, ini, fin, 3)

    def horca():
        pygame.draw.rect(pantalla, WHITE, (30, 207, 100, 15))
        pygame.draw.rect(pantalla, WHITE, (70, 80, 10, 127))
        pygame.draw.rect(pantalla, WHITE, (80, 80, 60, 10))

    def preguntar_continuar():
        font = pygame.font.Font(None, 36)
        pregunta_texto = font.render("¿Deseas continuar? (Sí/No)", True, (0, 0, 0))
        pregunta_rect = pregunta_texto.get_rect(center=(pantalla.get_width() // 2, pantalla.get_height() // 2))

        while True:
            pantalla.fill((255, 255, 255))
            pantalla.blit(pregunta_texto, pregunta_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        return True
                    elif event.key == pygame.K_n:
                        return False

    while estado['jugando']:
        palabra_secreta = random.choice(palabras)
        print(palabra_secreta)
        letras_adivinadas = ["_"] * len(palabra_secreta)
        estado['enPartida'] = False
        intentos = 0
        while not estado['enPartida']:
            pantalla.blit(pizarra, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    estado['enPartida'] = True
                    sys.exit()
            horca()

            palabra_oculta = " ".join(letras_adivinadas)
            texto_palabra = fuente.render(palabra_oculta, True, BLACK)

            # Verificar si se adivinó la palabra
            if "_" not in letras_adivinadas:
                texto_ganar = fuente.render("¡Ganaste!", True, BLACK)
                pantalla.blit(texto_ganar, (140, 180))
                estado['enPartida'] = True
            elif intentos >= max_intentos:
                texto_perder = fuente.render("¡Perdiste! La palabra era: ", True, BLACK)
                texto_perder2 = fuente.render(palabra_secreta, True, BLACK)
                pantalla.blit(texto_perder, (140, 160))
                pantalla.blit(texto_perder2, (140, 200))
                estado['enPartida'] = True
            else:
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
            if intentos > 0 and not estado['enPartida']:
                circle(partes[0][0], partes[0][1])
                if intentos > 1:
                    for i in range(1, intentos):
                        linea(partes[i][0], partes[i][1])
            pantalla.blit(texto_palabra, (170, 195))
            clock.tick(10)
            pygame.display.flip()
        time.sleep(3)
        if preguntar_continuar():
            estado['jugando'] = True
        else:
            estado['jugando'] = False


def drawKeyboard():
    # Dibujar teclado
    '''for i in range(26):
        letra = chr(ord("A") + i)
        pygame.draw.rect(screen, BLACK, (50 + i * 30, 100, 25, 25), 2)
        texto_letra = fuente.render(letra, True, BLACK)
        screen.blit(texto_letra, (60 + i * 30, 105))
'''
    print(1)
