import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk, UnidentifiedImageError
import mysql.connector

class CadastroProdutos:
    def __init__(self, parent):
        self.myParent = parent
        self.conexao = mysql.connector.connect(
            host="localhost", user="root", password="",
            database="python"
        )
        self.cursor = self.conexao.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255),
                preco FLOAT,
                imagem VARCHAR(255)
            )
        """)

        self.frame = tk.Frame(parent)
        self.frame.pack(padx=10, pady=10)

        # Formulário
        tk.Label(self.frame, text="Nome:", font=("Noto", 12)).grid(row=0, column=0, padx=5, pady=5)
        self.entrada_nome = ttk.Entry(self.frame, font=("Noto", 12))
        self.entrada_nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame, text="Preço:", font=("Noto", 12)).grid(row=1, column=0, padx=5, pady=5)
        self.entrada_preco = ttk.Entry(self.frame, font=("Noto", 12))
        self.entrada_preco.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame, text="Imagem:", font=("Noto", 12)).grid(row=2, column=0, padx=5, pady=5)
        self.entrada_imagem = ttk.Entry(self.frame, font=("Noto", 12))
        self.entrada_imagem.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(self.frame, text="Selecionar Imagem", command=self.selecionar_imagem).grid(row=2, column=2, padx=5, pady=5)
        ttk.Button(self.frame, text="Cadastrar", command=self.cadastrar).grid(row=3, column=0, columnspan=3, pady=10)

        # Visualização da imagem
        self.canvas = tk.Canvas(self.frame, width=200, height=200)
        self.canvas.grid(row=4, column=0, columnspan=3, pady=10)
    def selecionar_imagem(self):
        caminho = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg;*.png")])
        if caminho:
            self.entrada_imagem.delete(0, tk.END)
            self.entrada_imagem.insert(0, caminho)

            try:
                imagem = Image.open(caminho).resize((200, 200), Image.LANCZOS)
                self.imagem_tk = ImageTk.PhotoImage(imagem)
                self.canvas.create_image(100, 100, image=self.imagem_tk)
            except PermissionError:
                messagebox.showerror("Erro", "Permissão negada ao acessar a imagem. Tente copiar o arquivo para outra pasta.")
            except UnidentifiedImageError:
                messagebox.showerror("Erro", "Não foi possível abrir a imagem. Verifique o formato do arquivo.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar imagem:\n{e}")

    def cadastrar(self):
        nome = self.entrada_nome.get()
        preco = self.entrada_preco.get()
        imagem = self.entrada_imagem.get()

        if nome and preco.replace(".", "").isdigit() and imagem:
            try:
                self.cursor.execute("INSERT INTO produtos (nome, preco, imagem) VALUES (%s, %s, %s)", (nome, float(preco), imagem))
                self.conexao.commit()
                messagebox.showinfo("Sucesso", "Produto cadastrado!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao cadastrar produto: {e}")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente!")

# Iniciar interface
root = tk.Tk()
root.title("Cadastro de Produtos")
root.geometry("600x500")
app = CadastroProdutos(root)
root.mainloop()
