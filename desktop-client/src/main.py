from auxiliar import *
import threading
from utils_audio import *
import time


def programa():
    decir(datos['bienvenida'][0])
    nombre = escuchar().capitalize()
    #nombre = 'Paulo'
    decir(f"Hola {nombre}. Mucho gusto.")
    decir(f"{nombre} Ahora voy a explicarte sobre las opciones que tiene este programa. Tienes 3 opciones para escoger.")
    decir("La opción Aprendizaje es donde podrás aprender todo con respecto a la Estructura de un computador. "
               "La opción Pruebas es donde podrás poner en práctica lo que aprendiste mediante exámenes. "
               "Y por último, la tercer opción, es Juegos, donde tambien podrás demostrar lo que aprendiste jugando.")
    while not estado['fin_hilo']:
        decir("¿Qué opción eliges? ")
        decir(" 1) Aprendizaje\n 2) Pruebas\n 3) Juegos\n 4) Modificar\n 5) Salir")
        respuesta = escuchar()
        #respuesta = 'juegos'
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
    print('fin hilo')
    estado['fin_hilo'] = True
    hilo1.join()
    return


asistentePyg()