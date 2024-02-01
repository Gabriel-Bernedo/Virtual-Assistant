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
            print('en juegos')
            while not estado['fin_hilo']:
                #respuesta = escuchar()
                respuesta = 'memoria'
                if respuesta == 'memoria':
                    decir("Ahora jugaras memoria")
                    juego(False)
                    break
                elif respuesta == 'ahorcado':
                    decir("Ahora jugaras ahorcado")
                    juego()
                    break
                elif respuesta == "salir":
                    break
                else:
                    decir('Debe escoger un tipo de juego')
        elif respuesta == 'modificar':
            query()
            #respuesta = 'juegos'

        elif respuesta == "salir":
            break
        else:
            decir("Debes de escojer un modo de operacion")
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