import pygame.font
from pygame.sprite import Group

from pacman import Pacman

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats, high_score):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (255, 255, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score(high_score)
        self.prep_level()
        self.prep_pacmans()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self, high_score):
        """Turn the high score into a rendered image."""
        self.high_score = int(round(high_score, -1))
        high_score_str = "{:,}".format(self.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_pacmans(self):
        """Show how many pacmans are left."""
        self.pacmans = Group()
        for pacman_number in range(self.stats.pacmans_left):
            pacman = Pacman(self.ai_settings, self.screen)
            pacman.rect.x = 10 + pacman_number * pacman.rect.width * 1.25
            pacman.rect.y = 10
            self.pacmans.add(pacman)

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # Draw pacman.
        self.pacmans.draw(self.screen)
