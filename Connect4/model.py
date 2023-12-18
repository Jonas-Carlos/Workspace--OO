from constants import LINHAS, COLUNAS
class Model:
    def __init__(self, LINHAS, COLUNAS):
        self.tabuleiro = [[0] * COLUNAS for _ in range(LINHAS)]
        self.jogador_atual = 1
        self.jogador1_nome = None
        self.jogador2_nome = None
        self.winner = None  

    def definir_nomes_jogadores(self, jogador1_nome, jogador2_nome):
        self.jogador1_nome = jogador1_nome
        self.jogador2_nome = jogador2_nome

    def reset(self):
        self.tabuleiro = [[0] * COLUNAS for _ in range(LINHAS)]
        self.jogador_atual = 1
        self.winner = None

    def verificar_vencedor(self):
        # Verificar vitória na horizontal
        for linha in range(LINHAS):
            for coluna in range(COLUNAS - 3):
                if self.tabuleiro[linha][coluna] == self.tabuleiro[linha][coluna + 1] == self.tabuleiro[linha][coluna + 2] == self.tabuleiro[linha][coluna + 3] != 0:
                    self.winner = self.jogador1_nome if self.jogador_atual == 1 else self.jogador2_nome
                    return True

        # Verificar vitória na vertical
        for coluna in range(COLUNAS):
            for linha in range(LINHAS - 3):
                if self.tabuleiro[linha][coluna] == self.tabuleiro[linha + 1][coluna] == self.tabuleiro[linha + 2][coluna] == self.tabuleiro[linha + 3][coluna] != 0:
                    self.winner = self.jogador1_nome if self.jogador_atual == 1 else self.jogador2_nome
                    return True

        # Verificar vitória na diagonal principal
        for linha in range(LINHAS - 3):
            for coluna in range(COLUNAS - 3):
                if self.tabuleiro[linha][coluna] == self.tabuleiro[linha + 1][coluna + 1] == self.tabuleiro[linha + 2][coluna + 2] == self.tabuleiro[linha + 3][coluna + 3] != 0:
                    self.winner = self.jogador1_nome if self.jogador_atual == 1 else self.jogador2_nome
                    return True

        # Verificar vitória na diagonal secundária
        for linha in range(3, LINHAS):
            for coluna in range(COLUNAS - 3):
                if self.tabuleiro[linha][coluna] == self.tabuleiro[linha - 1][coluna + 1] == self.tabuleiro[linha - 2][coluna + 2] == self.tabuleiro[linha - 3][coluna + 3] != 0:
                    self.winner = self.jogador1_nome if self.jogador_atual == 1 else self.jogador2_nome
                    return True

        return False

    def fazer_movimento(self, coluna):
        for linha in range(LINHAS-1, -1, -1):
            if self.tabuleiro[linha][coluna] == 0:
                self.tabuleiro[linha][coluna] = self.jogador_atual
                if self.verificar_vencedor():
                    print(f"Jogador {self.jogador_atual} venceu!")
                self.alternar_jogador()
                print(f"Tabuleiro após movimento:\n{self.tabuleiro}")
                print(f"Jogador atual: {self.jogador_atual}")
                break

    def alternar_jogador(self):
        self.jogador_atual = 3 - self.jogador_atual
