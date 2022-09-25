class Settings:
    """Uma classe para armazenar todas as configurações da Invasão Alienígena."""
    def __init__(self):
        self.screen_width = 860
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Configurações da espaçonave.
        self.ship_speed_factor = 1.5
