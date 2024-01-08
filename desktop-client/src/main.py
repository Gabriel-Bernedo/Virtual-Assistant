import time

from auxiliar import *
import threading
from juegos import *
from utils_audio import *
import sys
def programa():
    decir(datos['bienvenida'][0])
    nombre = escuchar().capitalize()
    decir(f"Hola {nombre}. Mucho gusto.")
    #decir("Hola.")
    #estado['termino'] = True
    #time.sleep(1)
    #ahorcado()
    #return
    decir(f"{nombre} Ahora voy a explicarte sobre las opciones que tiene este programa. Tienes 3 opciones para escoger.")
    decir("La opción Aprendizaje es donde podrás aprender todo con respecto a la Estructura de un computador. "
               "La opción Pruebas es donde podrás poner en práctica lo que aprendiste mediante exámenes. "
               "Y por último, la tercer opción, es Juegos, donde tambien podrás demostrar lo que aprendiste jugando.")
    while True:
        decir("¿Qué opción eliges? ")
        decir(" 1) Aprendizaje\n 2) Pruebas\n 3) Juegos\n 4) Salir")
        respuesta = escuchar()
        #respuesta = 'juegos'
        if respuesta == "aprendizaje":
            decir("Elegiste la opcion APRENDIZAJE.")
            while True:
                decir("Que seccion deseas aprender\n 1) Introduccion\n 2) Repertorio de instrucciones\n 3) "
                              "Modos de direccionamiento\n 4) Salir")
                respuesta = escuchar()
                if respuesta == "introducción":
                    aprender('introduccion')
                elif respuesta == "repertorio de instrucciones":
                    decir("Escogiste Repertorio de instrucciones")
                    while True:
                        decir("Deseas la seccion\n 1) General\n 2) Instrucciones\n 3) Ambas\n 4) Salir")
                        respuesta = escuchar()
                        all = respuesta == "ambas"
                        if respuesta == "general" or all:
                            aprender('repertorio', 'general')
                        if respuesta == "instrucciones" or all:
                            aprender('repertorio', 'instrucciones')
                        if respuesta == "salir":
                            break
                        else:
                            decir("repite la opcion por favor")
                elif respuesta == "modos de direccionamiento":
                    decir("Escogiste modos de direccionamiento")
                    while True:
                        decir(
                            "Deseas la seccion\n 1) General\n 2) Primera seccion\n 3) Segunda seccion\n 4) Tercera seccione\n 5) Salir")
                        respuesta = escuchar()
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
                            decir("repite la opcion por favor")
                elif respuesta == "salir":
                    break
                else:
                    decir("repite la opcion por favor")
            break
        elif respuesta == "pruebas":
            decir("Elegiste la opción PRUEBAS.")
            decir("¿Por cual deseas empezar?")
            while True:
                decir(
                    "Deseas dar una prueba sobre\n 1) Introduccion\n 2) Repertorio de instrucciones\n 3) Modos de direccionamiento\n 4) Salir")
                respuesta = escuchar()
                print("rpta " + respuesta)
                if respuesta == "introducción":
                    decir("Escogiste introduccion\nEmpezemos con la prueba:")
                    dictarpreguntas("introduccion")
                elif respuesta == "repertorio de instrucciones":
                    decir("Escogiste Repertorio de instrucciones")
                    while True:
                        decir("Deseas la seccion\n 1) General\n 2) Instrucciones\n 3) Salir")
                        respuesta = escuchar()
                        if respuesta == "general":
                            dictarpreguntas('repertorio', 'general')
                        elif respuesta == "instrucciones":
                            dictarpreguntas('repertorio', 'instrucciones')
                        elif respuesta == "salir":
                            break
                        else:
                            decir("repite la opcion por favor")
                elif respuesta == "modos de direccionamiento":
                    while True:
                        decir("Escogiste Repertorio de instrucciones")
                        decir(
                            "Deseas la seccion\n 1) General\n 2) Primera seccion\n 3) Segunda seccion\n 4) Tercera seccion\n 5)Salir")
                        respuesta = escuchar()
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
                            decir("repite la opcion por favor")
                elif respuesta == "salir":
                    break
                else:
                    decir("repite la opcion por favor")
        elif respuesta == "juegos":
            decir("Ahora jugaras ahorcado")
            estado['asistente'] = False
            while not estado['asistente']:
                time.sleep(1)
        elif respuesta == "salir":
            break
        else:
            #decir(
            #    nombre + " creo que no has respondido con alguna de las instrucciones indicadas anteriormente")
            decir("Responde con una de las alternativas mencionadas.")
    estado['termino'] = True


def asistentePyg():#INTERFAZ grafica
    hilo1 = threading.Thread(target=programa)
    hilo1.start()
    interfaz()
def interfaz():
    pygame.init()
    fondo = pygame.image.load('img/fondo.jpg')  # .convert()#600x600px

    size = (fondo.get_width(), fondo.get_height())  # ancho,alto
    pygame.display.set_mode(size)

    micro = pygame.image.load('img/micro.png').convert_alpha()  # 120x120px
    load = [pygame.image.load('img/load.png').convert_alpha()]  # 140x140px

    fuente = pygame.font.SysFont('segoe print', 20)
    pygTxt = fuente.render('PYG-4 Tu Asistente Virtual', True, WHITE)
    pygame.display.flip()
    modo = True
    while not estado['termino']:
        screen = pygame.display.set_mode(size)

        while estado['asistente']:
            pygame.display.set_icon(fondo)
            pygame.display.set_caption('PYG-4')
            subtitulos = fuente.render(subTxt[0], True, WHITE)
            # print('iterando')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    estado['termino'] = True
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
                clock.tick(2.5)
                modo = not modo
            elif estado['escuchando']:#120+150=270/2=135
                if modo:  # 185-120 = x,y 405 -> 220 -> 2109
                    pygame.draw.circle(screen, CELESTE, (295, 230),80)
                modo = not modo
                screen.blit(micro, (235, 170))
                clock.tick(2)
            else:
                screen.blit(load[0], (235, 170))
                load[0] = pygame.transform.rotate(load[0], 90)
                clock.tick(1.5)
            screen.blit(pygTxt, (10, 10))
            screen.blit(subtitulos, (185, 160))
            pygame.display.flip()
        while not estado['asistente']:
            ahorcado()
            estado['jugando'] = True
            estado['asistente'] = True

asistentePyg()
