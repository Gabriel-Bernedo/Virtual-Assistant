import asyncio

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
    await asyncio.sleep(1)

async def Unburn(fire, time):
   await asyncio.sleep(time)
   fire.on_fire = False
   print("El fuego se apago")

async def main():
  house = House()
  fire = Fire()
  await asyncio.gather(Burn(fire, house), Unburn(fire, 5))

if __name__ == "_main_":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()