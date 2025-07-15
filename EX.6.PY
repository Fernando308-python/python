import tkinter as tk

class MinhaApp:
    def __init__(self, parent):
        self.myParent = parent
        self.frame = tk.Frame(parent)
        self.frame.pack(padx=10, pady=10)

        self.botao1 = tk.Button(self.frame, text="OK", background="green")
        self.botao1.pack(side=tk.LEFT, padx=5)
        self.botao1.bind("<Button-1>", self.botao1_clique)
        self.botao1.bind("<Return>", self.botao1_clique)
        self.botao1.focus_force()

        self.botao2 = tk.Button(self.frame, text="Cancelar", background="red")
        self.botao2.pack(side=tk.LEFT, padx=5)
        self.botao2.bind("<Button-1>", self.botao2_clique)

    def botao1_clique(self, event):
        cor_atual = self.botao1["background"]
        nova_cor = "yellow" if cor_atual == "green" else "green"
        self.botao1.configure(background=nova_cor)

    def botao2_clique(self, event):
        self.myParent.destroy()

# Criando a janela principal
root = tk.Tk()
root.title("Exemplo de Binding")
root.geometry("400x300")

# Iniciando o app
app = MinhaApp(root)

# Loop principal
root.mainloop()
