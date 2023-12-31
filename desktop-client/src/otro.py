import pygame
from pyvidplayer import Video
from utils_audio import *
import asyncio

def playvid():
    win = pygame.display.set_mode((1280,720))
    vid = Video('habla.mp4')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #vid.get_playback_data()["active"] = False
                vid.close()
                return
                #pygame.quit()
                #exit()

        pygame.time.wait(16)
        vid.draw(win, (0, 0), force_draw=False)
        pygame.display.update()

        if not vid.get_playback_data()["active"]:
            # The video has finished playing, you can add your stop logic here
            #break
            vid.close()
            return
            #pygame.quit()
            #exit()

async def ashablar(comando, doPrint=True):
    await asyncio.gather(
        asyncio.to_thread(playvid),
        asyncio.to_thread(txtToAudio, comando, doPrint)
    )
'''asyncio.run(ashablar('hola como estas'))
print('q paso')
asyncio.run(ashablar('adios'))'''
playvid()
playvid()