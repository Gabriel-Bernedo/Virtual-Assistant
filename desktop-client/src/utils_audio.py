import asyncio
import pyttsx3
from pyvidplayer import Video
import speech_recognition as sr
import pygame
from ui import *
recognizer = sr.Recognizer()
microphone = sr.Microphone()
pygame.init()
ventana = [None]
def setVentana(scrren):
    ventana[0] = scrren
dict = {'continuar': True,
        'rpta':''}

width, height = 1280,720
def playvid(path):
    win = pygame.display.set_mode((width, height))
    vid = Video(path)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vid.close()
                return

        pygame.time.wait(16)
        vid.draw(win, (0, 0), force_draw=False)
        pygame.display.update()

        if not vid.get_playback_data()["active"] or not dict["continuar"]:
            vid.close()
            return
def mostarimg(path):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Mostrar Imagen")
    image = pygame.image.load(path).convert()
    done = False
    print('mostrando img')
    while not done and dict["continuar"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.blit(image,[0,0])
        pygame.display.flip()
        #print('aun no termino')

    # Salir del programa
    pygame.quit()
def asistente(hablar=False):
    if hablar:
        #mostarimg('img/escucha.png')
        playvid('videos/habla.mp4')
    else:
        print('escuchando')
        playvid('videos/escucha.mp4')
        #mostarimg('img/escucha.png')

def asistentePyg():
    modo = True
    while dict["continuar"]:
        '''screen.fill(WHITE)
        screen.blit(texto, (10, 10))'''
        if hablando[0]:
            if modo:
                pygame.draw.ellipse(ventana[0], BLUE, (0, 0, 100, 300))
                pygame.draw.ellipse(ventana[0], BLUE, (204, 0, 100, 300))
                pygame.draw.ellipse(ventana[0], BLUE, (102, 0, 100, 300))
                pygame.display.flip()
            else:
                pygame.draw.ellipse(ventana[0], BLUE, (0, 0, 100, 200))
                pygame.draw.ellipse(ventana[0], BLUE, (102, 0, 100, 200))
                pygame.draw.ellipse(ventana[0], BLUE, (204, 0, 100, 200))
                pygame.display.flip()
            modo = not modo
        else:
            pygame.draw.line(ventana[0], BLUE, (20, 50), (100, 50))
            pygame.display.flip()

        clock.tick(1)  # Establecer la velocidad de actualización (1 FPS en este caso)

async def hablar(comando, doPrint=True):
    dict["continuar"] = True
    await asyncio.gather(
        asyncio.to_thread(asistentePyg),
        asyncio.to_thread(txtToAudio, comando, doPrint)
    )

def txtToAudio(comando, doPrint=True):
    if doPrint:
        print(comando)
    palabra = pyttsx3.init()
    palabra.say(comando)
    palabra.runAndWait()
    dict["continuar"] = False

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
        audio = reconocer.listen(fuente, None, 3)
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

async def escuchar():
    dict["continuar"] = True
    await asyncio.gather(
        asyncio.to_thread(asistente),
        asyncio.to_thread(enviar_voz)
    )

    return dict['mensaje']

def enviar_voz():
    while True:
        palabra = capturar_voz(recognizer, microphone)
        if palabra["mensaje"]:
            break
        if not palabra["suceso"]:
            print("Algo no está bien. No puedo reconocer tu micrófono o no lo tienes enchufado. <", palabra["error"], ">")
            txtToAudio("Algo no está bien. No puedo reconocer tu micrófono o no lo tienes enchufado.")
            exit(1)
        txtToAudio("No pude escucharte, ¿podrías repetirlo?", False)
    dict["continuar"] = False
    dict['mensaje'] = palabra["mensaje"].lower()
    return dict['mensaje']

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    nombre = loop.run_until_complete(escuchar()).capitalize()
    loop.close()
    print("Nombre:", nombre)
modo = True