from utils_audio import *
from cartas import *

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
    if subseccion is not None:
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
            rpta2 = escuchar()
            if rpta2.isdigit() and 0 < int(rpta2) < cont:
                if int(rpta2) == resul:
                    dicc['puntaje'] += 1
                    decir("respuesta correcta")
                else:
                    decir("respuesta incorrecta")
                break
            elif rpta2 in dicc and 0 < dicc[rpta2] < cont:
                if resul == dicc[rpta2]:
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
    if subseccion is not None:
        info = info[subseccion]
        imgs = imgs[subseccion]
    else:
        decir("Escogiste " + seccion)
    for dato, img in zip(info, imgs):
        decir(dato)
        estado['asistente'] = False
        estado['aprendiendo'] = True
        cargarImg(img)
        time.sleep(3)


def generar_mensaje_secciones(secciones):
    return "\n".join([f"{i + 1}) {seccion}" for i, seccion in enumerate(secciones)] + [f"{len(secciones) + 1}) Salir"])


def aprenderElseProbar(aprendiendo=True):
    decir(f"Elegiste la opcion {"Aprendizaje" if aprendiendo else "Pruebas"}", False)
    while not estado['fin_hilo']:
        mensaje_pregunta = "Que seccion deseas aprender\n" if aprendiendo else "Deseas dar una prueba sobre\n"
        decir(mensaje_pregunta + generar_mensaje_secciones(aprendizaje))
        # aqui cierro la ventana
        respuesta = escuchar()
        equivocado = True
        if not estado['fin_hilo']:
            for seccion in aprendizaje:
                if not estado['fin_hilo']:
                    if any(palabra in seccion for palabra in respuesta.split() if len(palabra) > 3):  # escoger seccion
                        equivocado = False
                        if not estado['fin_hilo']:
                            if isinstance(aprendizaje[seccion], dict) and len(seccion) > 1:
                                aprenderElseProbarSubseccion(seccion, aprendiendo)
                            else:
                                aprender(seccion) if aprendiendo else dictarpreguntas(seccion)
                            break
                        else:
                            break
                else:
                    break
        if respuesta == 'salir':
            break
        elif equivocado:
            decir("repite la opcion por favor", False)


def aprenderElseProbarSubseccion(seccion, aprendiendo=True):
    decir(f"Ahora aprenderas {seccion}" if aprendiendo else f"Escogiste {seccion}, empecemos con la prueba", False)
    while not estado['fin_hilo']:
        decir(
            f"En cual subseccion deseas {'aprender' if aprendiendo else 'dar una prueba'}\n" + generar_mensaje_secciones(
                aprendizaje[seccion]))
        respuesta = escuchar()
        equivocado = True
        for subseccion in aprendizaje[seccion]:
            if not estado['fin_hilo']:
                if any(palabra in subseccion for palabra in respuesta.split()):  # escoger seccion
                    equivocado = False
                    aprender(seccion, subseccion) if aprendiendo else dictarpreguntas(seccion, subseccion)
            else:
                break
        if respuesta == 'salir':
            break
        elif equivocado:
            decir("repite la opcion por favor")


def cargarImg(img):
    if not img == "":
        image_path = "res/imgs/" + img  # Ruta de la imagen que deseas abrir
        if not img.__contains__(".png"):
            image_path += ".png"
        img_path[0] = image_path


class Interfaz:
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.init()
        self.fondo = pygame.image.load('res/imgs/fondo.jpg')  # 600x600px

        self.sizeF = (self.fondo.get_width(), self.fondo.get_height())  # ancho,alto
        pygame.display.set_mode(self.sizeF)

        self.micro = pygame.image.load('res/imgs/micro.png').convert_alpha()  # 120x120px
        self.load = [pygame.image.load('res/imgs/load.png').convert_alpha()]  # 140x140px

        self.fuente = pygame.font.SysFont('segoe print', 20)
        self.pygTxt = self.fuente.render('PYG-4 Tu Asistente Virtual', True, WHITE)
        self.fuenteSub = None
        pygame.display.flip()

    def crearFuente(self, size):
        self.fuenteSub = pygame.font.SysFont('Arial', size)
        return self.fuenteSub


