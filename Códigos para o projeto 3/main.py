import pygame
import sys
from model import Jogador, Alvo, Database, Jogo
from view import View
from controller import ControladorJogo

if __name__ == "__main__":
    pygame.init()

    database = Database()

    view = View(800, 600)

    # Passe a instância de View para o ControladorJogo
    jogo_controller = ControladorJogo(
        Jogo(800, 600, database, view, "alvo.png"),  
        view
    )

    jogadores = [Jogador(""), Jogador("")]
    jogo_controller.view.obter_nomes_jogadores(jogadores)
    pontos_partida = jogo_controller.jogar_partida()
    vencedor = jogo_controller.determinar_vencedor()
    jogo_controller.salvar_pontuacao()
    jogo_controller.view.exibir_vencedor(vencedor)
    pygame.quit()
    sys.exit()
