import pygame
import sys
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CELESTE = (85, 201, 245)
#size = (600, 600)  # ancho,alto

#screen.fill(WHITE)
clock = pygame.time.Clock()

fondo = pygame.image.load('../img/pizarra.png')#.convert()#512x267px
size = (fondo.get_width(), fondo.get_height())
screen = pygame.display.set_mode(size)
pygame.display.set_caption('AHORADOS')
pygame.display.set_icon(fondo)
pygame.display.flip()

fuente = pygame.font.SysFont('segoe print', 20)
pygTxt = fuente.render('PYG-4 Tu Asistente Virtual', True, WHITE)
estado={'termino' : False}
def asistentePyg():#INTERFAZ grafica
    modo = True
    while not estado['termino']:
        #subtitulos = fuente.render(subTxt[0], True, WHITE)
        # print('iterando')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado['termino'] = True
                sys.exit()
        if modo == True:
            screen.blit(fondo, (0, 0))
            #pygame
            pygame.draw.rect(screen, WHITE, (30, 207, 100, 15))
            pygame.draw.rect(screen, WHITE, (70, 80, 10, 127))
            pygame.draw.rect(screen, WHITE, (80, 80, 60, 10))
            #print('dasd')
            modo = False
        #else:
            #screen.blit(fondo, (0, 0))
        clock.tick(1)
        #screen.blit(subtitulos, (185, 160))
        pygame.display.flip()
asistentePyg()
