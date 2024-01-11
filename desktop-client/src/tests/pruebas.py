'''
datos = "Esta instrucción se utiliza para realizar una bifurcación incondicional en un programa, llevándolo a una dirección específica."
print(datos)
print(int(len(datos)/30+1.8))
datos = 'Esta instrucción se utiliza pa'
print(len(datos))
'''
def dividir_texto(texto, longitud_maxima):
    palabras = texto.split()
    oraciones = []
    oracion_actual = palabras[0]

    for palabra in palabras[1:]:
        if len(oracion_actual + ' ' + palabra) <= longitud_maxima:
            oracion_actual += ' ' + palabra
        else:
            oraciones.append(oracion_actual)
            oracion_actual = palabra

    oraciones.append(oracion_actual)
    return oraciones

texto_original = "Es un programa informático que traduce el código fuente escrito en un lenguaje de programación de alto nivel (como C o Pascal) a código máquina, que es ejecutable por el procesador."
longitud_maxima = 40

resultado = dividir_texto(texto_original, longitud_maxima)

for i, oracion in enumerate(resultado):
    print(f"Oración {i + 1}: {oracion}")
