import pygame
import sys
import random
import time
from utils_audio import estado, repAudio
import json

with open('res/db/ahorcado.json', 'r', encoding='utf-8') as archivo:
    objJuego = json.load(archivo)
rpts = []
for rpta in objJuego:
    rpts.append(rpta)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CELESTE = (85, 201, 245)
clock = pygame.time.Clock()
palabras = rpts
max_intentos = 6

partes = [
    ((140, 105), 15),  # cabeza
    ((140, 120), (140, 170)),  # cuerpo
    ((140, 170), (160, 190)),  # pie der
    ((140, 170), (120, 190)),  # pie izq
    ((140, 130), (160, 150)),  # brazo der
    ((140, 130), (120, 150)),  # b izq

]

# pygame.init()
dest = [195, 25]


def dividir_texto(texto, longitud_maxima):
    palabras = texto.split()
    oraciones = []
    oracion_actual = palabras[0]

    for palabra in palabras[1:]:
        if len(oracion_actual + ' ' + palabra) <= longitud_maxima:
            oracion_actual += ' ' + palabra
        else:
            oraciones.append(oracion_actual)
            oracion_actual = palabra

    oraciones.append(oracion_actual)
    return oraciones


def ahorcado():  # INTERFAZ grafica
    fuente = pygame.font.SysFont('segoe print', 18)
    minFont = pygame.font.SysFont('segoe print', 13)
    pizarra = pygame.image.load('res/imgs/pizarra.png')  # 512x267px
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

    def parrafo():
        oraciones = dividir_texto(txt, 40)
        for i, oracion in enumerate(oraciones):
            txtAyuda = minFont.render(oracion, True, BLACK)
            pantalla.blit(txtAyuda, (195, 25 * (i + 1)))

    def preguntar_continuar():
        font = pygame.font.SysFont('segoe print', 25)
        pregunta_texto = font.render("¿Deseas continuar? (Sí/No)", True, BLACK)
        pregunta_rect = pregunta_texto.get_rect(center=(pantalla.get_width() // 2, pantalla.get_height() // 2))

        while True:
            pantalla.blit(pizarra, (0, 0))
            pantalla.blit(pregunta_texto, pregunta_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        return True
                    elif event.key == pygame.K_n:
                        return False

    while estado['jugando']:
        palabra_secreta = random.choice(palabras)
        img_ayuda = pygame.image.load(f'res/imgs/juegos/{palabra_secreta}.jpg')
        imagen_rect = img_ayuda.get_rect()
        txt = objJuego[palabra_secreta]
        texto_secreto = fuente.render(palabra_secreta, True, BLACK)
        # print(palabra_secreta)
        letras_adivinadas = ["_"] * len(palabra_secreta)
        estado['enPartida'] = True
        intentos = 0

        def munieco():
            if intentos > 0 and estado['enPartida']:
                circle(partes[0][0], partes[0][1])
                if intentos > 1:
                    for i in range(1, intentos):
                        linea(partes[i][0], partes[i][1])

        while estado['enPartida']:
            letra = None
            pantalla.blit(pizarra, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    estado['enPartida'] = False
                    estado['jugando'] = False
                    #sys.exit()
                elif event.type == pygame.KEYUP:
                    letra = event.unicode
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        pos = (int(mouse_pos[0]) - int(dest[0]), int(mouse_pos[1]) - int(dest[1]))
                        if imagen_rect.collidepoint(pos):
                            estado['ayuda'] = not estado['ayuda']
            horca()
            palabra_oculta = " ".join(letras_adivinadas)
            texto_palabra = fuente.render(palabra_oculta, True, BLACK)
            munieco()
            if estado['ayuda']:
                parrafo()
            else:
                pantalla.blit(img_ayuda, dest)
            if "_" not in letras_adivinadas:
                texto_ganar = fuente.render("¡Ganaste!", True, BLACK)
                pantalla.blit(texto_ganar, (140, 175))
                estado['enPartida'] = False
                pantalla.blit(texto_secreto, (170, 195))
                pygame.display.flip()
                repAudio("res/audio/victoria.mp3")
            else:
                if intentos >= max_intentos:
                    texto_perder = fuente.render("¡Perdiste! La palabra era: ", True, BLACK)
                    pantalla.blit(texto_perder, (140, 160))
                    pantalla.blit(texto_secreto, (140, 195))
                    repAudio("res/audio/derrota.mp3")
                    estado['enPartida'] = False
                    pygame.display.flip()
                    continue
                else:
                    if letra is not None and letra.isalpha():
                        #print(letra)
                        letra = letra.upper()
                        if letra not in palabra_secreta:
                            intentos += 1
                        else:
                            for j, letra_palabra in enumerate(palabra_secreta):
                                if letra == letra_palabra:
                                    letras_adivinadas[j] = letra
                pantalla.blit(texto_palabra, (170, 195))
            clock.tick(15)
            pygame.display.flip()
        time.sleep(3)
        if estado['jugando']:
            estado['jugando'] = True if preguntar_continuar() else False
