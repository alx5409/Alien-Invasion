from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .alien_invasion import AlienInvasion

class GameStats:
    ship_left: int
    def __init__(self, ai_game: "AlienInvasion"):
        self.settings = ai_game.settings
        self.reset_stats()
        # Starts the game in an inactive state.
        self.game_active = False

        # Highest registered score.
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1