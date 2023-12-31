import pygame
import random
import sys

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0

class Alvo:
    def __init__(self, view, imagem_alvo):
        self.view = view
        self.imagem = pygame.image.load(imagem_alvo)
        self.imagem = pygame.transform.scale(self.imagem, (50, 50))
        self.posicao = self.gerar_posicao()

    def gerar_posicao(self):
        largura_tela, altura_tela = self.view.largura_tela, self.view.altura_tela
        x = random.randint(0, largura_tela - self.imagem.get_width())
        y = random.randint(0, altura_tela - self.imagem.get_height())
        return x, y

class Database:
    def __init__(self):
        self.dados = {}

    def adicionar_jogador(self, jogador):
        self.dados[jogador.nome] = jogador.pontos

    def obter_pontuacao(self, nome):
        return self.dados.get(nome, 0)

class Jogo:
    def __init__(self, largura_tela, altura_tela, database, view, imagem_alvo):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.database = database
        self.view = view
        self.tempo_total = 20  
        self.jogadores = [Jogador(""), Jogador("")]

        self.alvo = Alvo(self.view, imagem_alvo)

    def jogar_partida(self):
        pontos = 0
        tempo_restante = self.tempo_total

        while tempo_restante > 0:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    alvo_rect = pygame.Rect(self.alvo.posicao, self.alvo.imagem.get_size())
                    if alvo_rect.collidepoint(x, y):
                        print("Alvo atingido!")
                        self.jogadores[0].pontos += 1
                        self.alvo.posicao = self.alvo.gerar_posicao()

            self.alvo.posicao = self.alvo.gerar_posicao() 
            self.view.tela.fill(self.view.cor_fundo)
            self.view.exibir_info(self.jogadores[0], tempo_restante, self.alvo)

            self.view.tela.blit(self.alvo.imagem, self.alvo.posicao)

            pygame.display.flip()

            pygame.time.delay(33)  # 30 fps

            tempo_restante -= 0.033  

        return self.jogadores[0].pontos
