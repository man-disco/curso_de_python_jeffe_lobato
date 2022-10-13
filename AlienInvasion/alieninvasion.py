import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Inicializa o pygame, as configurações e o objeto screen.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Limita e mostra o fps.
    fps = 1000
    clock = pygame.time.Clock()

    # Cria o botão play.
    play_button = Button(ai_settings, screen, "Play")

    # Cria uma instância para armazenar dados estatísticos do jogo
    # e cria painel de pontuação.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Cria uma espaçonave, um grupo de alienígenas e um grupo de balas.
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Inicia o laço principal do jogo.
    while True:
        clock.tick(fps)

        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button, sb)


run_game()
