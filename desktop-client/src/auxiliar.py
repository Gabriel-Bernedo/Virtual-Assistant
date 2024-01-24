import pygame

from utils_audio import *
from juegos import *

with open('res/db/basedatos.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)
aprendizaje, imagenes = datos['aprendizaje'], datos['img']
with open('res/db/preguntas.json', 'r', encoding='utf-8') as archivo:
    preguntas = json.load(archivo)
dicc = {
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
    if not subseccion is None:
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
        while True:  # uno-dos
            rpta = escuchar()
            if rpta.isdigit() and int(rpta) > 0 and int(rpta) < cont:
                if int(rpta) == resul:
                    dicc['puntaje'] += 1
                    decir("respuesta correcta")
                else:
                    decir("respuesta incorrecta")
                break
            elif rpta in dicc and dicc[rpta] > 0 and dicc[rpta] < cont:
                if resul == dicc[rpta]:
                    dicc['puntaje'] += 1
                    decir("respuesta correcta")
                else:
                    decir("respuesta incorrecta")
                break
            else:
                decir("la respuesta debe estar en el rango")
    decir("En esta seccion tu puntaje es de " + str(dicc['puntaje']) + " sobre " + str(len(arr)))
    dicc['puntaje'] = 0


def aprender(seccion, subseccion=None):
    info, imgs = aprendizaje[seccion], imagenes[seccion]
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
        time.sleep(3)


def generar_mensaje_secciones(secciones):
    return "\n".join([f"{i + 1}) {seccion}" for i, seccion in enumerate(secciones)] + [f"{len(secciones) + 1}) Salir"])
def aprenderElseProbar(aprendiendo=True):
    decir(f"Elegiste la opcion {"Aprendizaje" if aprendiendo else "Pruebas"}")
    while not estado['fin_hilo']:
        mensaje_pregunta = "Que seccion deseas aprender\n" if aprendiendo else "Deseas dar una prueba sobre\n"
        decir(mensaje_pregunta + generar_mensaje_secciones(aprendizaje))
        #aqui cierro la ventana
        respuesta = escuchar()
        equivocado = True
        if not estado['fin_hilo']:
            for seccion in aprendizaje:
                if not estado['fin_hilo']:
                    if any(palabra in seccion for palabra in respuesta.split() if len(palabra) > 3):#escoger seccion
                        equivocado = False
                        if not estado['fin_hilo']:
                            if isinstance(aprendizaje[seccion], dict) and len(seccion) > 1:
                                aprenderElseProbarSubseccion(seccion, aprendiendo)
                            else:
                                aprender(seccion) if aprendiendo else dictarpreguntas(seccion)
                            break
                        else:
                            break
                else: break
        if respuesta == 'salir':
            break
        elif equivocado:
            decir("repite la opcion por favor")


def aprenderElseProbarSubseccion(seccion, aprendiendo=True):
    decir(f"Ahora aprenderas {seccion}" if aprendiendo else f"Escogiste {seccion}, empecemos con la prueba")
    while not estado['fin_hilo']:
        decir(f"En cual subseccion deseas {'aprender'if aprendiendo else 'dar una prueba'}\n" + generar_mensaje_secciones(aprendizaje[seccion]))
        respuesta = escuchar()
        equivocado = True
        for subseccion in aprendizaje[seccion]:
            if not estado['fin_hilo']:
                if any(palabra in subseccion for palabra in respuesta.split()):#escoger seccion
                    equivocado = False
                    aprender(seccion,subseccion) if aprendiendo else dictarpreguntas(seccion,subseccion)
            else: break
        if respuesta == 'salir':
            break
        elif equivocado:
            decir("repite la opcion por favor")

def cargarimg(img):
    if not img == "":
        image_path = "res/imgs/" + img  # Ruta de la imagen que deseas abrir
        if not img.__contains__(".png"):
            image_path += ".png"
        img_path[0] = image_path

class Interfaz:
    def __init__(self):
        pygame.init()
        self.fondo = pygame.image.load('res/imgs/fondo.jpg')  # 600x600px

        self.max_alto = 150
        self.min_alto = 90

        self.alto1 = self.max_alto
        self.alto2 = self.min_alto

        self.y1 = 140
        self.y2 = 160

        self.sizeF = (self.fondo.get_width(), self.fondo.get_height())  # ancho,alto
        pygame.display.set_mode(self.sizeF)

        self.micro = pygame.image.load('res/imgs/micro.png').convert_alpha()  # 120x120px
        self.load = [pygame.image.load('res/imgs/load.png').convert_alpha()]  # 140x140px

        self.fuente = pygame.font.SysFont('segoe print', 20)
        self.fuenteSub = pygame.font.SysFont('segoe print', 11)
        self.pygTxt = self.fuente.render('PYG-4 Tu Asistente Virtual', True, WHITE)
        pygame.display.flip()
        self.modo = True
def interfaz():
    ventana = Interfaz()
    ventana.__init__()

    def parrafo(altura):
        if len(subTxt[0]) >0:
            oraciones = dividir_texto(subTxt[0], 38)
            for i, oracion in enumerate(oraciones):
                txtAyuda = ventana.fuenteSub.render(oracion, True, BLACK)
                screen.blit(txtAyuda, (185, altura + (17 * i)))
    inactivo = False
    while not estado['termino']:
        ventana.__init__()
        screen = pygame.display.set_mode(ventana.sizeF)
        while estado['asistente']:
            inactivo = False
            pygame.display.set_icon(ventana.fondo)
            pygame.display.set_caption('PYG-4')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    estado['termino'], estado['asistente'] = True, False
            screen.blit(ventana.fondo, (0, 0))
            if estado['hablando']:
                ancho = 70
                if ventana.modo:  # 185-120 = x,y 405 -> 220 -> 210
                    ventana.alto1 -= 2
                    ventana.alto2 += 2
                    ventana.y1 += 1
                    ventana.y2 -= 1

                    # print(alto1, alto2, y1)
                    if ventana.alto1 == ventana.min_alto:
                        ventana.modo = not ventana.modo

                    pygame.draw.ellipse(screen, RED, (185, ventana.y1, ancho, ventana.alto1))
                    pygame.draw.ellipse(screen, BLUE, (260, ventana.y2, ancho, ventana.alto2))
                    pygame.draw.ellipse(screen, GREEN, (335, ventana.y1, ancho, ventana.alto1))
                else:
                    ventana.alto1 += 2
                    ventana.alto2 -= 2
                    ventana.y1 -= 1
                    ventana.y2 += 1

                    if ventana.alto1 == ventana.max_alto:
                        ventana.modo = not ventana.modo

                    pygame.draw.ellipse(screen, RED, (185, ventana.y1, ancho, ventana.alto1))
                    pygame.draw.ellipse(screen, BLUE, (260, ventana.y2, ancho, ventana.alto2))
                    pygame.draw.ellipse(screen, GREEN, (335, ventana.y1, ancho, ventana.alto1))
                parrafo(285)
                clock.tick(60)

            elif estado['escuchando']:  # 120+150=270/2=135
                if ventana.modo:  # 185-120 = x,y 405 -> 220 -> 2109
                    pygame.draw.circle(screen, CELESTE, (295, 230), 80)
                ventana.modo = not ventana.modo
                screen.blit(ventana.micro, (235, 170))
                parrafo(305)
                clock.tick(2)
            else:
                screen.blit(ventana.load[0], (235, 170))
                ventana.load[0] = pygame.transform.rotate(ventana.load[0], 90)
                parrafo(305)
                clock.tick(1.5)
            screen.blit(ventana.pygTxt, (10, 10))
            pygame.display.flip()
        while estado['jugando']:
            inactivo = True
            ahorcado()
            estado['asistente'] = True
        while estado['aprendiendo']:
            inactivo = False
            imagen = pygame.image.load(img_path[0])
            size = (imagen.get_width(), imagen.get_height())
            screen = pygame.display.set_mode(size)
            screen.blit(imagen, (0, 0))
            pygame.display.flip()
            time.sleep(3)
            estado['asistente'] = True
            estado['aprendiendo']=False
        while estado['query']:
            if not inactivo:
                pygame.quit()
                print('sali')
                inactivo = True

