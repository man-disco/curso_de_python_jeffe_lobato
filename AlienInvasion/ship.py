import pygame


class Ship:
    def __init__(self, screen):
        """Inicializa a espaçonave e define sua posição inicial."""
        self.screen = screen

        # Carrega a espaçonave e obtém seu rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Inicia cada nova espaçonave na parte inferior central da tela.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Flag de movimento.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Atualiza a posição da espaçonave conforme a flag de movimento."""
        # Se a flag estiver verdadeira, move a espaçonave para a direita.
        if self.moving_right:
            self.rect.centerx += 1

        # Se a flag estiver verdadeira, move a espaçonave para a esquerda.
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Desenha a espaçonave em sua posição atual."""
        self.screen.blit(self.image, self.rect)
