import tkinter as tk
from tkinter import ttk

class MinhaApp:
    def __init__(self, parent):
        self.myParent = parent
        self.frame = tk.Frame(parent)
        self.frame.pack(padx=10, pady=10)

        # Combobox para selecionar categorias
        tk.Label(self.frame, text="Categoria:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.categoria = ttk.Combobox(self.frame, values=["Eletrônicos", "Roupas", "Livros"], font=("Arial", 12))
        self.categoria.grid(row=0, column=1, padx=5, pady=5)
        self.categoria.set("Eletrônicos")

        # Treeview para exibir produtos
        self.tree = ttk.Treeview(self.frame, columns=("Nome", "Preço"), show="headings")
        self.tree.heading("Nome", text="Nome do Produto")
        self.tree.heading("Preço", text="Preço (R$)")
        self.tree.grid(row=1, column=0, columnspan=2, pady=10)

        # Botão para adicionar item
        ttk.Button(self.frame, text="Adicionar", command=self.adicionar).grid(row=2, column=0, columnspan=2, pady=5)

    def adicionar(self):
        categoria = self.categoria.get()
        self.tree.insert("", tk.END, values=(f"Produto {categoria}", "99.90"))

# Criando a janela principal
root = tk.Tk()
root.title("Exemplo com TTK")
root.geometry("500x400")

# Iniciando a aplicação
app = MinhaApp(root)

# Loop principal
root.mainloop()
