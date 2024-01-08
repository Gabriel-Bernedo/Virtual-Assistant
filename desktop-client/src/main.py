from auxiliar import *
import threading
from utils_audio import *
import time
def programa():
    #decir(datos['bienvenida'][0])
    #nombre = escuchar().capitalize()
    nombre = 'carlo'
    #decir(f"Hola {nombre}. Mucho gusto.")
    #decir(f"{nombre} Ahora voy a explicarte sobre las opciones que tiene este programa. Tienes 3 opciones para escoger.")
    #decir("La opción Aprendizaje es donde podrás aprender todo con respecto a la Estructura de un computador. "
    #           "La opción Pruebas es donde podrás poner en práctica lo que aprendiste mediante exámenes. "
    #           "Y por último, la tercer opción, es Juegos, donde tambien podrás demostrar lo que aprendiste jugando.")
    while True:
        #decir("¿Qué opción eliges? ")
        #decir(" 1) Aprendizaje\n 2) Pruebas\n 3) Juegos\n 4) Salir")
        respuesta = escuchar()
        respuesta = 'aprendizaje'
        if respuesta == "aprendizaje":
            decir("Elegiste la opcion APRENDIZAJE.")
            while True:
                decir("Que seccion deseas aprender\n 1) Introduccion\n 2) Repertorio de instrucciones\n 3) "
                              "Modos de direccionamiento\n 4) Salir")
                respuesta = escuchar()
                estado['asistente'] = False
                estado['jugando'] = False
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

asistentePyg()
