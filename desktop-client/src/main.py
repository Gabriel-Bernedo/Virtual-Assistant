import time
import tkinter as tk
# New imports
from datos import datos, preguntas
from aprendizaje.imageWindow import ImageWindow
from juegos.quizApp import ComputerStructureQuizApp
from utils_audio import *
# BASE DE DATOS DONDE SE ENCUENTRA TODA LA INFORMACION CONCERNIENTE
# Migrado a datos.py para mejor manejo y posible mejora futura
dict = {
    "puntaje": 0,
    "uno":1,
    "dos":2,
    "tres":3,
    "cuatro":4,
    "cinco":5
}
#uno 1
# INICIO
def cargarimg(img):
    if not img == None:
        root = tk.Tk()
        image_path = "img/" + img  # Ruta de la imagen que deseas abrir
        if not img.__contains__(".png"):
            image_path += ".png"
        def close_window():
            root.destroy()

        image_window = ImageWindow(root, image_path)
        image_window.update()  # Iniciar la función de actualización
        # Programar el cierre de la ventana después de 5 segundos
        root.after(5000, close_window)
        root.mainloop()

def dictarpreguntas(seccion, subsecion=None):
    resul, arr = 0, preguntas[seccion]
    if not subsecion == None:
        arr = preguntas[seccion][subsecion]
    for pregunta in arr:
        cont = 1
        texto_a_audio("Pregunta numero "+pregunta)
        for alternativa in arr[pregunta]:
            if arr[pregunta][alternativa] == 1:
                resul = cont
            texto_a_audio(str(cont)+") "+alternativa)
            cont += 1
        texto_a_audio("Dicta el numero de opcion que creas que es correcta")
        while True:
            rpta = enviar_voz()
            if rpta.isdigit() and int(rpta) > 0 and int(rpta) < cont:
                if int(rpta) == resul:
                    dict['puntaje'] += 1
                    texto_a_audio("respuesta correcta")
                else: texto_a_audio("respuesta incorrecta")
                break
            elif rpta in dict and dict[rpta] > 0 and dict[rpta] < cont:
                if resul == dict[rpta]:
                    dict['puntaje'] += 1
                    texto_a_audio("respuesta correcta")
                else:
                    texto_a_audio("respuesta incorrecta")
                break
            else:
                texto_a_audio("la respuesta debe estar en el rango")
    texto_a_audio("En esta seccion tu puntaje es de "+str(dict['puntaje'])+" sobre "+str(len(arr)))
    dict['puntaje'] = 0
