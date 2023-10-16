import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
microphone = sr.Microphone()

#CONVERTIR CADENAS DE TEXTO A AUDIO Y REPRODUCIRLAS
def texto_a_audio(comando):
    palabra = pyttsx3.init()
    palabra.say(comando)
    palabra.runAndWait()

#CAPTURA AUDIO DESDE EL MICROFONO Y ANALIZA POSIBLES ERRORES
def capturar_voz(reconocer, microfono, tiempo_ruido = 1.0):
    if not isinstance(reconocer, sr.Recognizer):
        raise TypeError("'reconocer' no es de la instacia 'Recognizer'")

    if not isinstance(microfono, sr.Microphone):
        raise TypeError("'reconocer' no es de la instacia 'Recognizer'")
    
    with microfono as fuente:
        reconocer.adjust_for_ambient_noise(fuente, duration = tiempo_ruido)
        audio = reconocer.listen(fuente)

    respuesta = {
        "suceso": True,
        "error": None,
        "mensaje": None,
    }
    try:
        respuesta["mensaje"] = reconocer.recognize_google(audio, language="es-PE")
    except sr.RequestError:
        respuesta["suceso"] = False
        respuesta["error"] = "API no disponible"
    except sr.UnknownValueError:
        respuesta["error"] = "Habla inteligible"
    return respuesta

#CONVIERTE A UNA CADENA DE TEXTO EN MINUSCULA EL AUDIO ENVIADO POR MICROFONO
def enviar_voz():
    while (1):
        palabra = capturar_voz(recognizer, microphone)
        if palabra["mensaje"]:
            break
        if not palabra["suceso"]:
            print("Algo no está bien. No puedo reconocer tu micrófono o no lo tienes enchufado. <", palabra["error"],">")
            texto_a_audio("Algo no está bien. No puedo reconocer tu micrófono o no lo tienes enchufado.")
            exit(1)
        print("No pude escucharte, ¿podrias repetirlo?\n")
        texto_a_audio("No pude escucharte, ¿podrias repetirlo?")
    return palabra["mensaje"].lower()
