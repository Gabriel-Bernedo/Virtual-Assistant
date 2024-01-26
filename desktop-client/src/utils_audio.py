import pyttsx3
import speech_recognition as sr
import pygame

recognizer = sr.Recognizer()
microphone = sr.Microphone()
estado = {
    'hablando': True,
    'escuchando': False,
    'termino': False,
    'asistente': True,
    'aprendiendo': False,
    'enPartida': False,
    'jugando': False,
    'ayuda': False,
    'query': False,
    'fin_hilo': False,
    'cartas':False
}
subTxt = ['']


def decir(comando, cambiar=True):
    if not estado['fin_hilo']:
        estado['hablando'] = True
        subTxt[0] = comando if cambiar else subTxt[0]
        palabra = pyttsx3.init()
        palabra.say(comando)
        palabra.runAndWait()
        estado['hablando'] = False


def repAudio(archivo_audio):
    pygame.mixer.init()
    pygame.mixer.music.load(archivo_audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()


def enviarAudio(reconocer=recognizer, microfono=microphone, tiempo_ruido=3):
    if not isinstance(reconocer, sr.Recognizer):
        raise TypeError("'reconocer' no es de la instacia 'Recognizer'")

    if not isinstance(microfono, sr.Microphone):
        raise TypeError("'reconocer' no es de la instacia 'Recognizer'")

    with microfono as fuente:
        reconocer.adjust_for_ambient_noise(fuente, duration=tiempo_ruido)
        estado['escuchando'] = True
        repAudio("res/audio/inicio.wav")
        audio = reconocer.listen(fuente, None, 3)
        estado['escuchando'] = False
        repAudio("res/audio/fin.wav")

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


def escuchar():
    estado['hablando'] = False
    palabra = None
    while not estado['fin_hilo']:
        palabra = enviarAudio(recognizer, microphone)
        if palabra["mensaje"]:
            break
        if not palabra["suceso"]:
            print("Algo no está bien. No puedo reconocer tu micrófono o no lo tienes enchufado. <", palabra["error"],
                  ">")
            decir("Algo no está bien. No puedo reconocer tu micrófono o no lo tienes enchufado.")
            exit(1)
        decir("No pude escucharte, ¿podrías repetirlo?", False)
    if palabra is not None:
        return palabra["mensaje"].lower()
