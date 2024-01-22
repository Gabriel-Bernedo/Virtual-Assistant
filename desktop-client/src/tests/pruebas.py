import json

# Paso 1: Leer el archivo JSON
with open('basedatos.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Paso 2: Modificar los datos según sea necesario
#data['bienvenida'] += 'holá'
seccion = 'pruebas'
sub1 = ['sub1', 'sub2']
info = 'info'
data['aprendizaje'][seccion] = [
    info
    # ... Puedes agregar más claves y valores según sea necesario
]
# Paso 3: Escribir los cambios de vuelta al archivo JSON
with open('basedatos.json', 'w',  encoding='utf-8') as file:
    json.dump(data, file, indent=2,ensure_ascii=False)

