
import sys
from constants import LARGURA, ALTURA, BRANCO, LINHAS, COLUNAS, TAMANHO_CELULA, PRETO
import pygame

AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

class View:
    def __init__(self, model):
        pygame.init()
        self.model = model
        self.screen = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Connect 4")
        self.font = pygame.font.Font(None, 36)  
        self.messages = []  
        self.game_running = True  

    def obter_nomes_jogadores(self):
        jogador1 = input("Nome do Jogador 1: ")
        jogador2 = input("Nome do Jogador 2: ")
        return jogador1, jogador2

    def exibir_tela_inicial(self):
        self.screen.fill(BRANCO)
        jogador1, jogador2 = self.obter_nomes_jogadores()
        self.model.definir_nomes_jogadores(jogador1, jogador2)

    def exibir_opcao_novo_jogo(self):
        message = "Deseja jogar novamente? (S/N)"
        text = self.font.render(message, True, PRETO)
        self.screen.blit(text, (LARGURA // 2 - text.get_width() // 2, ALTURA // 2 - text.get_height() // 2))
        pygame.display.flip()

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.model.reset()
                        self.game_running = True
                        waiting_for_input = False
                    elif event.key == pygame.K_n:
                        pygame.quit()
                        sys.exit()

    def desenhar_tabuleiro(self):
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                pygame.draw.rect(self.screen, AZUL, (coluna * TAMANHO_CELULA, linha * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA), 0)

    def desenhar_pecas(self):
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                jogador = self.model.tabuleiro[linha][coluna]
                cor = VERMELHO if jogador == 1 else PRETO if jogador == 2 else BRANCO
                pygame.draw.circle(self.screen, cor, (coluna * TAMANHO_CELULA + TAMANHO_CELULA // 2, linha * TAMANHO_CELULA + TAMANHO_CELULA // 2), TAMANHO_CELULA // 2 - 5)

    def render_winner(self):
        if self.model.winner is not None:
            winner_text = f"{self.model.winner} venceu!"
            text = self.font.render(winner_text, True, PRETO)
            self.screen.blit(text, (LARGURA // 2 - text.get_width() // 2, ALTURA // 2 - text.get_height() // 2))
            self.exibir_opcao_novo_jogo()

    def render_messages(self):
        y_offset = 10
        for message in self.messages:
            text = self.font.render(message, True, PRETO)
            self.screen.blit(text, (10, y_offset))
            y_offset += 30

    def add_message(self, message):
        self.messages.append(message)

    def run(self):
        self.exibir_tela_inicial()

        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    coluna_clicada = event.pos[0] // TAMANHO_CELULA
                    message = f'Movimento na coluna {coluna_clicada}'
                    self.model.fazer_movimento(coluna_clicada)
                    self.add_message(message)
                    self.render_messages()

            self.screen.fill(BRANCO)
            self.desenhar_tabuleiro()
            self.desenhar_pecas()
            self.render_winner()
            self.render_messages()

            pygame.display.flip()

