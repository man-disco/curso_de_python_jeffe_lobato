import pygame
import sys


def check_events():
    """Responde a eventos de pressionamento de teclas e de mouse."""
    # Observa eventos de teclado e de mouse.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """"Atualiza as imagens na tela e alterna para a nova tela."""
    # Redesenha a tela a cada passagem pelo laço.
    screen.fill(ai_settings.bg_color)
    # Deixa a tela mais recente visível.
    ship.blitme()
    pygame.display.flip()