if __name__ == "__main__":
    texto_a_audio(datos['bienvenida'])
    print("Di tu nombre: ")
    nombre = enviar_voz().capitalize()
    texto_a_audio("Hola {}. Mucho gusto.".format(nombre))
    texto_a_audio("{} Ahora voy a explicarte sobre las opciones que tiene este programa. Tienes 3 opciones para escoger.".format(nombre))
    texto_a_audio("La opción Aprendizaje es donde podrás aprender todo con respecto a la Estructura de un computador. La opción Pruebas es donde podrás poner en práctica lo que aprendiste mediante exámenes. Y por último, la tercer opción, es Juegos, donde tambien podrás demostrar lo que aprendiste jugando.")
    while True:
        texto_a_audio("¿Qué opción eliges? ")
        texto_a_audio(" 1) Aprendizaje\n 2) Pruebas\n 3) Juegos")
        while True:
            respuesta = enviar_voz()
            if respuesta == "aprendizaje":
                texto_a_audio("Elegiste la opcion APRENDIZAJE.")
                while True:
                    texto_a_audio("Que seccion deseas aprender\n 1) Introduccion\n 2) Repertorio de instrucciones\n 3) "
                                  "Modos de direccionamiento\n 4) Salir")
                    respuesta = enviar_voz()
                    if respuesta == "introducción":
                        texto_a_audio("Escogiste introduccion")
                        for dato, img in zip(datos['aprendizaje']['introduccion'], datos['img']['intro']):
                            texto_a_audio(dato)
                            cargarimg(img)
                    elif respuesta == "repertorio de instrucciones":
                        texto_a_audio("Escogiste Repertorio de instrucciones")
                        while True:
                            texto_a_audio("Deseas la seccion\n 1) General\n 2) Instrucciones\n 3) Ambas\n 4) Salir")
                            respuesta = enviar_voz()
                            all = respuesta == "ambas"
                            if respuesta == "general" or all:
                                for dato in datos['aprendizaje']['repertorio']['general']:
                                    texto_a_audio(dato)
                            if respuesta == "instrucciones" or all:
                                for dato in datos['aprendizaje']['repertorio']['instrucciones']:
                                    texto_a_audio(dato)
                            if respuesta == "salir":
                                break
                            else:
                                texto_a_audio("repite la opcion por favor")
                    elif respuesta == "modos de direccionamiento":
                        texto_a_audio("Escogiste modos de direccionamiento")
                        while True:
                            texto_a_audio(
                                "Deseas la seccion\n 1) General\n 2) Primera seccion\n 3) Segunda seccion\n 4) Tercera seccione\n 5)Salir")
                            respuesta = enviar_voz()
                            if respuesta == "general":
                                for dato in datos['aprendizaje']['modos']['general']:
                                    texto_a_audio(dato)
                            elif respuesta == "primera seccion":
                                for dato in datos['aprendizaje']['modos']['primera']:
                                    texto_a_audio(dato)
                            elif respuesta == "segunda sección":
                                for dato in datos['aprendizaje']['modos']['segunda']:
                                    texto_a_audio(dato)
                            elif respuesta == "tercera sección":
                                for dato in datos['aprendizaje']['modos']['tercera']:
                                    texto_a_audio(dato)
                            elif respuesta == "salir":
                                break
                            else:
                                texto_a_audio("repite la opcion por favor")
                    elif respuesta == "salir":
                        break
                    else:
                        texto_a_audio("repite la opcion por favor")
                break
            elif respuesta == "pruebas":
                texto_a_audio("Elegiste la opción PRUEBAS.")
                texto_a_audio("¿Por cual deseas empezar?")
                # COMPRUEBA QUE EL MENSAJE ENVIADO SEA VALIDO
                while True:
                    texto_a_audio(
                        "Deseas dar una prueba sobre\n 1) Introduccion\n 2) Repertorio de instrucciones\n 3) Modos de direccionamiento\n 4) Salir")
                    respuesta = enviar_voz()
                    print("rpta " + respuesta)
                    if respuesta == "introducción":
                        texto_a_audio("Escogiste introduccion\nEmpezemos con la prueba:")
                        dictarpreguntas("introduccion")
                    elif respuesta == "repertorio de instrucciones":
                        texto_a_audio("Escogiste Repertorio de instrucciones")
                        while True:
                            texto_a_audio("Deseas la seccion\n 1) General\n 2) Instrucciones\n 3) Salir")
                            respuesta = enviar_voz()
                            if respuesta == "general":
                                dictarpreguntas('repertorio','general')
                            elif respuesta == "instrucciones":
                                dictarpreguntas('repertorio','instrucciones')
                            elif respuesta == "salir":
                                break
                            else:
                                texto_a_audio("repite la opcion por favor")
                    elif respuesta == "modos de direccionamiento":
                        while True:
                            texto_a_audio("Escogiste Repertorio de instrucciones")
                            texto_a_audio(
                                "Deseas la seccion\n 1) General\n 2) Primera seccion\n 3) Segunda seccion\n 4) Tercera seccion\n 5)Salir")
                            respuesta = enviar_voz()
                            if respuesta == "general":
                                dictarpreguntas('modos','general')
                            elif respuesta == "primera seccion":
                                dictarpreguntas('modos', '1')
                            elif respuesta == "segunda sección":
                                dictarpreguntas('modos', '2')
                            elif respuesta == "tercera sección":
                                dictarpreguntas('modos', '3')
                            elif respuesta == "salir":
                                break
                            else:
                                texto_a_audio("repite la opcion por favor")
                    elif respuesta == "salir":
                        break
                    else:
                        texto_a_audio("repite la opcion por favor")
            elif respuesta == "juegos":
                texto_a_audio("Elegiste la opción JUEGOS.")
                texto_a_audio(
                    "El primer juego consta en contestar las preguntas, haciendo click en la imagen que crees que es la respuesta.")
                if __name__ == "__main__":
                    root = tk.Tk()
                    app = ComputerStructureQuizApp(root)
                    root.mainloop()
            elif respuesta == "salir":
                break
            else:
                texto_a_audio(nombre+" creo que no has respondido con alguna de las instrucciones indicadas anteriormente")
                texto_a_audio("Responde con una de las alternativas mencionadas.")
