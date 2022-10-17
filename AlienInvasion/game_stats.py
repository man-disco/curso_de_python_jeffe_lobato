class GameStats:
    """Armazena dados estatísticos do Alien Invasion."""
    def __init__(self, ai_settings):
        """Inicializa os dados estatísticos."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo."""
        self.ships_left = self.ai_settings.ships_left
        self.score = 0
        self.level = 1
        # A pontuação máxima jamais deverá ser reiniciada.

