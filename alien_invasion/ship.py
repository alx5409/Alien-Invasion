import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    # Class for manage the ship
    def __init__(self, ai_game):
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
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #Updates the object rect of self.x.
        self.rect.x = self.x

    def blitme(self):
        # Draws the ship in his actual position.
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
