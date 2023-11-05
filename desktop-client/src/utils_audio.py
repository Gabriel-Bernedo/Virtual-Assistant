import speech_recognition as sr
import pyttsx3
import pygame
recognizer = sr.Recognizer()
microphone = sr.Microphone()
pygame.init()
#CONVERTIR CADENAS DE TEXTO A AUDIO Y REPRODUCIRLAS
def texto_a_audio(comando, doPrint = True):
    if doPrint:
        print(comando)
    palabra = pyttsx3.init()
    palabra.say(comando)
    palabra.runAndWait()
def mandaraudio(archivo_audio):
    pygame.mixer.init()
    pygame.mixer.music.load(archivo_audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
#CAPTURA AUDIO DESDE EL MICROFONO Y ANALIZA POSIBLES ERRORES
def capturar_voz(reconocer=recognizer, microfono=microphone, tiempo_ruido = 3):
    if not isinstance(reconocer, sr.Recognizer):
        raise TypeError("'reconocer' no es de la instacia 'Recognizer'")

    if not isinstance(microfono, sr.Microphone):
        raise TypeError("'reconocer' no es de la instacia 'Recognizer'")
    
    with microfono as fuente:
        reconocer.adjust_for_ambient_noise(fuente, duration = tiempo_ruido)
        #print("iniciando reconcimiento")
        mandaraudio("inicio.wav")
        audio = reconocer.listen(fuente,None,3)
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
        texto_a_audio("No pude escucharte, ¿podrias repetirlo?",False)
    return palabra["mensaje"].lower()
