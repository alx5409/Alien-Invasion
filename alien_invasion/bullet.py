import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        # Creates an object for the bullet in the current position of the ship.
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Creates a rectangle for the bullet in (0,0) y then establishes the correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Saves the position of the bullet as decimal
        self.y = float(self.rect.y)
        
    def update(self):
        # Moves the bullet to the top screen.
        # Updates the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # Updates the rectangle position.
        self.rect.y = self.y

    def draw_bullet(self):
        # Draws the bullet on the screen.
        pygame.draw.rect(self.screen, self.color, self.rect)