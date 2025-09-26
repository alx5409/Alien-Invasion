import sys 

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from time import sleep
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    # General class for resource managing and game behaviour.

    def __init__(self):
        # Initializes the game and resources.
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        # Creates an instance to save the game stats.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        
        # Creates the Play button.
        self.play_button = Button(self, 'Click to play')

        self._create_fleet()

    def run_game(self):
        # Initializes the main loop for the game.
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            
    def _check_events(self):
        # Respods to keyboard and mouse inputs.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the right
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            # Creates a new bullet and adds it to the group of bullets.
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        # Updates the position of the bullets and discards the old ones.
        self.bullets.update()
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
        
    def _create_fleet(self):
        # Creates the alien fleet.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        avaible_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = avaible_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        avaible_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = avaible_space_y // (2 * alien_height)

        # Creates the first row of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
            

    def _create_alien(self, alien_number, row_number):
        # Creates an alien and puts it in the row.
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
            self.aliens.add(alien)


    def _update_screen(self):
        # Updates screen images and changes to the new screen.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb.show_score()

        # Draws the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()
    
    def _update_aliens(self):
        # Checks if the fleet is in a border
        self._check_fleet_edges()
        # Updates the position of all aliens of the fleet.
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        self._check_aliens_bottom()
    
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _check_bullet_alien_collisions(self):
        # Search for sucessful bullets.
        # If there are any, removes the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            # Destroys the bullets and creates a new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Level up.
            self.stats.level += 1
            self.sb.prep_level()
    
    def _ship_hit(self):
        
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1
            self.sb.prep_ships()

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()


            sleep(2)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
    
    def _check_play_button(self, mouse_pos):
        # Starts a new game when the player makes click in Play.
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Restablishes the game configuration.
            self.settings.initialize_dynamic_settings()
            # Restrablishes the gamestats.
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_high_score()
            self.sb.prep_level()
            self.sb.prep_ships()
        
            # Removes the aliens and the bullets left.
            self.aliens.empty()
            self.bullets.empty()

            # Creates a new fleet and centers the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hides the mouse cursor.
            pygame.mouse.set_visible(False)

if __name__ == '__main__':
    # Makes a game instance and executes it.
    ai = AlienInvasion()
    ai.run_game()
    