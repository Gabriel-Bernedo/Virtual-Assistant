from auxiliar import *
import threading
from utils_audio import *
from query import query


def programa():
    nombre = 'Paulo'
    #respuesta = 'modificar'
    while not estado['fin_hilo']:
        #respuesta = escuchar()
        respuesta = 'juegos'
        if respuesta == "aprendizaje":
            aprenderElseProbar()
        elif respuesta == "pruebas":
            aprenderElseProbar(False)
        elif respuesta == "juegos":
            #decir("Ahora jugaras ahorcado",False)
            juego()
        elif respuesta == 'modificar':
            query()
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