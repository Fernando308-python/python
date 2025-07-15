import tkinter as tk
from tkinter import filedialog, messagebox

class EditorTexto:
    def __init__(self, parent):
        self.myParent = parent
        self.frame = tk.Frame(parent)
        self.frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.texto = tk.Text(self.frame, font=("Noto", 12), height=10)
        self.texto.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

        self.menu = tk.Menu(parent)
        parent.config(menu=self.menu)

        self.menu_arquivo = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Arquivo", menu=self.menu_arquivo)
        self.menu_arquivo.add_command(label="Salvar", command=self.salvar)
        self.menu_arquivo.add_command(label="Sair", command=self.sair)

    def salvar(self):
        arquivo = filedialog.asksaveasfilename(defaultextension=".txt")
        if arquivo:
            with open(arquivo, "w", encoding="utf-8") as f:
                f.write(self.texto.get("1.0", tk.END))
            messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso!")

    def sair(self):
        self.myParent.destroy()

# Execução principal
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Editor de Texto")
    root.geometry("600x400")
    app = EditorTexto(root)
    root.mainloop()
