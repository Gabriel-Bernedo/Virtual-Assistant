import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import json

with open('res/db/basedatos.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
def enviar_formulario():
    # Obtener la sección y la información general
    seccion = entry_seccion.get()
    if entry_seccion.get() != '':
        if seleccion_var.get():
            # Obtener la información de las subsecciones
            nombres_subsecciones_lista = [nom_subseccion.get() for nom_subseccion in
                                              nombres_subsecciones]
            informacion_subsecciones_lista = [info_subseccion.get("1.0", "end-1c") for info_subseccion in
                                              informacion_subsecciones]
            # Crear un diccionario para almacenar las subsecciones
            subsecciones_dict = {}
            # Iterar sobre las subsecciones y agregarlas al diccionario
            for nombre, info in zip(nombres_subsecciones_lista, informacion_subsecciones_lista):
                subsecciones_dict[nombre] = info.splitlines()
            # Asignar el diccionario de subsecciones a la sección en data['aprendizaje']
            data['aprendizaje'][seccion] = subsecciones_dict
        else:
            informacion = entry_informacion.get("1.0", "end-1c")
            data['aprendizaje'][seccion] = [
                informacion.splitlines()
            ]
        with open('res/db/basedatos.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

def actualizar_desplazamiento(event=None):
    # Actualizar la región de desplazamiento del Canvas
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def mostrar_nombres_secciones():
    if seleccion_var.get():
        # Obtener el número de subsecciones
        num_subsecciones = num_subsecciones_var.get()
        eliminar_nombres_secciones()

        for i in range(num_subsecciones):
            # Crear Entry para nombre de subsección
            nombre_seccion = tk.Entry(frame_subsecciones)
            nombre_seccion.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            nombres_subsecciones.append(nombre_seccion)

            # Crear Text para información de subsección
            info_subseccion = tk.Text(frame_subsecciones, width=50, height=2, wrap="word")
            info_subseccion.grid(row=i, column=2, padx=10, pady=5, sticky="w")
            informacion_subsecciones.append(info_subseccion)

        # Mostrar la información general
        label_informacion.grid_remove()
        entry_informacion.grid_remove()
        label_num_subsecciones.grid_remove()
        entrada_subsecciones.grid_remove()
        boton_enviar.grid(row=num_subsecciones + 5, columnspan=3, pady=10)
        actualizar_desplazamiento()
    else:
        # Si no se selecciona, eliminar las subsecciones y mostrar la información general
        eliminar_nombres_secciones()
        label_informacion.grid()
        entry_informacion.grid()
        label_num_subsecciones.grid()
        entrada_subsecciones.grid()
        boton_enviar.grid(row=num_subsecciones_var.get() + 5, columnspan=3, pady=10)
        actualizar_desplazamiento()

def eliminar_nombres_secciones():
    # Eliminar los Entry y Text de las subsecciones
    for nombre_seccion in nombres_subsecciones:
        nombre_seccion.destroy()
    for info_subseccion in informacion_subsecciones:
        info_subseccion.destroy()
    nombres_subsecciones.clear()
    informacion_subsecciones.clear()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agregar Temas a la Base de Datos")

# Configurar el tamaño de la ventana
ventana.geometry("720x720")
'''
imagen_fondo = PhotoImage(file="res/imgs/fondo.jpg")  # Reemplaza con la ruta de tu imagen
canvas = tk.Canvas(ventana, width=720, height=720)
canvas.pack()

# Mostrar la imagen de fondo
canvas.create_image(0, 0, anchor=tk.NW, image=imagen_fondo)
'''
# Etiqueta y entrada para la sección
label_seccion = tk.Label(ventana, text="Nombre de la Sección:")
label_seccion.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_seccion = tk.Entry(ventana)
entry_seccion.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Etiqueta y área de texto para la información general
label_informacion = tk.Label(ventana, text="Información:")
label_informacion.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_informacion = tk.Text(ventana, width=50, height=5)
entry_informacion.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Etiqueta y entrada para el número de subsecciones
label_num_subsecciones = tk.Label(ventana, text="Número de Subsecciones:")
label_num_subsecciones.grid(row=4, column=0, padx=10, pady=5, sticky="e")

num_subsecciones_var = tk.IntVar()
num_subsecciones_var.set(5)
entrada_subsecciones = tk.Entry(ventana, textvariable=num_subsecciones_var)
entrada_subsecciones.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Lista para almacenar los Entry de nombres de secciones
nombres_subsecciones = []

# Lista para almacenar los Text de información de subsecciones
informacion_subsecciones = []

# Checkbutton para mostrar nombres de secciones
seleccion_var = tk.BooleanVar()
seleccion_checkbutton = tk.Checkbutton(ventana, text="Mostrar Nombres de Secciones", variable=seleccion_var, command=mostrar_nombres_secciones)
seleccion_checkbutton.grid(row=3, column=0, columnspan=2, pady=5)

# Canvas para contener las subsecciones con Scrollbar
canvas = tk.Canvas(ventana)
canvas.grid(row=5, column=0, columnspan=3, pady=5)

# Frame interior para las subsecciones
frame_subsecciones = tk.Frame(canvas)
frame_subsecciones.grid(row=0, column=0, padx=10, pady=5, sticky="w")

# Scrollbar vertical
scrollbar_vertical = ttk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
scrollbar_vertical.grid(row=5, column=3, pady=5, sticky="ns")

# Configurar el Canvas para usar la Scrollbar vertical
canvas.configure(yscrollcommand=scrollbar_vertical.set)

# Permitir que el Canvas expanda su altura al agregar subsecciones
canvas.create_window((0, 0), window=frame_subsecciones, anchor="nw")

# Botón para enviar el formulario
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_formulario)
boton_enviar.grid(row=6, columnspan=3, pady=10)

# Llamada inicial a actualizar_desplazamiento
actualizar_desplazamiento()

# Configurar el evento de desplazamiento
canvas.bind("<Configure>", actualizar_desplazamiento)

ventana.mainloop()
def query():
    ventana.mainloop()
query()