import tkinter as tk

# Criando a janela principal
janela = tk.Tk()
janela.title("Exemplo com Botão")
janela.geometry("400x300")

# Criando um rótulo
rotulo = tk.Label(janela, text="Bem-vindo ao Tkinter!", font=("Noto", 14))
rotulo.pack(pady=10)

# Função para alterar o texto do rótulo
def clique_botao():
    rotulo.config(text="Botão clicado!")

# Criando um botão
botao = tk.Button(janela, text="Clique Aqui", command=clique_botao, font=("Noto", 12))
botao.pack(pady=10)

# Iniciando o loop principal
janela.mainloop()
