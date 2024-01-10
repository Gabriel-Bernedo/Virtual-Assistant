import json
with open('../res/db/ahorcado.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)
'''for rpta in datos:
    print(rpta)
    print(datos[rpta])'''
print(datos)