import pygame
import constants
from time import sleep
from pygame.sprite import Sprite
from spritesheet_functions import SpriteSheet


class Pellet(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        super(Pellet, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.pframe = []

        # Load the alien image, and set its rect attribute.
        sprite_sheet = SpriteSheet('images/spreadsheet5.png')

        image = sprite_sheet.get_image(6, 23, 4, 4)
        self.pframe.append(image)

        self.image = self.pframe[0]

        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
