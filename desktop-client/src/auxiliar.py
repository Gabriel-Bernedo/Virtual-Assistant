import json
import time

from utils_audio import *
from juegos import *


with open('basedatos.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)

with open('preguntas.json', 'r', encoding='utf-8') as archivo:
    preguntas = json.load(archivo)

dict = {
    "puntaje": 0,
    "uno": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5
}
img_path = ['']


def dictarpreguntas(seccion, subseccion=None):
    resul, arr = 0, preguntas[seccion]
    if not subseccion == None:
        arr = arr[subseccion]
    for pregunta in arr:
        cont = 1
        decir("Pregunta numero " + pregunta)
        for alternativa in arr[pregunta]:
            if arr[pregunta][alternativa] == 1:
                resul = cont
            decir(str(cont) + ") " + alternativa)
            cont += 1
        decir("Dicta el numero de opcion que creas que es correcta")
        while True:#uno-dos
            rpta = escuchar()
            if rpta.isdigit() and int(rpta) > 0 and int(rpta) < cont:
                if int(rpta) == resul:
                    dict['puntaje'] += 1
                    decir("respuesta correcta")
                else:
                    decir("respuesta incorrecta")
                break
            elif rpta in dict and dict[rpta] > 0 and dict[rpta] < cont:
                if resul == dict[rpta]:
                    dict['puntaje'] += 1
                    decir("respuesta correcta")
                else:
                    decir("respuesta incorrecta")
                break
            else:
                decir("la respuesta debe estar en el rango")
    decir("En esta seccion tu puntaje es de " + str(dict['puntaje']) + " sobre " + str(len(arr)))
    dict['puntaje'] = 0


def aprender(seccion, subseccion=None):
    info, imgs = datos['aprendizaje'][seccion], datos['img'][seccion]
    if not subseccion == None:
        info = info[subseccion]
        imgs = imgs[subseccion]
    else:
        decir("Escogiste " + seccion)
    for dato, img in zip(info, imgs):
        decir(dato)
        estado['asistente'] = False
        estado['aprendiendo'] = True
        cargarimg(img)
        print('siguiente dato')
        time.sleep(3)

def cargarimg(img):
    if not img == "":
        image_path = "img/" + img  # Ruta de la imagen que deseas abrir
        if not img.__contains__(".png"):
            image_path += ".png"
        img_path[0] = image_path

def interfaz():
    pygame.init()
    fondo = pygame.image.load('img/fondo.jpg')  # .convert()#600x600px

    sizeF = (fondo.get_width(), fondo.get_height())  # ancho,alto
    pygame.display.set_mode(sizeF)

    micro = pygame.image.load('img/micro.png').convert_alpha()  # 120x120px
    load = [pygame.image.load('img/load.png').convert_alpha()]  # 140x140px

    fuente = pygame.font.SysFont('segoe print', 20)
    fuenteSub = pygame.font.SysFont('segoe print', 11)
    pygTxt = fuente.render('PYG-4 Tu Asistente Virtual', True, WHITE)
    pygame.display.flip()
    modo = True
    while not estado['termino']:
        screen = pygame.display.set_mode(sizeF)

        while estado['asistente']:
            pygame.display.set_icon(fondo)
            pygame.display.set_caption('PYG-4')
            subtitulos = fuenteSub.render(subTxt[0], True, BLACK)
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
            screen.blit(subtitulos, (185, 280))
            pygame.display.flip()
        while estado['jugando']:
            ahorcado()
            estado['jugando'] = False
            estado['asistente'] = True
        while estado['aprendiendo']:
            imagen = pygame.image.load(img_path[0])
            size = (imagen.get_width(), imagen.get_height())
            screen = pygame.display.set_mode(size)
            screen.blit(imagen, (0, 0))
            pygame.display.flip()
            time.sleep(3)
            print('termino de aprender')
            estado['asistente'] = True
            estado['aprendiendo'] = False
