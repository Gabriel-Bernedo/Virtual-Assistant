import tkinter as tk
from tkinter import ttk
import json
from auxiliar import estado


class InterfazGrafica:
    def __init__(self, ventana_principal):
        self.ventana = ventana_principal
        self.ventana.title("Agregar Temas a la Base de Datos")
        self.ventana.geometry("720x720")
        self.ventana.configure(bg="#60BBF4")
        self.crear_widgets()

    def crear_widgets(self):
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

        def actualizar_desplazamiento():
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


        # Etiqueta y entrada para la sección
        label_seccion = tk.Label(self.ventana, text="Nombre de la Sección:")
        label_seccion.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        entry_seccion = tk.Entry(self.ventana)
        entry_seccion.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Etiqueta y área de texto para la información general
        label_informacion = tk.Label(self.ventana, text="Información:")
        label_informacion.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        entry_informacion = tk.Text(self.ventana, width=50, height=5)
        entry_informacion.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Etiqueta y entrada para el número de subsecciones
        label_num_subsecciones = tk.Label(self.ventana, text="Número de Subsecciones:")
        label_num_subsecciones.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        num_subsecciones_var = tk.IntVar()
        num_subsecciones_var.set(5)
        entrada_subsecciones = tk.Entry(self.ventana, textvariable=num_subsecciones_var)
        entrada_subsecciones.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Lista para almacenar los Entry de nombres de secciones
        nombres_subsecciones = []

        # Lista para almacenar los Text de información de subsecciones
        informacion_subsecciones = []

        # Checkbutton para mostrar nombres de secciones
        seleccion_var = tk.BooleanVar()
        seleccion_checkbutton = tk.Checkbutton(self.ventana, text="Mostrar Nombres de Secciones",
                                               variable=seleccion_var,
                                               command=mostrar_nombres_secciones)
        seleccion_checkbutton.grid(row=3, column=0, columnspan=2, pady=5)

        # Canvas para contener las subsecciones con Scrollbar
        canvas = tk.Canvas(self.ventana)
        canvas.grid(row=5, column=0, columnspan=3, pady=5)

        # Frame interior para las subsecciones
        frame_subsecciones = tk.Frame(canvas)
        frame_subsecciones.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Scrollbar vertical
        scrollbar_vertical = ttk.Scrollbar(self.ventana, orient="vertical", command=canvas.yview)
        scrollbar_vertical.grid(row=5, column=3, pady=5, sticky="ns")

        # Configurar el Canvas para usar la Scrollbar vertical
        canvas.configure(yscrollcommand=scrollbar_vertical.set)

        # Permitir que el Canvas expanda su altura al agregar subsecciones
        canvas.create_window((0, 0), window=frame_subsecciones, anchor="nw")

        # Botón para enviar el formulario
        boton_enviar = tk.Button(self.ventana, text="Enviar", command=enviar_formulario)
        boton_enviar.grid(row=6, columnspan=3, pady=10)

        # Llamada inicial a actualizar_desplazamiento
        actualizar_desplazamiento()

    def iniciar_interfaz(self):
        self.ventana.mainloop()


def query():
    estado['asistente'] = False
    estado['query'] = True
    ventana = tk.Tk()
    interfaz = InterfazGrafica(ventana)
    interfaz.iniciar_interfaz()
    estado['asistente'] = True
    estado['query'] = False
