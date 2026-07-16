import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface
from pygame.rect import Rect

from .alien_invasion import AlienInvasion
from .settings import Settings

class Ship(Sprite):
    screen: Surface
    screen_rect: Rect
    settings: Settings
    # Class for manage the ship
    def __init__(self, ai_game: AlienInvasion):
        super().__init__()
        #Initializes the ship and configures its initial position.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
    
        # Loads the ship image and gets its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Puts initially each new ship in the center of the inferior part of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Save a decimal value for the horizontal position of the ship
        self.x = float(self.rect.x)

        # Flag of movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Updates the position of the ship depending on the flag of movement.
        if not self.image or not self.rect:
            raise ValueError("Ship image or rect is not initialized.")
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #Updates the object rect of self.x.
        self.rect.x = self.x

    def blitme(self):
        # Draws the ship in his actual position.
        if not self.image or not self.rect:
            raise ValueError("Ship image or rect is not initialized.")
        self.screen.blit(source=self.image, dest=self.rect)

    def center_ship(self):
        if not self.rect or not self.screen_rect:
            raise ValueError("Ship rect or screen rect is not initialized.")
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
