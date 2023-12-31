import json
from aprendizaje.imageWindow import ImageWindow
from utils_audio import *
import tkinter as tk
from PIL import Image, ImageTk

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

def cargarimg(img):
    if not img == "":
        root = tk.Tk()
        image_path = "img/" + img  # Ruta de la imagen que deseas abrir
        if not img.__contains__(".png"):
            image_path += ".png"

        def close_window():
            root.destroy()

        image_window = ImageWindow(root, image_path, image_path)
        image_window.update()  # Iniciar la función de actualización
        # Programar el cierre de la ventana después de 5 segundos
        root.after(5000, close_window)
        root.mainloop()


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
        cargarimg(img)
