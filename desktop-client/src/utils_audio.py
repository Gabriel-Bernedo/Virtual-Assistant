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
subTxt = ['',[]]


def decir(comando, cambiar=True):
    if not estado['fin_hilo']:
        estado['hablando'] = True
        if cambiar:
            subTxt[0] = comando
            subTxt[1].append((comando, 0))
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
    respuesta = {
        "suceso": True,
        "error": None,
        "mensaje": None,
    }
    with microfono as fuente:
        reconocer.adjust_for_ambient_noise(fuente, duration=tiempo_ruido)
        estado['escuchando'] = True
        repAudio("res/audio/inicio.wav")
        try:
            audio = reconocer.listen(fuente, 5, 3)
            estado['escuchando'] = False
            repAudio("res/audio/fin.wav")
        except sr.WaitTimeoutError:
            respuesta['mensaje'] = ' '
            return respuesta

    try:
        respuesta["mensaje"] = reconocer.recognize_google(audio, language="es-PE")
    except sr.RequestError:
        respuesta["suceso"] = False
        respuesta["error"] = "API no disponible"
    except sr.UnknownValueError:
        respuesta["mensaje"] = " "

    return respuesta


def escuchar():
    estado['hablando'] = False
    palabra = None
    while not estado['fin_hilo']:
        palabra = enviarAudio(recognizer, microphone)
        if not palabra["mensaje"].isspace():
            break
        if not palabra["suceso"]:
            decir("Algo no está bien. No puedo reconocer tu micrófono o no lo tienes enchufado.")
            exit(1)
        if not estado['fin_hilo']:
            decir("No pude escucharte, ¿podrías repetirlo?", False)
    if palabra is not None or palabra is not ' ':
        subTxt[1].append((palabra["mensaje"].lower(), 1))
        return palabra["mensaje"].lower()
    else: return ''
