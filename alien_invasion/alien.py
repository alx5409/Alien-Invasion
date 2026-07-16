import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .alien_invasion import AlienInvasion

class Alien(Sprite):
    # Class for representing a single alien in the fleet.

    def __init__(self, ai_game: "AlienInvasion"):
        # Initializes the alien the stablishes his initial position.
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Loads the alien image and configures the rect atribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Initializes a new alien close to the left top screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        # Saves the horizontal position of the alien.
        self.x = float(self.rect.x)

    def check_edges(self):
        # Return true if the alien is in the border of the screen.
        screen_rect = self.screen.get_rect()
        if not self.rect:
            raise ValueError("Alien rect is not initialized.")
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def update(self):
        if not self.rect:
            raise ValueError("Alien rect is not initialized.")
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
