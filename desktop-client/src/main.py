from auxiliar import *
from juegos.quizApp import *
from utils_audio import *
from ui import *
from multiprocessing import Process
'''def programa():
    txtToAudio(datos['bienvenida'])
    print("Di tu nombre: ")
    #nombre = asyncio.run(escuchar()).capitalize()
    nombre = enviar_voz().capitalize()
    txtToAudio(f"Hola {nombre}. Mucho gusto.")
    asyncio.run(hablar(f"{nombre} Ahora voy a explicarte sobre las opciones que tiene este programa. Tienes 3 opciones para escoger."))
    asyncio.run(hablar(
        "La opción Aprendizaje es donde podrás aprender todo con respecto a la Estructura de un computador. La opción Pruebas es donde podrás poner en práctica lo que aprendiste mediante exámenes. Y por último, la tercer opción, es Juegos, donde tambien podrás demostrar lo que aprendiste jugando."))
    while True:
        asyncio.run(hablar("¿Qué opción eliges? "))
        asyncio.run(hablar(" 1) Aprendizaje\n 2) Pruebas\n 3) Juegos\n 4) Salir"))
        respuesta = asyncio.run(escuchar())
        if respuesta == "aprendizaje":
            asyncio.run(hablar("Elegiste la opcion APRENDIZAJE."))
            while True:
                asyncio.run(hablar("Que seccion deseas aprender\n 1) Introduccion\n 2) Repertorio de instrucciones\n 3) "
                              "Modos de direccionamiento\n 4) Salir"))
                respuesta = asyncio.run(escuchar())
                if respuesta == "introducción":
                    aprender('introduccion')
                elif respuesta == "repertorio de instrucciones":
                    asyncio.run(hablar("Escogiste Repertorio de instrucciones"))
                    while True:
                        asyncio.run(hablar("Deseas la seccion\n 1) General\n 2) Instrucciones\n 3) Ambas\n 4) Salir"))
                        respuesta = asyncio.run(escuchar())
                        all = respuesta == "ambas"
                        if respuesta == "general" or all:
                            aprender('repertorio', 'general')
                        if respuesta == "instrucciones" or all:
                            aprender('repertorio', 'instrucciones')
                        if respuesta == "salir":
                            break
                        else:
                            asyncio.run(hablar("repite la opcion por favor"))
                elif respuesta == "modos de direccionamiento":
                    asyncio.run(hablar("Escogiste modos de direccionamiento"))
                    while True:
                        asyncio.run(hablar(
                            "Deseas la seccion\n 1) General\n 2) Primera seccion\n 3) Segunda seccion\n 4) Tercera seccione\n 5) Salir"))
                        respuesta = asyncio.run(escuchar())
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
                            asyncio.run(hablar("repite la opcion por favor"))
                elif respuesta == "salir":
                    break
                else:
                    asyncio.run(hablar("repite la opcion por favor"))
            break
        elif respuesta == "pruebas":
            asyncio.run(hablar("Elegiste la opción PRUEBAS."))
            asyncio.run(hablar("¿Por cual deseas empezar?"))
            while True:
                asyncio.run(hablar(
                    "Deseas dar una prueba sobre\n 1) Introduccion\n 2) Repertorio de instrucciones\n 3) Modos de direccionamiento\n 4) Salir"))
                respuesta = asyncio.run(escuchar())
                print("rpta " + respuesta)
                if respuesta == "introducción":
                    asyncio.run(hablar("Escogiste introduccion\nEmpezemos con la prueba:"))
                    dictarpreguntas("introduccion")
                elif respuesta == "repertorio de instrucciones":
                    asyncio.run(hablar("Escogiste Repertorio de instrucciones"))
                    while True:
                        asyncio.run(hablar("Deseas la seccion\n 1) General\n 2) Instrucciones\n 3) Salir"))
                        respuesta = asyncio.run(escuchar())
                        if respuesta == "general":
                            dictarpreguntas('repertorio', 'general')
                        elif respuesta == "instrucciones":
                            dictarpreguntas('repertorio', 'instrucciones')
                        elif respuesta == "salir":
                            break
                        else:
                            asyncio.run(hablar("repite la opcion por favor"))
                elif respuesta == "modos de direccionamiento":
                    while True:
                        asyncio.run(hablar("Escogiste Repertorio de instrucciones"))
                        asyncio.run(hablar(
                            "Deseas la seccion\n 1) General\n 2) Primera seccion\n 3) Segunda seccion\n 4) Tercera seccion\n 5)Salir"))
                        respuesta = asyncio.run(escuchar())
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
                            asyncio.run(hablar("repite la opcion por favor"))
                elif respuesta == "salir":
                    break
                else:
                    asyncio.run(hablar("repite la opcion por favor"))
        elif respuesta == "juegos":
            asyncio.run(hablar("Elegiste la opción JUEGOS."))
            asyncio.run(hablar(
                "El primer juego consta en contestar las preguntas, haciendo click en la imagen que crees que es la respuesta."))
            if __name__ == "__main__":
                root = tk.Tk()
                app = ComputerStructureQuizApp(root)
                root.mainloop()
        elif respuesta == "salir":
            break
        else:
            asyncio.run(hablar(
                nombre + " creo que no has respondido con alguna de las instrucciones indicadas anteriormente"))
            asyncio.run(hablar("Responde con una de las alternativas mencionadas."))'''
def programa():
    # Tu código aquí
    #setVentana(screen)
    txtToAudio(datos['bienvenida'])
    print("Di tu nombre: ")
    # nombre = asyncio.run(escuchar()).capitalize()
    nombre = enviar_voz().capitalize()
    txtToAudio(f"Hola {nombre}. Mucho gusto.")
async def main():
    #dict["continuar"] = True
    await asyncio.gather(
        asyncio.to_thread(programa),
        asyncio.to_thread(asistentePyg)
    )
asyncio.run(main())
'''import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ventana en Blanco")
screen.fill(WHITE)
pygame.display.flip()

# Función principal del programa
def programa(screen):
    # Tu código aquí
    setVentana(screen)
    txtToAudio(datos['bienvenida'])
    print("Di tu nombre: ")
    # nombre = asyncio.run(escuchar()).capitalize()
    nombre = enviar_voz().capitalize()
    txtToAudio(f"Hola {nombre}. Mucho gusto.")

programa(screen)
print("Saliendo del programa")'''
'''
procesos = [
    Process(target=programa),
    Process(target=asistentePyg)
]
#freeze_support()
for proceso in procesos:
    proceso.start()
for proceso in procesos:
    proceso.join()'''