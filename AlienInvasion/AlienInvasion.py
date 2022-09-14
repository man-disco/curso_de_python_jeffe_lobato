import sys
import pygame
from settings import Settings
ai_settings = Settings()


def run_game():
    """Inicializa o jogo e cria um objeto para a tela."""
    pygame.init()
    # Cria a janela do pygame com a resolução escolhida.
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Nome da janela atual.
    pygame.display.set_caption("Alien Invasion")

    # Inicia os laços principais do jogo.
    while True:
        # Observa os eventos do teclado ou mouse.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        # Deixa a tela mais recente visível (atualiza o frame)
        pygame.display.flip()


run_game()