import pygame
import sys

class View:
    def __init__(self, largura_tela, altura_tela):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.cor_fundo = (255, 255, 255)

        pygame.init()
        self.tela = pygame.display.set_mode((self.largura_tela, self.altura_tela))
        pygame.display.set_caption("Jogo de Tiro ao Alvo")

        self.fonte = pygame.font.Font(None, 36)

    def obter_nomes_jogadores(self, jogadores):
        for jogador in jogadores:
            input_active = True
            while input_active:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_RETURN:
                            input_active = False
                        elif evento.key == pygame.K_BACKSPACE:
                            jogador.nome = jogador.nome[:-1]
                        else:
                            jogador.nome += evento.unicode

                self.tela.fill(self.cor_fundo)
                texto_instrucao = self.fonte.render(f"Digite o nome do jogador {jogadores.index(jogador) + 1} e pressione Enter:", True, (0, 0, 0))
                self.tela.blit(texto_instrucao, (10, 10))
                texto_nome_digitado = self.fonte.render(jogador.nome, True, (0, 0, 0))
                self.tela.blit(texto_nome_digitado, (10, 50))
                pygame.display.flip()
                pygame.time.delay(33)

    def exibir_info(self, jogador, tempo_restante, alvo):
        texto_nome = self.fonte.render(f"Jogador: {jogador.nome}", True, (0, 0, 0))
        texto_pontos = self.fonte.render(f"Pontos: {jogador.pontos}", True, (0, 0, 0))
        texto_tempo = self.fonte.render(f"Tempo: {int(tempo_restante)} s", True, (0, 0, 0))

        self.tela.fill(self.cor_fundo)

        self.tela.blit(texto_nome, (10, 10))
        self.tela.blit(texto_pontos, (10, 50))
        self.tela.blit(texto_tempo, (10, 90))

    def exibir_vencedor(self, vencedor):
        self.tela.fill(self.cor_fundo)
        texto_vencedor = self.fonte.render(f"Vencedor: {vencedor}", True, (0, 0, 0))
        self.tela.blit(texto_vencedor, (10, 10))
        pygame.display.flip()
        pygame.time.delay(3000)
