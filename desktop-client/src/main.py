
import time
import sys
import tkinter as tk
from PIL import Image, ImageTk
#New imports
from datos import datos, preguntas
from aprendizaje.imageWindow import ImageWindow
from aprendizaje.process import aprender
from juegos.quizApp import ComputerStructureQuizApp

from utils_audio import enviar_voz, texto_a_audio

#BASE DE DATOS DONDE SE ENCUENTRA TODA LA INFORMACION CONCERNIENTE
#Migrado a datos.py para mejor manejo y posible mejora futura

#INICIO
if __name__ == "__main__":
    salir = False

    #USANDO LA FUNCION TEXTO_A_AUDIO SE HACE LEER CADENAS DE TEXTO, COMO SI LA COMPUTADORA TE ESTUVIERA HABLANDO
    texto_a_audio(datos['bienvenida'])
    print("Di tu nombre: ")
    #LA FUNCION 'enviar_voz' RETORNA UNA CADENA DE TEXTO DEL AUDIO ENVIADO POR VOZ DEL USUARIO
    nombre = enviar_voz()
    texto_a_audio("Hola {}. Mucho gusto.".format(nombre))
    texto_a_audio("{} Ahora voy a explicarte sobre las opciones que tiene este programa. Tienes 3 opciones para escoger.".format(nombre))
    texto_a_audio("\n 1) Aprendizaje\n 2) Tests\n 3) Juegos\n")
    texto_a_audio("La opción Aprendizaje es donde podrás aprender todo con respecto a la Estructura de un computador. La opción Tests es donde podrás poner en práctica lo que aprendiste mediante exámenes. Y por último, la tercer opción, es Juegos, donde tambien podrás demostrar lo que aprendiste jugando.")
    texto_a_audio("¿Qué opción eliges?")
    time.sleep(0.5)
    texto_a_audio("¿Aprendizaje? ¿Tests? ¿Juegos?", False)
    
    #SE USA LA FUNCION SLEEP DE LA LIBRERIA TIME PARA PAUSAR UN TIEMPO LA EJECUCION DEL PROGRAMA
    #PARA QUE LA INTERACCION SEA MAS NATURAL
    time.sleep(0.5)
    
    #PREGUNTA AL USUARIO QUE OPCION ELIGE
    while (1): 
        respuesta = enviar_voz()
        print("Tu respuesta " + respuesta)

        if respuesta == "aprendizaje": 
            texto_a_audio("Elegiste la opcion APRENDIZAJE.")
            texto_a_audio("Muy bien, empecemos entonces.")

            texto_a_audio("Antes de empezar quisiera hacer una introduccion a la estructura de computadores.")
            time.sleep(0.5)
            
            def main():
                root = tk.Tk()
                image_path = "img/computador.jpg"  # Ruta de la imagen que deseas abrir
                
                image_window = ImageWindow(root, image_path)
                image_window.update()  # Iniciar la función de actualización

                root.mainloop()

            if __name__ == "__main__":
                main()

            texto_a_audio(datos['aprendizaje'])
            
            try:
                img = Image.open("img/arquitectura.png")
            except:
                print("No se pudo cargar la imagen.")
                sys.exit(1)
            
            size = (600,400)
            img2 = img.resize(size)
            img2.show()

            texto_a_audio("Como se puede apreciar en la imagen, la estructura de un computador está dado por:")
            texto_a_audio("\n1) Unidad central de proceso CPU\n 2) Memoria\n 3) Entrada / Salida\n 4) Sistemas de interconexion: Buses\n 5) Periféricos\n")

            #PREGUNTA AL USUARIO CON QUÉ PARTE DESEA EMPEZAR
            while(not salir):
                texto_a_audio("¿Por cual deseas empezar?")
                time.sleep(0.5)

                #COMPRUEBA QUE EL MENSAJE ENVIADO SEA VALIDO
                while (1):
                    respuesta = enviar_voz()
                    print("Tu respuesta " + respuesta)

                    if respuesta == "unidad central de proceso" or respuesta == "memoria" or respuesta == "entrada salida" or respuesta == "sistemas de interconexion buses" or respuesta == "perifericos":
                        continuar= aprender(respuesta)
                        if not continuar:
                            salir = True
                            break
                    elif respuesta != "unidad central de proceso" or respuesta != "memoria" or respuesta != "entrada salida" or respuesta != "sistemas de interconexion buses" or respuesta != "perifericos":
                        texto_a_audio("Perdona, pero por el momento no tengo informacion sobre {}. Prueba con otra OPCION".format(respuesta))
                        print("\n1) Unidad central de proceso CPU\n2) Memoria\n3) Entrada / Salida\n4) Sistemas de interconexion: Buses\n5) Periféricos\n")
                    #SI EL MENSAJE ENVIADO NO ES ERRONEO LE PIDE AL USUARIO SELECCIONAR UNA OPCION VALIDA
                    else:
                        texto_a_audio(nombre + " creo que no has respondido con alguna de las instrucciones indicadas anteriormente")
                        print("\n1) Unidad central de proceso CPU\n 2) Memoria\n 3) Entrada / Salida\n 4) Sistemas de interconexion: Buses\n 5) Periféricos\n")    

            break
        elif respuesta == "test":
            texto_a_audio("Elegiste la opción TEST.")
            texto_a_audio("En esta opción tienes para elegir en dar una prueba de entrada sobre PENSAMIENTO COMPUTACIONAL, o dar un examen sobre Estructura de Computadores.")
            texto_a_audio("¿Cuál eliges?")
            texto_a_audio("\n 1) Prueba de entrada - Pensamiento Computacional\n 2) Examen - Estructura de computadores\n")
            
            while(not salir):
                texto_a_audio("¿Por cual deseas empezar?")
                time.sleep(0.5)

                #COMPRUEBA QUE EL MENSAJE ENVIADO SEA VALIDO
                while (1):
                    
                    respuesta = enviar_voz()
                    if respuesta == "prueba de entrada pensamiento computacional":

                        print("Tu respuesta " + respuesta)
                        texto_a_audio("Escogiste: Prueba de entrada de Pensamiento Computacional")
                        texto_a_audio("Empezemos con la prueba:")
                        puntaje = 0
                        def escribir_respuesta(pregunta, alternativas, respuesta_correcta):
                            print("------------------------------------------------------------------------------------")
                            print(pregunta)
                            for i, alternativa in enumerate(alternativas, start = 1):
                                print(f"{i}. {alternativa}")
                            texto_a_audio("Escribe el número de la alternativa que crees correcta: ", False)
                            print("Escribe el número de la alternativa que crees correcta: ")
                            respuesta_usuario = enviar_voz()
                            print("Tu respuesta " + respuesta)

                            if respuesta_usuario.isdigit():
                                opcion_elegida = int(respuesta_usuario)
                                if 1 <= opcion_elegida <= len(alternativas):
                                    if alternativas[opcion_elegida - 1] == alternativas[respuesta_correcta-1]:
                                        texto_a_audio("Respuesta correcta.")
                                        puntaje +=1
                                    else:
                                        texto_a_audio("Respuesta incorrecta.")
                                else:
                                    print("Opción inválida.")
                            else:
                                print("Entrada inválida. Por favor, ingresa el número de la alternativa.")
                            texto_a_audio("TU PUNTAJE ES DE "+puntaje+" PUNTOS")
                        for pregunta in preguntas['preguntas']:
                            texto_a_audio([pregunta['pregunta'],pregunta['alternativas']], False)
                            escribir_respuesta(pregunta['pregunta'], pregunta['alternativas_arr'], pregunta['respuesta_correcta'])       

                        texto_a_audio("¿Quieres seguir aprendiendo?")
                        time.sleep(0.5)
                        print("Responde con:\n1) Está bien\n2) No gracias")

                        respuesta = enviar_voz()
                        print("Tu respuesta " + respuesta)

                        #COMPRUEbA QUE EL MENSAJE ENVIADO SEA VALIDO
                        if respuesta == "está bien": 
                            #ELEGIMOS CON QUÉ OPCIÓN SEGUIR
                            texto_a_audio("Elige la opcion que desees aprender: ")
                            print("\n1) Aprendizaje\n2) Test\n3) Juegos\n")
                            salir = True
                            break
                        elif respuesta == "no gracias":
                            texto_a_audio("Oh. es una lástima. En ese caso nos veremos en otra ocasión.")
                            
                            time.sleep(0.5)
                            texto_a_audio("Espero que hayas aprendido mucho sobre este tema. Hasta luego.")
                            exit(0)
                        #SI EL MENSAJE ENVIADO NO ES ERRONEO LE PIDE AL USUARIO SELECCIONAR UNA OPCION VALIDA
                        else:
                            texto_a_audio(nombre + " creo que no has respondido con alguna de las instrucciones indicadas anteriormente")
                            print("Responde con:\n1) Esta bien.\n2) No gracias")  

        elif respuesta == "juegos":
            
            texto_a_audio("Elegiste la opción JUEGOS.")

            texto_a_audio("El primer juego consta en contestar las preguntas, haciendo click en la imagen que crees que es la respuesta.")
            
            if __name__ == "__main__":
                root = tk.Tk()
                app = ComputerStructureQuizApp(root)
                root.mainloop()
                    
        #SI EL MENSAJE ENVIADO NO ES ERRONEO LE PIDE AL USUARIO SELECCIONAR UNA OPCION VALIDA
        else:
            texto_a_audio(nombre + " creo que no has respondido con alguna de las instrucciones indicadas anteriormente")
            texto_a_audio("Responde con una de las alternativas mencionadas.")