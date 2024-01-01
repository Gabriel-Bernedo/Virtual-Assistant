from auxiliar import *
# from juegos.quizApp import *
# from utils_audio import *
# from ui import *
import pygame
from multiprocessing import Process
import sys
import asyncio

'''def programa():
    txtToAudio(datos['bienvenida'])
    print("Di tu nombre: ")
    #nombre = asyncio.run(escuchar()).capitalize()
    nombre = enviar_voz().capitalize()
    txtToAudio(f"Hola {nombre}. Mucho gusto.")
    asyncio.run(hablar(f"{nombre} Ahora voy a explicarte sobre las opciones que tiene este programa. Tienes 3 opciones para escoger."))
    asyncio.run(hablar(
        "La opción Aprendizaje es donde podrás aprender todo con respecto a la Estructura de un computador. La opción Pruebas es donde podrás poner en práctica lo que aprendiste mediante exámenes. Y por último, la tercer opción, es Juegos, donde tambien podrás demostrar lo que aprendiste jugando."))
    while True:
        asyncio.run(hablar("¿Qué opción eliges? "))
        asyncio.run(hablar(" 1) Aprendizaje\n 2) Pruebas\n 3) Juegos\n 4) Salir"))
        respuesta = asyncio.run(escuchar())
        if respuesta == "aprendizaje":
            asyncio.run(hablar("Elegiste la opcion APRENDIZAJE."))
            while True:
                asyncio.run(hablar("Que seccion deseas aprender\n 1) Introduccion\n 2) Repertorio de instrucciones\n 3) "
                              "Modos de direccionamiento\n 4) Salir"))
                respuesta = asyncio.run(escuchar())
                if respuesta == "introducción":
                    aprender('introduccion')
                elif respuesta == "repertorio de instrucciones":
                    asyncio.run(hablar("Escogiste Repertorio de instrucciones"))
                    while True:
                        asyncio.run(hablar("Deseas la seccion\n 1) General\n 2) Instrucciones\n 3) Ambas\n 4) Salir"))
                        respuesta = asyncio.run(escuchar())
                        all = respuesta == "ambas"
                        if respuesta == "general" or all:
                            aprender('repertorio', 'general')
                        if respuesta == "instrucciones" or all:
                            aprender('repertorio', 'instrucciones')
                        if respuesta == "salir":
                            break
                        else:
                            asyncio.run(hablar("repite la opcion por favor"))
                elif respuesta == "modos de direccionamiento":
                    asyncio.run(hablar("Escogiste modos de direccionamiento"))
                    while True:
                        asyncio.run(hablar(
                            "Deseas la seccion\n 1) General\n 2) Primera seccion\n 3) Segunda seccion\n 4) Tercera seccione\n 5) Salir"))
                        respuesta = asyncio.run(escuchar())
                        if respuesta == "general":
                            aprender('modos', 'general')
                        elif respuesta.__contains__("primera"):
                            aprender('modos', '1')
                        elif respuesta.__contains__("segunda"):
                            aprender('modos', '2')
                        elif respuesta.__contains__("tercera"):
                            aprender('modos', '3')
                        elif respuesta == "salir":
                            break
                        else:
                            asyncio.run(hablar("repite la opcion por favor"))
                elif respuesta == "salir":
                    break
                else:
                    asyncio.run(hablar("repite la opcion por favor"))
            break
        elif respuesta == "pruebas":
            asyncio.run(hablar("Elegiste la opción PRUEBAS."))
            asyncio.run(hablar("¿Por cual deseas empezar?"))
            while True:
                asyncio.run(hablar(
                    "Deseas dar una prueba sobre\n 1) Introduccion\n 2) Repertorio de instrucciones\n 3) Modos de direccionamiento\n 4) Salir"))
                respuesta = asyncio.run(escuchar())
                print("rpta " + respuesta)
                if respuesta == "introducción":
                    asyncio.run(hablar("Escogiste introduccion\nEmpezemos con la prueba:"))
                    dictarpreguntas("introduccion")
                elif respuesta == "repertorio de instrucciones":
                    asyncio.run(hablar("Escogiste Repertorio de instrucciones"))
                    while True:
                        asyncio.run(hablar("Deseas la seccion\n 1) General\n 2) Instrucciones\n 3) Salir"))
                        respuesta = asyncio.run(escuchar())
                        if respuesta == "general":
                            dictarpreguntas('repertorio', 'general')
                        elif respuesta == "instrucciones":
                            dictarpreguntas('repertorio', 'instrucciones')
                        elif respuesta == "salir":
                            break
                        else:
                            asyncio.run(hablar("repite la opcion por favor"))
                elif respuesta == "modos de direccionamiento":
                    while True:
                        asyncio.run(hablar("Escogiste Repertorio de instrucciones"))
                        asyncio.run(hablar(
                            "Deseas la seccion\n 1) General\n 2) Primera seccion\n 3) Segunda seccion\n 4) Tercera seccion\n 5)Salir"))
                        respuesta = asyncio.run(escuchar())
                        if respuesta == "general":
                            dictarpreguntas('modos', 'general')
                        elif respuesta == "primera seccion":
                            dictarpreguntas('modos', '1')
                        elif respuesta == "segunda sección":
                            dictarpreguntas('modos', '2')
                        elif respuesta == "tercera sección":
                            dictarpreguntas('modos', '3')
                        elif respuesta == "salir":
                            break
                        else:
                            asyncio.run(hablar("repite la opcion por favor"))
                elif respuesta == "salir":
                    break
                else:
                    asyncio.run(hablar("repite la opcion por favor"))
        elif respuesta == "juegos":
            asyncio.run(hablar("Elegiste la opción JUEGOS."))
            asyncio.run(hablar(
                "El primer juego consta en contestar las preguntas, haciendo click en la imagen que crees que es la respuesta."))
            if __name__ == "__main__":
                root = tk.Tk()
                app = ComputerStructureQuizApp(root)
                root.mainloop()
        elif respuesta == "salir":
            break
        else:
            asyncio.run(hablar(
                nombre + " creo que no has respondido con alguna de las instrucciones indicadas anteriormente"))
            asyncio.run(hablar("Responde con una de las alternativas mencionadas."))'''

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CELESTE = (114, 157, 174)
CELESTE = (85, 201, 245)
#CELESTE = RED#para diferenciar
size = (600, 600)  # ancho,alto

