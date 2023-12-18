import pygame
from constants import TAMANHO_CELULA
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_event(self, event):
          if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            coluna_clicada = event.pos[0] // TAMANHO_CELULA
            print(f'Movimento na coluna {coluna_clicada}')
            self.model.fazer_movimento(coluna_clicada)
