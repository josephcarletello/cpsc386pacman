import pygame
import constants
from time import sleep
from pygame.sprite import Sprite
from spritesheet_functions import SpriteSheet


class Pacman(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship, and set its starting position."""
        super(Pacman, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.frame = 0
        self.centerx = 300
        self.centery = 300
        self.pacframesl = []
        self.pacframesr = []
        self.pacframesu = []
        self.pacframesd = []
        self.pacex = []

        # Load the ship image, and get its rect.
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(0, 160, 32, 32)
        self.pacframesl.append(image)
        image = sprite_sheet.get_image(32, 160, 32, 32)
        self.pacframesl.append(image)
        image = sprite_sheet.get_image(0, 192, 32, 32)
        self.pacframesl.append(image)
        image = sprite_sheet.get_image(32, 192, 32, 32)
        self.pacframesl.append(image)
        self.image = self.pacframesl[0]

        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(0, 160, 32, 32)
        image = pygame.transform.rotate(image, 180)
        self.pacframesr.append(image)
        image = sprite_sheet.get_image(32, 160, 32, 32)
        image = pygame.transform.rotate(image, 180)
        self.pacframesr.append(image)
        image = sprite_sheet.get_image(0, 192, 32, 32)
        image = pygame.transform.rotate(image, 180)
        self.pacframesr.append(image)
        image = sprite_sheet.get_image(32, 192, 32, 32)
        image = pygame.transform.rotate(image, 180)
        self.pacframesr.append(image)

        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(0, 160, 32, 32)
        image = pygame.transform.rotate(image, 270)
        self.pacframesu.append(image)
        image = sprite_sheet.get_image(32, 160, 32, 32)
        image = pygame.transform.rotate(image, 270)
        self.pacframesu.append(image)
        image = sprite_sheet.get_image(0, 192, 32, 32)
        image = pygame.transform.rotate(image, 270)
        self.pacframesu.append(image)
        image = sprite_sheet.get_image(32, 192, 32, 32)
        image = pygame.transform.rotate(image, 270)
        self.pacframesu.append(image)

        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(0, 160, 32, 32)
        image = pygame.transform.rotate(image, 90)
        self.pacframesd.append(image)
        image = sprite_sheet.get_image(32, 160, 32, 32)
        image = pygame.transform.rotate(image, 90)
        self.pacframesd.append(image)
        image = sprite_sheet.get_image(0, 192, 32, 32)
        image = pygame.transform.rotate(image, 90)
        self.pacframesd.append(image)
        image = sprite_sheet.get_image(32, 192, 32, 32)
        image = pygame.transform.rotate(image, 90)
        self.pacframesd.append(image)

        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(0, 0, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(32, 0, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(64, 0, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(96, 0, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(0, 32, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(32, 32, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(64, 32, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(96, 32, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(0, 64, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(32, 64, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(64, 64, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(96, 64, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(0, 96, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(32, 96, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(64, 96, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(96, 96, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(0, 128, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(32, 128, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(64, 128, 32, 32)
        self.pacex.append(image)
        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(96, 128, 32, 32)
        self.pacex.append(image)

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centery = 304
        # self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx
        # self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.power = 0
        self.seconds = 0

    def center_pacman(self):
        """Center the ship on the screen."""
        self.rect.x = 300
        self.rect.y = 300
        self.centerx = self.rect.x
        self.rect.centerx = self.rect.x
        self.centery = self.rect.y
        self.rect.centery = self.rect.y
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def explosion(self, x):
        self.image = self.pacex[x]

    def update(self, pacmans, mazeblocks):

        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.

        if self.moving_left:
            collisions = pygame.sprite.groupcollide(pacmans, mazeblocks, False, False)
            if collisions:
                self.moving_left = False
                self.rect.centerx += 1
            else:
                self.update_left()

        if self.moving_right:
            collisions = pygame.sprite.groupcollide(pacmans, mazeblocks, False, False)
            if collisions:
                self.moving_right = False
                self.rect.centerx -= 1
            else:
                self.update_right()

        if self.moving_up:
            collisions = pygame.sprite.groupcollide(pacmans, mazeblocks, False, False)
            if collisions:
                self.moving_up = False
                self.rect.centery += 1
            else:
                self.update_up()

        if self.moving_down:
            collisions = pygame.sprite.groupcollide(pacmans, mazeblocks, False, False)
            if collisions:
                self.moving_down = False
                self.rect.centery -= 1
            else:
                self.update_down()

    def update_right(self):
        if self.rect.centerx < 584:
            if self.rect.centerx > 577:
                if self.rect.centery > 273:
                    if self.rect.centery < 337:
                        self.centerx = 20
                        self.rect.centerx = self.centerx
        if self.centerx < 584:
            self.centerx += self.ai_settings.pacman_speed_factor
            # Update rect object from self.center.
            self.rect.centerx = self.centerx

            # frame = (pos // 30) % len(self.pacframesl)
            self.frame += 1
            if self.frame > 3:
                self.frame = 0
            self.image = self.pacframesr[self.frame]

    def update_left(self):
        if self.rect.centerx < 30:
            if self.rect.centerx > 16:
                if self.rect.centery > 273:
                    if self.rect.centery < 337:
                        self.centerx = 584
                        self.rect.centerx = self.centerx

        if self.centerx > 16:
            self.centerx -= self.ai_settings.pacman_speed_factor
            # Update rect object from self.center.
            self.rect.centerx = self.centerx

            # frame = (pos // 30) % len(self.pacframesl)
            self.frame += 1
            if self.frame > 3:
                self.frame = 0
            self.image = self.pacframesl[self.frame]

    def update_up(self):
        if self.centery > 16:
            self.centery -= self.ai_settings.pacman_speed_factor
            # Update rect object from self.center.
            self.rect.centery = self.centery

            # frame = (pos // 30) % len(self.pacframesl)
            self.frame += 1
            if self.frame > 3:
                self.frame = 0
            self.image = self.pacframesu[self.frame]

    def update_down(self):
        if self.centery < 584:
            self.centery += self.ai_settings.pacman_speed_factor
            # Update rect object from self.center.
            self.rect.centery = self.centery

            # frame = (pos // 30) % len(self.pacframesl)
            self.frame += 1
            if self.frame > 3:
                self.frame = 0
            self.image = self.pacframesd[self.frame]

    def blitme (self):
        """Draw the pac at its current location."""
        self.screen.blit(self.image, self.rect)
