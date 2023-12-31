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
i = []
hablando = [True]
def asistentePyg():
    modo = True
    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(WHITE)
        if hablando:
            if modo:
                #pygame.draw.ellipse(screen, GREEN, (0,0,100,200))#x1,y1, ancho, alto
                pygame.draw.ellipse(screen, BLUE, (0,0,100,300))
                pygame.draw.ellipse(screen, BLUE, (204,00,100,300))
                pygame.draw.ellipse(screen, BLUE, (102,00,100,300))
                pygame.display.flip()
            else:
                pygame.draw.ellipse(screen, BLUE, (0,0,100,200))
                pygame.draw.ellipse(screen, BLUE, (102,00,100,200))
                pygame.draw.ellipse(screen, BLUE, (204,00,100,200))
                pygame.display.flip()
            modo = not modo
        else:
            pygame.draw.line(screen, BLUE, (20,50),(100,50))
            pygame.display.flip()
        time.sleep(0.1)
#asyncio.run(asistentePyg())
#print('hola')