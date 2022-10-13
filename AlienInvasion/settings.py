class Settings:
    """Uma classe para armazenar todas as configurações da Invasão Alienígena."""
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Configurações da espaçonave.
        self.ships_left = 3

        # Configurações de projéteis.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 60, 60)
        self.bullets_allowed = 3

        # Configurações dos alienígenas.
        self.fleet_drop_speed = 10

        # A taxa com o que a velocidade do jogo aumenta.
        self.speedup_scale = 1.1

        # A taxa com o que os pontos para cada alienígena aumentam.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializa as configurações que mudam no decorrer do jogo."""
        self.alien_speed_factor = 1
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        # fleet_direction igual à 1 representa a direita; -1 representa a esquerda.
        self.fleet_direction = 1

        # Pontuação.
        self.alien_points = 50

    def increase_speed(self):
        """Aumenta as configurações de velocidade."""
        self.alien_speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

