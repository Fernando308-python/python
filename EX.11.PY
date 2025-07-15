import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class MinhaApp:
    def __init__(self, parent):
        self.myParent = parent
        self.canvas = tk.Canvas(parent, width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Caminho absoluto da imagem
        caminho_imagem = "C:/Users/Aluno/Downloads/20250714 - Aulas 44/background.jpg"
        
        # Verifica se o arquivo existe antes de abrir
        if not os.path.exists(caminho_imagem):
            messagebox.showerror("Erro", f"Arquivo não encontrado:\n{caminho_imagem}")
            parent.destroy()  # Fecha o app caso a imagem não exista
            return
        
        # Carregando e redimensionando a imagem
        imagem = Image.open(caminho_imagem)
        imagem = imagem.resize((800, 600), Image.LANCZOS)
        self.background_image = ImageTk.PhotoImage(imagem)
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        # Adicionando um formulário
        self.frame = tk.Frame(self.canvas, bg="white")
        self.canvas.create_window(400, 300, window=self.frame)

        tk.Label(self.frame, text="Usuário:", font=("Noto", 12), bg="white").grid(row=0, column=0, padx=5, pady=5)
        self.entrada_usuario = tk.Entry(self.frame, font=("Noto", 12))
        self.entrada_usuario.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.frame, text="Entrar", command=self.entrar).grid(row=1, column=0, columnspan=2, pady=5)

    def entrar(self):
        usuario = self.entrada_usuario.get()
        print(f"Entrar clicado! Usuário: {usuario}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Formulário com Imagem")
    root.geometry("800x600")
    app = MinhaApp(root)
    root.mainloop()
