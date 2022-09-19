import pygame
import sys


def check_events(ship):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def event_KEYUP():
    """Observa eventos do teclado quando a tecla é solta."""


def update_screen(ai_settings, screen, ship):
    """Atualiza as imagens na
    tela e alterna para a nova tela."""
    # Desenha a nave.
    ship.blitme()

    # Deixa a tela mais recente visível (atualiza o frame)
    pygame.display.flip()
    screen.fill(ai_settings.bg_color)
