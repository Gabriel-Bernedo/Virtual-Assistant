import json
with open('basedatos.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)

with open('preguntas.json', 'r', encoding='utf-8') as archivo:
    preguntas = json.load(archivo)
