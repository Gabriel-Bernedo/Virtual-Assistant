from auxiliar import *
import threading
from utils_audio import *
import time
from query import query


def programa():
    nombre = 'Paulo'

    while not estado['fin_hilo']:
        #decir(" 1) Aprendizaje\n 2) Pruebas\n 3) Juegos\n 4) Modificar\n 5) Salir")
        #respuesta = escuchar()
        respuesta = 'juegos'
        if respuesta == "aprendizaje":
            aprenderElseProbar()
        elif respuesta == "pruebas":
            aprenderElseProbar(False)
        elif respuesta == "juegos":
            decir("Ahora jugaras ahorcado")
            juego()
            #respuesta = "aprendizaje"
        elif respuesta == 'modificar':
            query()
            #respuesta = 'juegos'
        elif respuesta == "salir":
            break
        else:
            decir(
                nombre + " creo que no has respondido con alguna de las instrucciones indicadas anteriormente")
    estado['termino'] = True


def asistentePyg():#INTERFAZ grafica
    hilo1 = threading.Thread(target=programa)
    hilo1.start()
    interfaz()
    #pass
    print('fin hilo')
    estado['fin_hilo'] = True
    hilo1.join()
    return


asistentePyg()