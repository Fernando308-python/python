import tkinter as tk

class MinhaApp:
    def __init__(self, parent):
        self.myParent = parent
        self.frame = tk.Frame(parent)
        self.frame.pack(padx=10, pady=10)

        botoes = [("Botão 1", "green", 1, "Bom!"),
                  ("Botão 2", "red", 2, "Ruim!")]

        for nome, cor, identificador, msg in botoes:
            botao = tk.Button(self.frame, text=nome, background=cor)
            botao.pack(side=tk.LEFT, padx=5)
            # Usando lambda para capturar valores
            botao.bind("<Button-1>", lambda event, n=nome, i=identificador, m=msg: self.handler(n, i, m))

    def handler(self, nome, identificador, mensagem):
        print(f"Botão: {nome}, ID: {identificador}, Mensagem: {mensagem}")

# Criando a janela principal
root = tk.Tk()
root.title("Exemplo com Lambda")
root.geometry("400x300")

# Iniciando a aplicação
app = MinhaApp(root)

# Loop principal
root.mainloop()
