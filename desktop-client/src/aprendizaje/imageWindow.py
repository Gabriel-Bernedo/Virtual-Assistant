import tkinter as tk
from PIL import Image, ImageTk
class ImageWindow:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("Imagen")
        
        self.image = Image.open(image_path)
        self.tk_image = ImageTk.PhotoImage(self.image)
        
        self.image_label = tk.Label(root, image=self.tk_image)
        self.image_label.pack()
        
    def update(self):
        # Actualizar la ventana (puedes agregar lógica de actualización aquí si es necesario)
        self.root.update_idletasks()
        self.root.after(100, self.update)  # Llama a la función de actualización cada 100 ms
