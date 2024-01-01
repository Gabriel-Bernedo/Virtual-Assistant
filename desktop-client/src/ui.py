import asyncio
import sys
import time

import pygame
pygame.init()
BLACK = (0,0,0)
WHITE= (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

size = (800,500)#ancho,alto

screen = pygame.display.set_mode(size)
fuente = pygame.font.SysFont('segoe print', 20)
texto = fuente.render('Subtitulo',True,RED)
hablando = [True]
clock = pygame.time.Clock()  # Crear un reloj de pygame

def asistentePyg():
    modo = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(WHITE)
        screen.blit(texto, (10, 10))

        if hablando[0]:
            if modo:
                pygame.draw.ellipse(screen, BLUE, (0, 0, 100, 300))
                pygame.draw.ellipse(screen, BLUE, (204, 0, 100, 300))
                pygame.draw.ellipse(screen, BLUE, (102, 0, 100, 300))
                pygame.display.flip()
            else:
                pygame.draw.ellipse(screen, BLUE, (0, 0, 100, 200))
                pygame.draw.ellipse(screen, BLUE, (102, 0, 100, 200))
                pygame.draw.ellipse(screen, BLUE, (204, 0, 100, 200))
                pygame.display.flip()
            modo = not modo
        else:
            pygame.draw.line(screen, BLUE, (20, 50), (100, 50))
            pygame.display.flip()

        clock.tick(1)  # Establecer la velocidad de actualización (1 FPS en este caso)

    #print('fdfsf')
asistentePyg()