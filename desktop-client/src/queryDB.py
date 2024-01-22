from auxiliar import estado
import tkinter as tk

# Top level window
frame = tk.Tk()
frame.title("Consultas a Base de Datos")
frame.geometry('1080x720')


def printInput():
    inp = seccion.get(1.0, "end-1c")
    #lbl.config(text="Provided Input: " + inp)
#panelSec = tk.PanedWindow(frame, orient=tk.HORIZONTAL)
#tk.Label(frame, text="Seccion").place(x=0,y=0)
# TextBox Creation
#texto = tk.Text(frame, height=5, width=100)
#texto.grid(row=0, column=1)




# Crear un PanedWindow
paned_window = tk.PanedWindow(frame, orient="horizontal")

# Crear dos Frame (contenedores) que se agregarán al PanedWindow
frame1 = tk.Frame(paned_window, background="lightblue")
frame2 = tk.Frame(paned_window, background="lightgreen")
txtSeccion = tk.Label(paned_window, text="Seccion")
seccion = tk.Text(paned_window, height=5, width=100)
seccion.grid(row=0, column=0)

# Agregar los Frames al PanedWindow
paned_window.add(txtSeccion)
paned_window.add(seccion)

# Establecer el tamaño inicial de cada sección del PanedWindow
paned_window.paneconfig(txtSeccion, minsize=100)
paned_window.paneconfig(seccion, minsize=100)









'''# Button Creation
printButton = tk.Button(frame, text="Print", command=printInput)
printButton.place(x=300,y=300)

# Label Creation
lbl = tk.Label(frame, text="")
lbl.place(x=200,y=200)'''
def modificar():
    frame.mainloop()
modificar()