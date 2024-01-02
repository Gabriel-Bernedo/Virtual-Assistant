from auxiliar import *
import threading
# from juegos.quizApp import *
from utils_audio import *
import sys

def programa():
    decir(datos['bienvenida'][0])
    print("Di tu nombre: ")
    nombre = escuchar().capitalize()
    decir(f"Hola {nombre}. Mucho gusto.")
    decir(f"{nombre} Ahora voy a explicarte sobre las opciones que tiene este programa. Tienes 3 opciones para escoger.")
    decir("La opción Aprendizaje es donde podrás aprender todo con respecto a la Estructura de un computador. "
               "La opción Pruebas es donde podrás poner en práctica lo que aprendiste mediante exámenes. "
               "Y por último, la tercer opción, es Juegos, donde tambien podrás demostrar lo que aprendiste jugando.")
    while True:
        decir("¿Qué opción eliges? ")
        decir(" 1) Aprendizaje\n 2) Pruebas\n 3) Juegos\n 4) Salir")
        respuesta = escuchar()
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
            decir("Elegiste la opción JUEGOS.")
            decir(
                "El primer juego consta en contestar las preguntas, haciendo click en la imagen que crees que es la respuesta.")
            if __name__ == "__main__":
                '''root = tk.Tk()
                app = ComputerStructureQuizApp(root)
                root.mainloop()'''
                print('ingresaste a juegos')
        elif respuesta == "salir":
            break
        else:
            decir(
                nombre + " creo que no has respondido con alguna de las instrucciones indicadas anteriormente")
            decir("Responde con una de las alternativas mencionadas.")

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CELESTE = (85, 201, 245)
size = (600, 600)  # ancho,alto

screen = pygame.display.set_mode(size)
screen.fill(WHITE)
pygame.display.flip()
pygame.display.set_caption('PYG-4')
pygame.display.set_icon(pygame.image.load("img/fondo.jpg"))
clock = pygame.time.Clock()
fondo = pygame.image.load('img/fondo.jpg').convert()#600x600px
micro = pygame.image.load('img/micro.png').convert_alpha()#120x120px
load = [pygame.image.load('img/load.png').convert_alpha()]#140x140px

fuente = pygame.font.SysFont('segoe print', 20)
pygTxt = fuente.render('PYG-4 Tu Asistente Virtual', True, WHITE)

def asistentePyg():#INTERFAZ grafica
    modo = True
    hilo1 = threading.Thread(target=programa)
    hilo1.start()
    while not estado['termino']:
        subtitulos = fuente.render(subTxt[0], True, WHITE)
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
asistentePyg()
