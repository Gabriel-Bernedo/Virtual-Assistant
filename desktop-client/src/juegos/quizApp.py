import tkinter as tk
from PIL import Image, ImageTk
from utils_audio import hablar
import asyncio
class ComputerStructureQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JUEGO: Modos de direccionamiento")

        self.question_label = tk.Label(root, text="¿Cual no es una operacion logica?")
        asyncio.run(hablar("¿Cual no es una operacion logica?",False))
        self.question_label.pack()

        self.image_frame = tk.Frame(root)
        self.image_frame.pack()

        self.image_labels = []
        for _ in range(4):
            image_label = tk.Label(self.image_frame, image=None)
            image_label.pack(side=tk.LEFT, padx=10)
            image_label.bind("<Button-1>", self.check_answer)
            self.image_labels.append(image_label)

        self.correct_answer = 2  # Índice de la respuesta correcta
        self.load_question()

    def load_question(self):
        # Cargar la pregunta y las imágenes aquí
        question = "¿Cual no es una operacion logica?"
        options = ["AND", "OR", "ADD", "NOT"]
        
        self.question_label.config(text=question)
        self.correct_answer = 2  # Respuesta correcta en la posición 0 (RAM)

        for i in range(4):
            image_path = f"img/{options[i]}.png"
            image = Image.open(image_path)
            image = image.resize((200, 200))
            photo = ImageTk.PhotoImage(image)
            self.image_labels[i].config(image=photo)
            self.image_labels[i].image = photo

    def check_answer(self, event):
        clicked_label = event.widget
        clicked_index = self.image_labels.index(clicked_label)

        if clicked_index == self.correct_answer:
            asyncio.run(hablar("Respuesta correcta.", False))
            self.root.destroy()  # Cierra la aplicación al dar la respuesta correcta
        else:
            asyncio.run(hablar("Respuesta incorrecta. Intentalo de nuevo", False))

            # Verificar si la ventana aún está abierta antes de cargar la siguiente pregunta
            if self.root.winfo_exists():
                self.load_question()

