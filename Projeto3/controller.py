# controller.py
import pygame
import sys
from model import Jogo

class ControladorJogo:
    def __init__(self, jogo, view):
        self.jogo = jogo
        self.view = view

    def jogar_partida(self):
        tempo_restante = self.jogo.tempo_total

        while tempo_restante > 0:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    alvo_rect = pygame.Rect(self.jogo.alvo.posicao, self.jogo.alvo.imagem.get_size())
                    if alvo_rect.collidepoint(x, y):
                        print("Alvo atingido!")
                        self.jogo.jogadores[0].pontos += 1
                        self.jogo.alvo.posicao = self.jogo.alvo.gerar_posicao()

            self.jogo.alvo.posicao = self.jogo.alvo.gerar_posicao()  # movimenta o alvo para uma nova posição aleatória

            # Limpa a tela
            self.view.tela.fill(self.view.cor_fundo)

            # Exibe o nome do jogador, a contagem de pontos e o tempo restante
            self.view.exibir_info(self.jogo.jogadores[0], tempo_restante, self.jogo.alvo)

            # Desenha o alvo na tela
            self.view.tela.blit(self.jogo.alvo.imagem, self.jogo.alvo.posicao)

            # Atualiza a tela
            pygame.display.flip()

            # Define a taxa de atualização
            pygame.time.delay(33)  # Aguarda 33 milissegundos (aproximadamente 30 quadros por segundo)

            # Atualiza o tempo restante
            tempo_restante -= 0.033  # Subtrai 1/30 (aproximadamente 0.033) a cada iteração

        return self.jogo.jogadores[0].pontos

    def determinar_vencedor(self):
        if self.jogo.jogadores[0].pontos > self.jogo.jogadores[1].pontos:
            return self.jogo.jogadores[0].nome
        elif self.jogo.jogadores[0].pontos < self.jogo.jogadores[1].pontos:
            return self.jogo.jogadores[1].nome
        else:
            return "Empate"

    def salvar_pontuacao(self):
        for jogador in self.jogo.jogadores:
            self.jogo.database.adicionar_jogador(jogador)
