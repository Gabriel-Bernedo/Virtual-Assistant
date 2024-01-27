from ahorcado import *

with open('res/db/cartas.json', 'r', encoding='utf-8') as archivo:
    cartasJson = json.load(archivo)
db_cartas = []
for carta in cartasJson:
    print(f'agregando: {carta}')
    db_cartas.append(carta)

def cartas():  # INTERFAZ grafica CARTA
    pygame.init()
    fuente = pygame.font.SysFont('segoe print', 18)
    tablero = pygame.image.load('res/imgs/tablero.jpg')  # 1280x720px
    tamanio = (tablero.get_width(), tablero.get_height())
    pantalla = pygame.display.set_mode(tamanio)
    pygame.display.set_caption('CARTAS')
    pygame.display.set_icon(tablero)
    puntaje = 0
    turnos = 0

    n = 4
    ANCHO_VENTANA = tablero.get_width()
    ANCHO_CARTA = (tablero.get_width() - ((n + 1) * 10)) / n
    ALTO_CARTA = (tablero.get_height() - 30) / 2
    MARGEN = 10
    COLOR_CARTA_OCULTA = (100, 100, 100)

    class Carta:
        def __init__(self, nombre, contenido, tipo):
            self.nombre = nombre
            self.contenido = contenido
            self.tipo = tipo
            self.mostrada = False
            self.eliminada = False

    def dividir_texto_cuadro(texto, fuente, longitud_maxima):
        palabras = texto.split()
        oraciones = []
        oracion_actual = palabras[0]

        for palabra in palabras[1:]:
            ancho_actual, _ = fuente.size(oracion_actual + ' ' + palabra)

            if ancho_actual <= longitud_maxima:
                oracion_actual += ' ' + palabra
            else:
                oraciones.append(oracion_actual)
                oracion_actual = palabra

        oraciones.append(oracion_actual)
        return oraciones

    def parrafo_cuadro(txt, fuente, longitud_maxima, x, y):
        oraciones = dividir_texto_cuadro(txt, fuente, longitud_maxima)
        altura_total = len(oraciones) * fuente.get_linesize()

        # Crear una superficie temporal con fondo blanco
        superficie_temporal = pygame.Surface((ANCHO_CARTA - MARGEN, altura_total))
        superficie_temporal.fill((255, 255, 255))  # Fondo blanco

        for i, oracion in enumerate(oraciones):
            txtAyuda = fuente.render(oracion, True, (0, 0, 0))
            # Blit del texto en la superficie temporal
            superficie_temporal.blit(txtAyuda, (0, fuente.get_linesize() * i))

        # Blit de la superficie temporal en la pantalla
        pantalla.blit(superficie_temporal, (x + (MARGEN / 2), y))

    # Función para cargar imágenes
    def cargar_imagen(nombre, extension='jpg'):
        ruta = f"res/imgs/cartas/{nombre}.{extension}"
        imagen = pygame.image.load(ruta)
        return pygame.transform.scale(imagen, (ANCHO_CARTA, ALTO_CARTA))

    # Función para crear el tablero de cartas
    def crear_tablero():
        cartas = []

        # Agregar parejas de cartas al tablero
        print(f'db_cartas: {db_cartas}')
        for i in range(n):
            print(f'carta{i}: {db_cartas[i]}')
            nombre_carta = db_cartas[i]
            descripcion_carta = cartasJson[nombre_carta]

            imagen_img = nombre_carta
            imagen_descripcion = descripcion_carta

            # Agregar dos cartas idénticas
            cartas.append(Carta(nombre_carta, imagen_img, 'imagen'))
            cartas.append(Carta(nombre_carta, imagen_descripcion, 'texto'))

        # Mezclar las cartas
        random.shuffle(cartas)

        return cartas

    def dibujar_tablero(cartas):
        pantalla.fill(BLACK)

        # Dibujar el fondo del tablero
        pantalla.blit(tablero, (0, 0))

        x, y = MARGEN, MARGEN

        for carta in cartas:
            if carta.eliminada:
                print(f"saltando carta {carta.nombre}")
                x += ANCHO_CARTA + MARGEN
                if x > ANCHO_VENTANA - ANCHO_CARTA - MARGEN:
                    x = MARGEN
                    y += ALTO_CARTA + MARGEN
                continue

            if carta.mostrada:
                if carta.tipo == 'imagen':
                    # Mostrar imagen
                    imagen_carta = cargar_imagen(carta.contenido)
                    pantalla.blit(imagen_carta, (x, y))
                elif carta.tipo == 'texto':
                    # Mostrar texto
                    texto_carta = carta.contenido
                    parrafo_cuadro(texto_carta, fuente, ANCHO_CARTA - MARGEN, x, y)
            else:
                imagen_carta = cargar_imagen('oculto', 'png')
                pantalla.blit(imagen_carta, (x, y))

            x += ANCHO_CARTA + MARGEN

            if x > ANCHO_VENTANA - ANCHO_CARTA - MARGEN:
                x = MARGEN
                y += ALTO_CARTA + MARGEN

        pygame.display.flip()

        pass

    cartas = crear_tablero()
    dibujar_tablero(cartas)
    cartas_seleccionadas = []

    while estado['jugando']:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Obtener posición del clic
                pos = pygame.mouse.get_pos()
                x, y = pos

                # Verificar si se hizo clic en una carta
                for carta in cartas:

                    carta_x, carta_y = MARGEN + (ANCHO_CARTA + MARGEN) * (cartas.index(carta) % 4), MARGEN + (
                            ALTO_CARTA + MARGEN) * (cartas.index(carta) // 4)

                    if not carta.mostrada:
                        if x >= carta_x and x <= carta_x + ANCHO_CARTA and y >= carta_y and y <= carta_y + ALTO_CARTA:
                            carta.mostrada = True
                            print(carta.nombre)
                            cartas_seleccionadas.append(carta)
                            dibujar_tablero(cartas)

                print(f'{cartas_seleccionadas}: {len(cartas_seleccionadas)}')
                # Lógica para comparar las cartas seleccionadas
                if len(cartas_seleccionadas) == 2:
                    turnos += 1
                    print(turnos)
                    if cartas_seleccionadas[0].nombre == cartas_seleccionadas[1].nombre:
                        pygame.time.delay(1000)
                        print(f'cartas encontradas de {cartas_seleccionadas[0].nombre}')
                        puntaje += 1
                        cartas_seleccionadas[0].eliminada = True
                        cartas_seleccionadas[1].eliminada = True
                        # Cartas iguales, manténlas mostradas
                        print(puntaje)
                        pass
                    else:
                        # Cartas diferentes, ocúltalas nuevamente después de un breve tiempo
                        pygame.time.delay(1000)
                        for carta in cartas_seleccionadas:
                            carta.mostrada = False
                            print(f'ocultando {carta.nombre}')

                    # Limpiar lista de cartas seleccionadas
                    cartas_seleccionadas = []

                dibujar_tablero(cartas)
                if puntaje == 4:
                    # Imprimir resultados, agregar el break
                    parrafo_cuadro(f"ADIVINASTE TODAS LAS CARTAS EN: {turnos} TURNOS", fuente, 200,
                                   (ANCHO_VENTANA - 200) / 2, pantalla.get_height() - (400))
                    pygame.display.flip()
                    estado['jugando'] = False
                    estado['cartas'] = False


