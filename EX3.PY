import tkinter as tk

# Criando a janela principal
janela = tk.Tk()
janela.title("Exemplo com Entry")
janela.geometry("400x300")

# Criando um rótulo
rotulo = tk.Label(janela, text="Digite seu nome:", font=("Arial", 12))
rotulo.pack(pady=10)

# Criando um campo de texto
entrada = tk.Entry(janela, font=("Arial", 12))
entrada.pack(pady=10)

# Função para exibir o texto inserido
def mostrar_nome():
    nome = entrada.get()
    rotulo.config(text=f"Olá, {nome}!")

# Criando um botão
botao = tk.Button(janela, text="Enviar", command=mostrar_nome, font=("Arial", 12))
botao.pack(pady=10)

# Iniciando o loop principal
janela.mainloop()
