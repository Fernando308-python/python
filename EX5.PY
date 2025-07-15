import tkinter as tk

class MinhaApp:
    def __init__(self, parent):
        self.myParent = parent
        self.frame = tk.Frame(parent)
        self.frame.pack(padx=10, pady=10)

        tk.Label(self.frame, text="Nome:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entrada_nome = tk.Entry(self.frame, font=("Arial", 12))
        self.entrada_nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame, text="Idade:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entrada_idade = tk.Entry(self.frame, font=("Arial", 12))
        self.entrada_idade.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self.frame, text="Enviar", command=self.enviar, font=("Arial", 12)).grid(
            row=2, column=0, columnspan=2, pady=10
        )

    def enviar(self):
        nome = self.entrada_nome.get()
        idade = self.entrada_idade.get()
        print(f"Nome: {nome}, Idade: {idade}")

# Criando a janela principal
root = tk.Tk()
root.title("Exemplo com Grid")
root.geometry("400x300")

# Inicializando o app
app = MinhaApp(root)

# Iniciando o loop principal
root.mainloop()