screen = pygame.display.set_mode(size)
screen.fill(WHITE)
pygame.display.flip()
pygame.display.set_caption('PYG4 Asistente Virtual')
pygame.display.set_icon(pygame.image.load("img/fondo.jpg"))
clock = pygame.time.Clock()
fondo = pygame.image.load('img/fondo.jpg').convert()#600x600px
micro = pygame.image.load('img/micro.png').convert_alpha()#120x120px
from utils_audio import *


def programa():
    txtToAudio(datos['bienvenida'])
    #hablando[0] = False
    nombre = enviar_voz().capitalize()
    txtToAudio(f"Hola {nombre}. Mucho gusto.")
    nombre = enviar_voz()
    estado['termino'] = True


fuente = pygame.font.SysFont('segoe print', 20)
texto = fuente.render('Pyg4 Tu Asistente Virtual', True, WHITE)


def asistentePyg():
    import threading
    modo = True
    hilo1 = threading.Thread(target=programa)
    hilo1.start()
    while not estado['termino']:
        # print('iterando')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(fondo, (0, 0))
        if estado['hablando']:
            ancho = 70
            if modo:#185-120 = x,y 405 -> 220 -> 210
                alto = 150
                pygame.draw.ellipse(screen, RED, (185, 140, ancho, alto-40))
                pygame.draw.ellipse(screen, BLUE, (260, 120, ancho, alto))
                pygame.draw.ellipse(screen, GREEN, (335, 140, ancho, alto-40))
            else:
                alto = 90
                pygame.draw.ellipse(screen, RED, (185, 140, ancho, alto+40))
                pygame.draw.ellipse(screen, BLUE, (260, 160, ancho, alto))
                pygame.draw.ellipse(screen, GREEN, (335, 140, ancho, alto+40))
            modo = not modo
        elif estado['escuchando']:#120+150=270/2=135
            ancho = 70
            if modo:  # 185-120 = x,y 405 -> 220 -> 2109
                alto = 150
                pygame.draw.circle(screen, CELESTE, (295, 230),80)
            modo = not modo
            screen.blit(micro, (235, 170))
            #pygame.draw.rect(screen, BLUE, (185, 255, 220, 10))
        screen.blit(texto, (10, 10))
        pygame.display.flip()
        clock.tick(2.5)


asistentePyg()
