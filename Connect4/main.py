import pygame
import sys
from model import Model
from controller import Controller
from constants import BRANCO

LINHAS, COLUNAS = 6, 7

def main():
    pygame.init() 
    model = Model(LINHAS, COLUNAS)
    from view import View
    view = View(model)
    controller = Controller(model, view)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                controller.handle_event(event)

        view.screen.fill(BRANCO)
        view.desenhar_tabuleiro()
        view.desenhar_pecas()
        pygame.display.flip()

if __name__ == "__main__":
    main()
