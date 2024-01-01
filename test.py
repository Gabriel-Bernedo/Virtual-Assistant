import threading
import time
# Async 1 : Ejemplo de la casa y el incendio (Eventos Planificados)
# '''
class Fire:
  on_fire = True
  power = 50

class House:
  value = 500

async def Burn(fire, house):
  while fire.on_fire and house.value > 0:
    house.value -= fire.power
    print(f"La casa se quema, valor restante : $ {house.value}")
    time.sleep(1)

async def Unburn(fire, tmp):
   time.sleep(tmp)
   fire.on_fire = False
   print("El fuego se apago")

def main():
  house = House()
  fire = Fire()
  therad1 = threading.Thread(target=lambda x: Burn(fire, house))
  therad1.start()
  while True:
    pass
# '''
        
# Async 2 : El vecindario y el incendio (Eventos disruptivos)
# '''
# '''

