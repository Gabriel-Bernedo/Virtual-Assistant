from auxiliar import *
import threading
from utils_audio import *
from query import query


def programa():
    decir(datos['bienvenida'][0])
    nombre = escuchar().capitalize()
    #subTxt[1].append(("paulo", 1))
    #nombre = 'paulo'
    decir(f"Hola {nombre}. Mucho gusto.")
    decir(
        f"{nombre} Tienes 3 opciones para escoger.")
    decir("En Aprendizaje te enseñare todo con respecto a la Estructura de un computador. "
          "En Pruebas podrás poner en práctica tu conocimiento. "
          "En Juegos, podrás entretenerte y practicar."
          "Y en modificar, se pueden agregar secciones a la Base de datos")
    while not estado['fin_hilo']:
        decir("¿Qué opción eliges? ")
        decir(" 1) Aprendizaje\n 2) Pruebas\n 3) Juegos\n 4) Modificar\n 5) Salir")
        respuesta = escuchar()
        #subTxt[1].append(('juegos', 1))
        #respuesta = 'juegos'
        if respuesta == "aprendizaje":
            aprenderElseProbar()
        elif respuesta == "pruebas":
            aprenderElseProbar(False)
        elif respuesta == "juegos":
            decir('Deseas jugar memoria o ahorcado?')
            while not estado['fin_hilo']:
                respuesta = escuchar()
                #subTxt[1].append(('memoria', 1))
                #respuesta = 'memoria'
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
        elif respuesta == "salir":
            break
        else:
            decir(
                nombre + " creo que no has respondido con alguna de las instrucciones indicadas anteriormente")
    estado['termino'] = True


def asistentePyg():
    hilo1 = threading.Thread(target=programa)
    hilo1.start()
    interfaz()
    print('fin hilo')
    estado['fin_hilo'] = True
    hilo1.join()
    return


asistentePyg()
