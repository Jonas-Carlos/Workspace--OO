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

            self.view.tela.fill(self.view.cor_fundo)

            self.view.exibir_info(self.jogo.jogadores[0], tempo_restante, self.jogo.alvo)

            self.view.tela.blit(self.jogo.alvo.imagem, self.jogo.alvo.posicao)

            pygame.display.flip()

            pygame.time.delay(33)  

            tempo_restante -= 0.033  

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