def juego(jahorcado=True):
    if not jahorcado:
        estado['cartas'] = True
    estado['asistente'] = False
    estado['jugando'] = True
    while not estado['asistente']:
        time.sleep(1)


def interfaz():
    def parrafo():
        sub(185, 305, subTxt[0], 38, 13)

    def log():
        txt = subTxt[1]
        if not len(txt) == 0:
            i = sub(20, 45, txt[0], 25, 13)
            for j in range(1, len(txt)):
                i = sub(20, i, txt[j], 25, 13)
                if i > 450:
                    subTxt[1].remove(subTxt[1][0])

    def sub(x, y, txt, maxlong, tam):
        if isinstance(txt,tuple):
            if txt[1] == 1:
                COLOR = WHITE
            else: COLOR = BLACK
            txt = txt[0]
        else: COLOR = BLACK
        if len(txt) > 0:
            oraciones = dividir_texto(txt, maxlong)
            cont = 0
            for i, oracion in enumerate(oraciones):
                txtAyuda = ventana.crearFuente(tam).render(oracion, True, COLOR)
                screen.blit(txtAyuda, (x, y + (17 * i)))
                cont = i
            return y + (17 * (cont + 1))

    max_alto, min_alto = 150, 90

    alto1, alto2 = max_alto, min_alto

    y1, y2 = 140, 160
    while not estado['termino']:
        ventana = Interfaz()
        screen = pygame.display.set_mode(ventana.sizeF)
        inactivo, modo = False, True
        while estado['asistente']:
            pygame.display.set_icon(ventana.fondo)
            pygame.display.set_caption('PYG-4')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    estado['termino'], estado['asistente'] = True, False
                    pygame.quit()
                    break
            if not estado['termino']:
                screen.blit(ventana.fondo, (0, 0))
                if estado['hablando']:
                    ancho = 70
                    if modo:  # 185-120 = x,y 405 -> 220 -> 210
                        alto1 -= 2
                        alto2 += 2
                        y1 += 1
                        y2 -= 1

                    else:
                        alto1 += 2
                        alto2 -= 2
                        y1 -= 1
                        y2 += 1

                    modo = not modo if alto1 >= max_alto or alto1 <= min_alto else modo

                    pygame.draw.ellipse(screen, RED, (185, y1, ancho, alto1))
                    pygame.draw.ellipse(screen, BLUE, (260, y2, ancho, alto2))
                    pygame.draw.ellipse(screen, GREEN, (335, y1, ancho, alto1))
                    ventana.clock.tick(60)
                elif estado['escuchando']:  # 120+150=270/2=135
                    if modo:  # 185-120 = x,y 405 -> 220 -> 2109
                        pygame.draw.circle(screen, CELESTE, (295, 230), 80)
                    modo = not modo
                    screen.blit(ventana.micro, (235, 170))
                    ventana.clock.tick(2)
                else:
                    screen.blit(ventana.load[0], (235, 170))
                    ventana.load[0] = pygame.transform.rotate(ventana.load[0], 90)
                    ventana.clock.tick(2)
                parrafo()
                log()
                screen.blit(ventana.pygTxt, (10, 10))
                pygame.display.flip()
        while estado['jugando']:
            print(estado['cartas'])
            if estado['cartas']:
                cartas()
            else:
                ahorcado()
            estado['asistente'] = True
        while estado['aprendiendo']:
            imagen = pygame.image.load(img_path[0])
            size = (imagen.get_width(), imagen.get_height())
            screen = pygame.display.set_mode(size)
            screen.blit(imagen, (0, 0))
            pygame.display.flip()
            time.sleep(3)
            estado['asistente'] = True
            estado['aprendiendo'] = False
        while estado['query']:
            if not inactivo:
                pygame.quit()
                inactivo = True
