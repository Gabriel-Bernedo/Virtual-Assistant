# New imports
from auxiliar import *
from juegos.quizApp import ComputerStructureQuizApp
from utils_audio import *

if __name__ == "__main__":
    '''texto_a_audio(datos['bienvenida'])
    print("Di tu nombre: ")
    nombre = enviar_voz().capitalize()
    texto_a_audio("Hola {}. Mucho gusto.".format(nombre))
    texto_a_audio("{} Ahora voy a explicarte sobre las opciones que tiene este programa. Tienes 3 opciones para escoger.".format(nombre))
    texto_a_audio("La opción Aprendizaje es donde podrás aprender todo con respecto a la Estructura de un computador. La opción Pruebas es donde podrás poner en práctica lo que aprendiste mediante exámenes. Y por último, la tercer opción, es Juegos, donde tambien podrás demostrar lo que aprendiste jugando.")
    '''
    nombre = ""
    while True:
        texto_a_audio("¿Qué opción eliges? ")
        texto_a_audio(" 1) Aprendizaje\n 2) Pruebas\n 3) Juegos\n 4) Salir")
        respuesta = enviar_voz()
        if respuesta == "aprendizaje":
            texto_a_audio("Elegiste la opcion APRENDIZAJE.")
            while True:
                texto_a_audio("Que seccion deseas aprender\n 1) Introduccion\n 2) Repertorio de instrucciones\n 3) "
                              "Modos de direccionamiento\n 4) Salir")
                respuesta = enviar_voz()
                if respuesta == "introducción":
                    aprender('introduccion')
                elif respuesta == "repertorio de instrucciones":
                    texto_a_audio("Escogiste Repertorio de instrucciones")
                    while True:
                        texto_a_audio("Deseas la seccion\n 1) General\n 2) Instrucciones\n 3) Ambas\n 4) Salir")
                        respuesta = enviar_voz()
                        all = respuesta == "ambas"
                        if respuesta == "general" or all:
                            aprender('repertorio','general')
                        if respuesta == "instrucciones" or all:
                            aprender('repertorio', 'instrucciones')
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
            '''texto_a_audio(
                "El primer juego consta en contestar las preguntas, haciendo click en la imagen que crees que es la respuesta.")
            if __name__ == "__main__":
                root = tk.Tk()
                app = ComputerStructureQuizApp(root)
                root.mainloop()'''
        elif respuesta == "salir":
            break
        else:
            texto_a_audio(nombre+" creo que no has respondido con alguna de las instrucciones indicadas anteriormente")
            texto_a_audio("Responde con una de las alternativas mencionadas.")