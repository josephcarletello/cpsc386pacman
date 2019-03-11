import pygame
from time import sleep
from spritesheet_functions import SpriteSheet
from pygame.sprite import Sprite


class Pinky(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        super(Pinky, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.frame = 0
        self.redr = []
        self.redl = []
        self.redu = []
        self.redd = []
        self.redblue = []

        # Load the alien image, and set its rect attribute.
        sprite_sheet = SpriteSheet('images/spreadsheet.png')

        image = sprite_sheet.get_image(160, 128, 32, 32)
        self.redr.append(image)
        image = sprite_sheet.get_image(160, 160, 32, 32)
        self.redr.append(image)

        image = sprite_sheet.get_image(160, 128, 32, 32)
        image = pygame.transform.flip(image, 1, 0)
        self.redl.append(image)
        image = sprite_sheet.get_image(160, 160, 32, 32)
        image = pygame.transform.flip(image, 1, 0)
        self.redl.append(image)

        image = sprite_sheet.get_image(160, 192, 32, 32)
        self.redu.append(image)
        image = sprite_sheet.get_image(160, 224, 32, 32)
        self.redu.append(image)

        image = sprite_sheet.get_image(64, 224, 32, 32)
        image = pygame.transform.rotate(image, 90)
        self.redblue.append(image)
        image = sprite_sheet.get_image(96, 224, 32, 32)
        image = pygame.transform.rotate(image, 90)
        self.redblue.append(image)

        sprite_sheet = SpriteSheet('images/spreadsheet.png')
        image = sprite_sheet.get_image(192, 0, 32, 32)
        self.redd.append(image)
        image = sprite_sheet.get_image(192, 32, 32, 32)
        self.redd.append(image)

        self.image = self.redr[0]

        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.rect.centery = 250
        self.rect.centerx = 300

        self.centery = self.rect.centery
        self.centerx = self.rect.centerx

        # Store the alien's exact position.
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = True
        self.moving_down = False
        self.lastmove = 5

    def update(self, mazeblocks):
        if self.moving_left:
            collisions = pygame.sprite.spritecollide(self, mazeblocks, False)
            if collisions:
                time = pygame.time.get_ticks() % 3
                if time == 0:
                    if self.lastmove == 2:
                        self.moving_left = False
                        self.moving_up = True
                        self.rect.centerx += 1
                    else:
                        self.moving_left = False
                        self.moving_down = True
                        self.rect.centerx += 1
                    self.lastmove = 4
                elif time == 1:
                    if self.lastmove == 8:
                        self.moving_left = False
                        self.moving_down = True
                        self.rect.centerx += 1
                    else:
                        self.moving_left = False
                        self.moving_up = True
                        self.rect.centerx += 1
                    self.lastmove = 4
                elif time == 2:
                    self.moving_left = False
                    self.moving_right = True
                    self.rect.centerx += 1
            else:
                self.update_left()

        elif self.moving_right:
            collisions = pygame.sprite.spritecollide(self, mazeblocks, False)
            if collisions:
                time = pygame.time.get_ticks() % 3
                if time == 0:
                    if self.lastmove == 2:
                        self.moving_right = False
                        self.moving_up = True
                        self.rect.centerx -= 1
                    else:
                        self.moving_right = False
                        self.moving_down = True
                        self.rect.centerx -= 1
                    self.lastmove = 6
                elif time == 1:
                    if self.lastmove == 8:
                        self.moving_right = False
                        self.moving_down = True
                        self.rect.centerx -= 1
                    else:
                        self.moving_right = False
                        self.moving_up = True
                        self.rect.centerx -= 1
                    self.lastmove = 6
                elif time == 2:
                    self.moving_right = False
                    self.moving_left = True
                    self.rect.centerx -= 1
            else:
                self.update_right()

        elif self.moving_up:
            collisions = pygame.sprite.spritecollide(self, mazeblocks, False)
            if collisions:
                time = pygame.time.get_ticks() % 3
                if time == 0:
                    if self.lastmove == 6:
                        self.moving_up = False
                        self.moving_right = True
                        self.rect.centery += 1
                    else:
                        self.moving_up = False
                        self.moving_left = True
                        self.rect.centery += 1
                    self.lastmove = 8
                elif time == 1:
                    self.moving_up = False
                    self.moving_down = True
                    self.rect.centery += 1
                elif time == 2:
                    if self.lastmove == 4:
                        self.moving_up = False
                        self.moving_right = True
                        self.rect.centery += 1

                    else:
                        self.moving_up = False
                        self.moving_left = True
                        self.rect.centery += 1
                    self.lastmove = 8
            else:
                self.update_up()

        elif self.moving_down:
            collisions = pygame.sprite.spritecollide(self, mazeblocks, False)
            if collisions:
                time = pygame.time.get_ticks() % 3
                if time == 0:
                    self.moving_down = False
                    self.moving_up = True
                    self.rect.centery -= 1
                elif time == 1:
                    if self.lastmove == 6:
                        self.moving_down = False
                        self.moving_left = True
                        self.rect.centery -= 1
                    else:
                        self.moving_down = False
                        self.moving_right = True
                        self.rect.centery -= 1
                    self.lastmove = 2
                elif time == 2:
                    if self.lastmove == 4:
                        self.moving_down = False
                        self.moving_right = True
                        self.rect.centery -= 1
                    else:
                        self.moving_down = False
                        self.moving_left = True
                        self.rect.centery -= 1
                    self.lastmove = 2
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
            self.centerx += self.ai_settings.ghost_speed_factor
            # Update rect object from self.center.
            self.rect.centerx = self.centerx

            self.frame += 1
            if self.frame > 1:
                self.frame = 0
            self.image = self.redr[self.frame]

    def update_left(self):
        if self.rect.centerx < 30:
            if self.rect.centerx > 16:
                if self.rect.centery > 273:
                    if self.rect.centery < 337:
                        self.centerx = 584
                        self.rect.centerx = self.centerx

        if self.centerx > 16:
            self.centerx -= self.ai_settings.ghost_speed_factor
            # Update rect object from self.center.
            self.rect.centerx = self.centerx

            # frame = (pos // 30) % len(self.pacframesl)
            self.frame += 1
            if self.frame > 1:
                self.frame = 0
            self.image = self.redl[self.frame]

    def update_up(self):
        if self.centery > 16:
            self.centery -= self.ai_settings.ghost_speed_factor
            # Update rect object from self.center.
            self.rect.centery = self.centery

            # frame = (pos // 30) % len(self.pacframesl)
            self.frame += 1
            if self.frame > 1:
                self.frame = 0
            self.image = self.redu[self.frame]

    def update_down(self):
        if self.centery < 584:
            self.centery += self.ai_settings.ghost_speed_factor
            # Update rect object from self.center.
            self.rect.centery = self.centery

            # frame = (pos // 30) % len(self.pacframesl)
            self.frame += 1
            if self.frame > 1:
                self.frame = 0
            self.image = self.redd[self.frame]

    def explosion(self):
        self.screen.blit(self.image, self.rect)

    def center_pinky(self):
        """Center the ship on the screen."""
        self.rect.centery = 250
        self.rect.centerx = 300
        self.centerx = self.rect.x
        self.rect.centerx = self.rect.x
        self.centery = self.rect.y
        self.rect.centery = self.rect.y

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)