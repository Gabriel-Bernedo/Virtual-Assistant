import pyttsx3
import speech_recognition as sr
import pygame
recognizer = sr.Recognizer()
microphone = sr.Microphone()
pygame.init()
ventana = [None]
def setVentana(scrren):
    ventana[0] = scrren
estado = {
    'hablando': True,
    'escuchando':False,
    'termino': False
}

def txtToAudio(comando, doPrint=True):
    estado['hablando'] = True
    if doPrint:
        print(comando)
    palabra = pyttsx3.init()
    palabra.say(comando)
    palabra.runAndWait()
    estado['hablando'] = False
def mandaraudio(archivo_audio):
    pygame.mixer.init()
    pygame.mixer.music.load(archivo_audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def capturar_voz(reconocer=recognizer, microfono=microphone, tiempo_ruido=3):
    if not isinstance(reconocer, sr.Recognizer):
        raise TypeError("'reconocer' no es de la instacia 'Recognizer'")

    if not isinstance(microfono, sr.Microphone):
        raise TypeError("'reconocer' no es de la instacia 'Recognizer'")

    with microfono as fuente:
        reconocer.adjust_for_ambient_noise(fuente, duration=tiempo_ruido)
        print("iniciando reconocimiento")
        mandaraudio("inicio.wav")
        estado['escuchando'] = True
        audio = reconocer.listen(fuente, None, 3)
        estado['escuchando'] = False
        mandaraudio("fin.wav")

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
        respuesta["error"] = "Habla ininteligible"

    return respuesta


def enviar_voz():
    estado['escuchando'] = False
    while True:
        palabra = capturar_voz(recognizer, microphone)
        if palabra["mensaje"]:
            break
        if not palabra["suceso"]:
            print("Algo no está bien. No puedo reconocer tu micrófono o no lo tienes enchufado. <", palabra["error"], ">")
            txtToAudio("Algo no está bien. No puedo reconocer tu micrófono o no lo tienes enchufado.")
            exit(1)
        txtToAudio("No pude escucharte, ¿podrías repetirlo?", False)
    estado['escuchando'] = False
    return palabra["mensaje"].lower()
