import json
with open('basedatos.json', 'r') as archivo:
    datos = json.load(archivo)

with open('preguntas.json', 'r') as archivo:
    preguntas = json.load(archivo)
