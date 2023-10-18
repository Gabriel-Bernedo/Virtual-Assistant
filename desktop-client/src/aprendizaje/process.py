import sys
import time
from utils_audio import texto_a_audio , enviar_voz
from PIL import Image
from datos import datos
data_path ={
    "unidad central de proceso":"img/CPU.png",
    "memoria":"img/memoria.png",
    "entrada salida":"img/entrada salida.png",
    "sistemas de interconexión buses":"img/buses.png",
    "periféricos":"img/perifericos.jpg"
}
def aprender(tema): # aprende tema y devuelve si continaur o no 
    try:
        img = Image.open(data_path[tema])
    except:
        print("No se pudo cargar la imagen.")
        sys.exit(1)

    size = (600,400)
    img2 = img.resize(size)
    img2.show()

    texto_a_audio(datos[tema])

    print("¿Quieres seguir aprendiendo?")
    texto_a_audio("¿Quieres seguir aprendiendo?")
    time.sleep(0.5)
    print("Responde con:\n1) Está bien\n2) No gracias")

    respuesta = enviar_voz()
    print("Tu respuesta " + respuesta)

    #COMPRUEbA QUE EL MENSAJE ENVIADO SEA VALIDO
    if respuesta == "está bien": 
        #ELEGIMOS CON QUÉ OPCIÓN SEGUIR
        print("Elige la opcion que desees aprender: ")
        texto_a_audio("Elige la opcion que desees aprender: ")
        print("\n1) Unidad central de proceso CPU\n2) Memoria\n3) Entrada / Salida\n4) Sistemas de interconexion: Buses\n5) Periféricos\n")
        return True
    elif respuesta == "no gracias":
        print("Oh. es una lástima. En ese caso nos veremos en otra ocasión ")
        texto_a_audio("Oh. es una lástima. En ese caso nos veremos en otra ocasión")
        
        time.sleep(0.5)
        print("Espero que hayas aprendido mucho sobre este tema. Hasta luego.")
        texto_a_audio("Espero que hayas aprendido mucho sobre este tema. Hasta luego.")
        return False
    #SI EL MENSAJE ENVIADO NO ES ERRONEO LE PIDE AL USUARIO SELECCIONAR UNA OPCION VALIDA
    else:
        print( "Estimado, creo que no has respondido con alguna de las instrucciones indicadas anteriormente")
        texto_a_audio("Estimado, creo que no has respondido con alguna de las instrucciones indicadas anteriormente")
        print("Responde con:\n1) Esta bien.\n2) No gracias")
        return True
