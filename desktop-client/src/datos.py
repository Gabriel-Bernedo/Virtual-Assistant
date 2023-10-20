import json
with open('basedatos.json', 'r') as archivo:
    datos = json.load(archivo)

with open('basedatospreguntas.json', 'r') as archivo:
    preguntas = json.load(archivo)
