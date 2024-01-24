from auxiliar import *
import threading
from utils_audio import *
import time


def programa():
    nombre = 'Paulo'
    respuesta = 'modificar'

    while not estado['fin_hilo']:
        decir(" 1) Aprendizaje\n 2) Pruebas\n 3) Juegos\n 4) Modificar\n 5) Salir")
        #respuesta = escuchar()
        #respuesta = 'modificar'
        if respuesta == "aprendizaje":
            aprenderElseProbar()
        elif respuesta == "pruebas":
            aprenderElseProbar(False)
        elif respuesta == "juegos":
            decir("Ahora jugaras ahorcado")
            estado['asistente'] = False
            estado['jugando'] = True
            while not estado['asistente']:
                time.sleep(1)
        elif respuesta == 'modificar':
            estado['asistente'] = False
            estado['query'] = True
            from query import query
            query()
            estado['asistente'] = True
            estado['query'] = False
            respuesta = 'juegos'
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