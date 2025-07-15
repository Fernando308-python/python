import tkinter as tk

class MinhaApp:
    def __init__(self, parent):
        self.myParent = parent
        self.buttons_frame = tk.Frame(parent, background="lightgray")
        self.buttons_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.botao1 = tk.Button(self.buttons_frame, text="Botão 1", background="green")
        self.botao1.pack(side=tk.LEFT, padx=5, pady=5)

        self.botao2 = tk.Button(self.buttons_frame, text="Botão 2", background="yellow")
        self.botao2.pack(side=tk.LEFT, padx=5, pady=5)

        self.botao3 = tk.Button(self.buttons_frame, text="Botão 3", background="red")
        self.botao3.pack(side=tk.LEFT, padx=5, pady=5)

# Criando a janela principal
root = tk.Tk()
root.title("Exemplo com Pack")
root.geometry("400x300")

# Inicializando o aplicativo
app = MinhaApp(root)

# Iniciando o loop principal
root.mainloop()
