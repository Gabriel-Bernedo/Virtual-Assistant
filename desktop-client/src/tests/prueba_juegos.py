import pygame
import sys
import random


pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CELESTE = (85, 201, 245)
clock = pygame.time.Clock()

fondo = pygame.image.load('../img/pizarra.png')#512x267px
size = (fondo.get_width(), fondo.get_height())
screen = pygame.display.set_mode(size)
pygame.display.set_caption('AHORCADO')
pygame.display.set_icon(fondo)

fuente = pygame.font.SysFont('segoe print', 20)
estado={'termino' : False}
# Palabras para adivinar
palabras = ["PYTHON", "PROGRAMACION", "VIDEOJUEGO", "AHORCADO", "GITHUB", "INTELIGENCIA"]
max_intentos = 6
palabra_secreta = random.choice(palabras)
letras_adivinadas = ["_"] * len(palabra_secreta)
partes = [
    ((140,105),15),#cabeza
    ((140,120),(140,170)),#cuerpo
    ((140,170),(160,190)),#pie der
    ((140,170),(120,190)),#pie izq
    ((140,130),(160,150)),#brazo der
    ((140,130),(120,150)),#b izq

]
def circle(center,r):
    pygame.draw.circle(screen,BLACK,center,r,3)
def linea(ini,fin):
    pygame.draw.line(screen, BLACK,ini,fin, 3)
def horca():
    pygame.draw.rect(screen, WHITE, (30, 207, 100, 15))
    pygame.draw.rect(screen, WHITE, (70, 80, 10, 127))
    pygame.draw.rect(screen, WHITE, (80, 80, 60, 10))

def asistentePyg():#INTERFAZ grafica

    intentos = 0
    while not estado['termino']:
        screen.blit(fondo,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado['termino'] = True
                sys.exit()
        horca()

        palabra_oculta = " ".join(letras_adivinadas)
        texto_palabra = fuente.render(palabra_oculta, True, BLACK)
        screen.blit(texto_palabra, (170, 195))


        # Verificar si se adivinó la palabra
        if "_" not in letras_adivinadas:
            texto_ganar = fuente.render("¡Ganaste!", True, BLACK)
            screen.blit(texto_ganar, (140, 180))
        elif intentos >= max_intentos:
            texto_perder = fuente.render("¡Perdiste! La palabra era: " + palabra_secreta, True, BLACK)
            screen.blit(texto_perder, (140, 180))
        else:
            # Dibujar teclado
            '''for i in range(26):
                letra = chr(ord("A") + i)
                pygame.draw.rect(screen, BLACK, (50 + i * 30, 100, 25, 25), 2)
                texto_letra = fuente.render(letra, True, BLACK)
                screen.blit(texto_letra, (60 + i * 30, 105))
'''
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
        if intentos > 0:
            circle(partes[0][0], partes[0][1])
            if intentos > 1:
                for i in range(1,intentos):
                    linea(partes[i][0], partes[i][1])
        clock.tick(10)
        pygame.display.flip()


asistentePyg()
