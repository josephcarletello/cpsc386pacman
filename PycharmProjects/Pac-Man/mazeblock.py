import pygame
import constants
from time import sleep
from pygame.sprite import Sprite
from spritesheet_functions import SpriteSheet


class Mazeblock(Sprite):

    def __init__(self, ai_settings, screen):
        super(Mazeblock, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.mazeframe = []

        # Load the mazeblock image, and set its rect attribute.
        sprite_sheet = SpriteSheet('images/spreadsheet3.png')

        # self.image = sprite_sheet.get_image(352, 0, 32, 32)
        image = sprite_sheet.get_image(19, 1, 16, 16)
        self.mazeframe.append(image)

        self.image = self.mazeframe[0]

        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
