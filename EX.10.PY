import tkinter as tk
import random

class JogoNave:
    def __init__(self, parent):
        self.myParent = parent
        self.canvas = tk.Canvas(parent, width=600, height=400, background="black")
        self.canvas.pack(padx=10, pady=10)

        # Criando a nave
        self.nave = self.canvas.create_rectangle(280, 360, 320, 380, fill="blue")
        self.velocidade = 5
        self.tiros = []
        self.inimigos = []
        self.pontuacao = 0
        self.game_over = False

        # Texto da pontuação
        self.txt_pontos = self.canvas.create_text(10, 10, anchor="nw", fill="white", font=("Arial", 14), text="Pontos: 0")

        # Vinculando eventos de teclado
        self.canvas.bind_all("<Left>", self.mover_esquerda)
        self.canvas.bind_all("<Right>", self.mover_direita)
        self.canvas.bind_all("<space>", self.disparar)

        # Iniciando a animação e inimigos
        self.animar()
        self.criar_inimigos()

    def mover_esquerda(self, event):
        if self.game_over:
            return
        x1, _, _, _ = self.canvas.bbox(self.nave)
        if x1 > 0:
            self.canvas.move(self.nave, -self.velocidade, 0)

    def mover_direita(self, event):
        if self.game_over:
            return
        _, _, x2, _ = self.canvas.bbox(self.nave)
        if x2 < 600:
            self.canvas.move(self.nave, self.velocidade, 0)

    def disparar(self, event):
        if self.game_over:
            return
        x1, y1, x2, _ = self.canvas.bbox(self.nave)
        tiro = self.canvas.create_oval(x1+15, y1-10, x2-15, y1, fill="red")
        self.tiros.append(tiro)

    def criar_inimigos(self):
        if self.game_over:
            return
        x = random.randint(10, 590)
        inimigo = self.canvas.create_oval(x, 0, x+30, 30, fill="gray")
        self.inimigos.append(inimigo)
        # Criar novo inimigo a cada 1.5 segundos
        self.myParent.after(1500, self.criar_inimigos)

    def animar(self):
        if self.game_over:
            return

        # Movimentar tiros para cima e remover se sair da tela
        for tiro in self.tiros[:]:
            self.canvas.move(tiro, 0, -10)
            if self.canvas.bbox(tiro)[1] < 0:
                self.canvas.delete(tiro)
                self.tiros.remove(tiro)

        # Movimentar inimigos para baixo e checar colisões
        for inimigo in self.inimigos[:]:
            self.canvas.move(inimigo, 0, 5)
            # Se inimigo chegar ao chão -> game over
            if self.canvas.bbox(inimigo)[3] >= 400:
                self.game_over = True
                self.canvas.create_text(300, 200, text="GAME OVER", font=("Arial", 40), fill="red")
                return

            # Checar colisão com tiros
            for tiro in self.tiros[:]:
                if self.colidiu(inimigo, tiro):
                    self.canvas.delete(inimigo)
                    self.canvas.delete(tiro)
                    self.inimigos.remove(inimigo)
                    self.tiros.remove(tiro)
                    self.pontuacao += 10
                    self.canvas.itemconfig(self.txt_pontos, text=f"Pontos: {self.pontuacao}")
                    break

        self.myParent.after(50, self.animar)

    def colidiu(self, obj1, obj2):
        x11, y11, x12, y12 = self.canvas.bbox(obj1)
        x21, y21, x22, y22 = self.canvas.bbox(obj2)
        return not (x12 < x21 or x11 > x22 or y12 < y21 or y11 > y22)

# Criando a janela principal
root = tk.Tk()
root.title("Mini-Jogo de Nave Turbinado")
root.geometry("620x420")

# Iniciando o jogo
app = JogoNave(root)

# Loop principal
root.mainloop()
