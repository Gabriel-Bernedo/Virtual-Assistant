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
    while True:
        mensaje_pregunta = "Que seccion deseas aprender\n" if aprendiendo else "Deseas dar una prueba sobre\n"
        decir(mensaje_pregunta + generar_mensaje_secciones(aprendizaje))
        respuesta = escuchar()
        equivocado = True
        for seccion in aprendizaje:
            if any(palabra in seccion for palabra in respuesta.split() if len(palabra) > 3):#escoger seccion
                equivocado = False
                if isinstance(aprendizaje[seccion], dict) and len(seccion) > 1:
                    aprenderElseProbarSubseccion(seccion, aprendiendo)
                else:
                    aprender(seccion) if aprendiendo else dictarpreguntas(seccion)
                break
        if respuesta == 'salir':
            break
        elif equivocado:
            decir("repite la opcion por favor")


def aprenderElseProbarSubseccion(seccion, aprendiendo=True):
    decir(f"Ahora aprenderas {seccion}" if aprendiendo else f"Escogiste {seccion}, empecemos con la prueba")
    while True:
        decir(f"En cual subseccion deseas {'aprender'if aprendiendo else 'dar una prueba'}\n" + generar_mensaje_secciones(aprendizaje[seccion]))
        respuesta = escuchar()
        equivocado = True
        for subseccion in aprendizaje[seccion]:
            if any(palabra in subseccion for palabra in respuesta.split()):#escoger seccion
                equivocado = False
                aprender(seccion,subseccion) if aprendiendo else dictarpreguntas(seccion,subseccion)
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


def interfaz():
    pygame.init()
    fondo = pygame.image.load('res/imgs/fondo.jpg')  # 600x600px

    max_alto = 150
    min_alto = 90

    alto1 = max_alto
    alto2 = min_alto

    y1 = 140
    y2 = 160

    sizeF = (fondo.get_width(), fondo.get_height())  # ancho,alto
    pygame.display.set_mode(sizeF)

    micro = pygame.image.load('res/imgs/micro.png').convert_alpha()  # 120x120px
    load = [pygame.image.load('res/imgs/load.png').convert_alpha()]  # 140x140px

    fuente = pygame.font.SysFont('segoe print', 20)
    fuenteSub = pygame.font.SysFont('segoe print', 11)
    pygTxt = fuente.render('PYG-4 Tu Asistente Virtual', True, WHITE)
    pygame.display.flip()
    modo = True

    def parrafo(altura):
        if len(subTxt[0]) >0:
            oraciones = dividir_texto(subTxt[0], 38)
            for i, oracion in enumerate(oraciones):
                txtAyuda = fuenteSub.render(oracion, True, BLACK)
                screen.blit(txtAyuda, (185, altura + (17 * i)))

    while not estado['termino']:
        screen = pygame.display.set_mode(sizeF)
        while estado['asistente']:
            pygame.display.set_icon(fondo)
            pygame.display.set_caption('PYG-4')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    estado['termino'] = True
                    sys.exit()
            screen.blit(fondo, (0, 0))
            if estado['hablando']:
                ancho = 70
                if modo:  # 185-120 = x,y 405 -> 220 -> 210
                    alto1 -= 2
                    alto2 += 2
                    y1 += 1
                    y2 -= 1

                    # print(alto1, alto2, y1)
                    if alto1 == min_alto:
                        modo = not modo

                    pygame.draw.ellipse(screen, RED, (185, y1, ancho, alto1))
                    pygame.draw.ellipse(screen, BLUE, (260, y2, ancho, alto2))
                    pygame.draw.ellipse(screen, GREEN, (335, y1, ancho, alto1))
                else:
                    alto1 += 2
                    alto2 -= 2
                    y1 -= 1
                    y2 += 1

                    if alto1 == max_alto:
                        modo = not modo

                    pygame.draw.ellipse(screen, RED, (185, y1, ancho, alto1))
                    pygame.draw.ellipse(screen, BLUE, (260, y2, ancho, alto2))
                    pygame.draw.ellipse(screen, GREEN, (335, y1, ancho, alto1))
                parrafo(285)
                clock.tick(60)

            elif estado['escuchando']:  # 120+150=270/2=135
                if modo:  # 185-120 = x,y 405 -> 220 -> 2109
                    pygame.draw.circle(screen, CELESTE, (295, 230), 80)
                modo = not modo
                screen.blit(micro, (235, 170))
                parrafo(305)
                clock.tick(2)
            else:
                screen.blit(load[0], (235, 170))
                load[0] = pygame.transform.rotate(load[0], 90)
                parrafo(305)
                clock.tick(1.5)
            screen.blit(pygTxt, (10, 10))
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
            estado['asistente'] = True
            estado['aprendiendo']=False