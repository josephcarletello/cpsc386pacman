import sys
import pygame
import inspect
from time import sleep
from mazeblock import Mazeblock
from pellet import Pellet
from powerpellet import PowerPellet
from spritesheet_functions import SpriteSheet


def update_screen(ai_settings, screen, stats, sb, pacman, play_button, mazeblock, mazeblocks, mazeblock_number, pellets, powerpellets, pellets_number, ghosts, blinky, pinky, inky, clyde):
    if not stats.game_active:
        update_menu(ai_settings, screen, stats, pacman, play_button, blinky, pinky, inky, clyde)

    else:

        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen, each pass through the loop.
        screen.fill(ai_settings.bg_color)

        # Draw Pacman
        pacman.blitme()

        # Draw the score information.


        for mazeblock in mazeblocks.sprites():
            mazeblock.blitme()

        for pellet in pellets.sprites():
            pellet.blitme()

        for powerpellet in powerpellets.sprites():
            powerpellet.blitme()

        for ghost in ghosts.sprites():
            ghost.blitme()

        sb.show_score()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


def update_menu(ai_settings, screen, stats, pacman, play_button, blinky, pinky, inky, clyde):

    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(ai_settings.bg_color)

    play_button.draw_button()
    myfont = pygame.font.SysFont('arial', 40)
    mytitle = pygame.font.SysFont('arial', 2)

    titletext = myfont.render('Pac-Man', False, (255, 255, 0))

    # Draw Pacman
    pacman.rect.x = 360
    pacman.rect.y = 280
    pacman.blitme()
    pactext = myfont.render('Pac-Man', False, (255, 255, 0))

    blinky.rect.x = 360
    blinky.rect.y = 330
    blinky.blitme()
    blitext = myfont.render('Blinky', False, (255, 0, 0))

    pinky.rect.x = 360
    pinky.rect.y = 380
    pinky.blitme()
    pitext = myfont.render('Pinky', False, (255, 0, 255))

    inky.rect.x = 360
    inky.rect.y = 430
    inky.blitme()
    itext = myfont.render('Inky', False, (0, 255, 255))

    clyde.rect.x = 360
    clyde.rect.y =480
    clyde.blitme()
    clytext = myfont.render('Clyde', False, (255, 125, 0))

    screen.blit(titletext, (240, 100))
    screen.blit(clytext, (200, 472))
    screen.blit(itext, (200, 422))
    screen.blit(pitext, (200, 372))
    screen.blit(blitext, (200, 322))
    screen.blit(pactext, (200, 272))
    pygame.display.flip()


def update_positions(pacman, pacmans, mazeblocks, blinky, pinky, clyde, inky):
    pacman.update(pacmans, mazeblocks)
    blinky.update(mazeblocks)
    pinky.update(mazeblocks)
    clyde.update(mazeblocks)
    inky.update(mazeblocks)


def check_events(ai_settings, screen, stats, sb, pacman, pacmans, blinky, pinky, inky, clyde, ghosts, mazeblocks, play_button, high_score):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, pacman, pacmans, mazeblocks, stats, high_score)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, pacman, pacmans, mazeblocks)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, pacman, blinky, pinky, inky, clyde, play_button, mouse_x, mouse_y, high_score)
            # check_high_button(ai_settings, screen, stats, sb, play_button, high_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, pacman, blinky, pinky, inky, clyde, play_button, mouse_x, mouse_y, high_score):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score(high_score)
        sb.prep_level()
        sb.prep_pacmans()

        # Create pacman and aliens.
        pacman.center_pacman()
        blinky.center_blinky()
        pinky.center_pinky()
        clyde.center_clyde()
        inky.center_inky()




def check_keydown_events(event, ai_settings, screen, pacman, pacmans, mazeblocks, stats, high_score):
    """Respond to key presses."""
    if event.key == pygame.K_RIGHT:
        pacman.moving_right = False
        pacman.moving_left = False
        pacman.moving_up = False
        pacman.moving_down = False

        collisions = pygame.sprite.groupcollide(pacmans, mazeblocks, False, False)
        if collisions:
            for mazeblocks in collisions.values():
                for pacman in pacmans:
                    for mazeblock in mazeblocks:
                        if pacman.rect.colliderect(mazeblock) == True:
                            pacman.moving_right = False
        else:
            pacman.moving_right = True

    elif event.key == pygame.K_LEFT:
        pacman.moving_right = False
        pacman.moving_left = False
        pacman.moving_up = False
        pacman.moving_down = False

        collisions = pygame.sprite.groupcollide(pacmans, mazeblocks, False, False)
        if collisions:
            for mazeblocks in collisions.values():
                for pacman in pacmans:
                    for mazeblock in mazeblocks:
                        if pacman.rect.colliderect(mazeblock) == True:
                            pacman.moving_left = False
        else:
            pacman.moving_left = True

    elif event.key == pygame.K_UP:
        pacman.moving_right = False
        pacman.moving_left = False
        pacman.moving_up = False
        pacman.moving_down = False

        collisions = pygame.sprite.groupcollide(pacmans, mazeblocks, False, False)
        if collisions:
            for mazeblocks in collisions.values():
                for pacman in pacmans:
                    for mazeblock in mazeblocks:
                        if pacman.rect.colliderect(mazeblock) == True:
                            pacman.moving_up = False
        else:
            pacman.moving_up = True

    elif event.key == pygame.K_DOWN:
        pacman.moving_right = False
        pacman.moving_left = False
        pacman.moving_up = False
        pacman.moving_down = False

        collisions = pygame.sprite.groupcollide(pacmans, mazeblocks, False, False)
        if collisions:
            for mazeblocks in collisions.values():
                for pacman in pacmans:
                    for mazeblock in mazeblocks:
                        if pacman.rect.colliderect(mazeblock) == True:
                            pacman.moving_down = False
        else:
            pacman.moving_down = True

    elif event.key == pygame.K_SPACE:
        pacman.moving_right = False
        pacman.moving_left = False
        pacman.moving_up = False
        pacman.moving_down = False
        pacman.center_pacman()

    elif event.key == pygame.K_q:
        if stats.score > high_score:
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(stats.score))
            high_score_file.close()
        sys.exit()


def check_keyup_events(event, ai_settings, screen, pacman, pacmans, mazeblocks):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        collisions = pygame.sprite.groupcollide(pacmans, mazeblocks, False, False)
        if collisions:
            for mazeblocks in collisions.values():
                for pacman in pacmans:
                    for mazeblock in mazeblocks:
                        if pacman.rect.colliderect(mazeblock) == True:
                            pacman.moving_right = False

    elif event.key == pygame.K_LEFT:
        collisions = pygame.sprite.groupcollide(pacmans, mazeblocks, False, False)
        if collisions:
            for mazeblocks in collisions.values():
                for pacman in pacmans:
                    for mazeblock in mazeblocks:
                        if pacman.rect.colliderect(mazeblock) == True:
                            pacman.moving_left = False

    elif event.key == pygame.K_UP:

        collisions = pygame.sprite.groupcollide(pacmans, mazeblocks, False, False)
        if collisions:
            for mazeblocks in collisions.values():
                for pacman in pacmans:
                    for mazeblock in mazeblocks:
                        if pacman.rect.colliderect(mazeblock) == True:
                            pacman.moving_up = False

    elif event.key == pygame.K_DOWN:

        collisions = pygame.sprite.groupcollide(pacmans, mazeblocks, False, False)
        if collisions:
            for mazeblocks in collisions.values():
                for pacman in pacmans:
                    for mazeblock in mazeblocks:
                        if pacman.rect.colliderect(mazeblock) == True:
                            pacman.moving_down = False


def update_pellets(ai_settings, screen, stats, sb, pacman, pacmans, mazeblock, mazeblocks, mazeblock_number, pellets, powerpellets, pellets_number, ghosts, blinky, pinky, inky, clyde, high_score):
    """Update position of bullets, and get rid of old bullets."""
    # Update bullet positions.
    pellets.update()

    check_pellet_pacman_collisions(ai_settings, screen, stats, sb, pacman, pacmans, mazeblock, mazeblocks, mazeblock_number, pellets, powerpellets, pellets_number, blinky, pinky, inky, clyde)
    check_powerpellet_pacman_collisions(ai_settings, screen, stats, sb, pacman, pacmans, powerpellets, blinky, pinky, inky, clyde, ghosts)

    check_ghosts_pacman_collisions(ai_settings, screen, stats, sb, mazeblocks, pellets, pacman, pacmans, ghosts, blinky, pinky, inky, clyde, high_score, mazeblock, powerpellets, pellets_number, mazeblock_number)


def check_pellet_pacman_collisions(ai_settings, screen, stats, sb, pacman, pacmans, mazeblock, mazeblocks, mazeblock_number, pellets, powerpellets, pellets_number, blinky, pinky, inky, clyde):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(pellets, pacmans, True, False)
    if collisions:

        for pellets in collisions.values():
            for pellet in pellets:
                # pacman_sound = pygame.mixer.Sound('Pacman Waka.wav')
                # pacman_sound.play()
                stats.score += ai_settings.pellet_points * len(pellets)
            sb.prep_score()
        # check_high_score(stats, sb)"""Respond to bullet-alien collisions."""

    if len(pellets) == 0:
        # If the entire fleet is destroyed, start a new level.
        ai_settings.increase_speed()
        pellets.empty()
        powerpellets.empty()

        # Increase level.
        stats.level += 1
        sb.prep_level()

        pacman.moving_right = False
        pacman.moving_left = False
        pacman.moving_up = False
        pacman.moving_down = False
        pacman.center_pacman()
        blinky.center_blinky()
        pinky.center_pinky()
        inky.center_inky()
        clyde.center_clyde()
        pygame.mixer.music.load('Win.mp3')
        pygame.mixer.music.play(-1)
        pacman.power = 0
        sleep(5)
        pacman.blitme()
        create_powerpellets(ai_settings, screen, pacman, powerpellets)
        create_pellets(ai_settings, screen, pacman, mazeblock, mazeblocks, mazeblock_number, pellets, pellets_number)
        pygame.mixer.music.load('Pac-Man Fever.mp3')
        pygame.mixer.music.play(-1)


def check_ghosts_pacman_collisions(ai_settings, screen, stats, sb, mazeblocks, pellets, pacman, pacmans, ghosts, blinky, pinky, inky, clyde, high_score, mazeblock, powerpellets, pellets_number, mazeblock_number):
    collisions = pygame.sprite.spritecollide(pacman, ghosts, False)
    if pacman.power == 0:
        if collisions:
            death_sound = pygame.mixer.Sound('Pacman Death.wav')
            death_sound.play()
            pacman_hit(ai_settings, screen, stats, sb, mazeblock, mazeblocks, pellets, pacman, blinky, pinky, inky, clyde, high_score, powerpellets, pellets_number, mazeblock_number)
    else:
        check_eat_ghosts(pacmans, ghosts, stats)


def check_powerpellet_pacman_collisions(ai_settings, screen, stats, sb, pacman, pacmans, powerpellets, blinky, pinky, inky, clyde, ghosts):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(powerpellets, pacmans, True, False)
    if collisions:
        pacman.power = 1
        pacman.seconds = 0
        for powerpellets in collisions.values():
            for pellet in powerpellets:
                stats.score += ai_settings.powerpellet_points * len(powerpellets)
            sb.prep_score()
        # check_high_score(stats, sb)"""Respond to bullet-alien collisions."""


def check_eat_ghosts(pacmans, ghosts, stats):
    collisions = pygame.sprite.groupcollide(pacmans, ghosts, False, False)
    if collisions:
        for ghosts in collisions.values():
            for ghost in ghosts:
                ghost.rect.x
                ghost.rect.centery = 250
                ghost.rect.centerx = 300
                ghost.centerx = ghost.rect.x
                ghost.rect.centerx = ghost.rect.x
                ghost.centery = ghost.rect.y
                ghost.rect.centery = ghost.rect.y
                stats.score += 200



def turnghostsblue(blinky, pinky, inky, clyde):
    blinky.frame += 1
    if blinky.frame > 1:
        blinky.frame = 0
    blinky.image = blinky.redblue[blinky.frame]
    inky.image = blinky.redblue[blinky.frame]
    pinky.image = blinky.redblue[blinky.frame]
    clyde.image = blinky.redblue[blinky.frame]

    blinky.blitme()
    inky.blitme()
    clyde.blitme()
    pinky.blitme()


def pacman_hit(ai_settings, screen, stats, sb, mazeblock, mazeblocks, pellets, pacman, blinky, pinky, inky, clyde, high_score, powerpellets, pellets_number, mazeblock_number):
    x = 0
    death_sound = pygame.mixer.Sound('Pacman Death.wav')
    death_sound.play()
    while x < 20:
        pacman.explosion(x)
        screen.fill(ai_settings.bg_color)
        pacman.blitme()
        for mazeblock in mazeblocks.sprites():
            mazeblock.blitme()

        for pellet in pellets.sprites():
            pellet.blitme()

        # Draw the score information.
        sb.show_score()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        sleep(0.15)
        x = x + 1

    sleep(0.5)

    if stats.pacmans_left > 0:
        # Decrement ships_left.
        stats.pacmans_left -= 1

        # Update scoreboard.
        sb.prep_pacmans()
        pacman.center_pacman()
        pacman.image = pacman.pacframesl[0]
        pacman.blitme()

    else:
        if stats.score > high_score:
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(stats.score))
            high_score_file.close()
        stats.game_active = False
        pygame.mouse.set_visible(True)
        pacman.image = pacman.pacframesl[0]
        pacman.blitme()
        pellets.empty()
        powerpellets.empty()
        create_powerpellets(ai_settings, screen, pacman, powerpellets)
        create_pellets(ai_settings, screen, pacman, mazeblock, mazeblocks, mazeblock_number, pellets, pellets_number)

    blinky.center_blinky()
    blinky.moving_right = True
    blinky.moving_left = False
    blinky.moving_up = False
    blinky.moving_down = False
    blinky.blitme()

    pinky.center_pinky()
    pinky.moving_right = False
    pinky.moving_left = False
    pinky.moving_up = True
    pinky.moving_down = False
    pinky.blitme()

    clyde.center_clyde()
    clyde.moving_right = False
    clyde.moving_left = False
    clyde.moving_up = False
    clyde.moving_down = True
    clyde.blitme()

    inky.center_inky()
    inky.moving_right = False
    inky.moving_left = True
    inky.moving_up = False
    inky.moving_down = False
    inky.blitme()




def create_pellets(ai_settings, screen, pacman, mazeblock, mazeblocks, mazeblock_number, pellets, pellets_number):
    pellet = Pellet(ai_settings, screen)
    create_pellet(ai_settings, screen, pacman, pellet, mazeblocks, mazeblock_number, pellets, pellets_number)


def create_powerpellets(ai_settings, screen, pacman, powerpellets):
    powerpellet = PowerPellet(ai_settings, screen)
    create_powerpellet(ai_settings, screen, pacman, powerpellets)


def create_powerpellet(ai_settings, screen, pacman, powerpellets):
    powerpellet = PowerPellet(ai_settings, screen)
    powerpellet.x = 558
    powerpellet.rect.x = powerpellet.x
    powerpellet.y = 555
    powerpellet.rect.y = powerpellet.y
    powerpellets.add(powerpellet)

    powerpellet = PowerPellet(ai_settings, screen)
    powerpellet.x = 538
    powerpellet.rect.x = powerpellet.x
    powerpellet.y = 150
    powerpellet.rect.y = powerpellet.y
    powerpellets.add(powerpellet)

    powerpellet = PowerPellet(ai_settings, screen)
    powerpellet.x = 46
    powerpellet.rect.x = powerpellet.x
    powerpellet.y = 85
    powerpellet.rect.y = powerpellet.y
    powerpellets.add(powerpellet)

    powerpellet = PowerPellet(ai_settings, screen)
    powerpellet.x = 34
    powerpellet.rect.x = powerpellet.x
    powerpellet.y = 555
    powerpellet.rect.y = powerpellet.y
    powerpellets.add(powerpellet)


def create_pellet(ai_settings, screen, pacman, pellet, mazeblocks, mazeblock_number, pellets, pellets_number):
    i = 0
    while i < 33:
        pellet = Pellet(ai_settings, screen)
        pellet.x = (i * 16) + 36
        pellet.rect.x = pellet.x
        pellet.y = 560
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 5:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 36
        pellet.rect.x = pellet.x
        pellet.y = 560 - (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 0
    while i < 5:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 560
        pellet.rect.x = pellet.x
        pellet.y = 560 - (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 5:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 330
        pellet.rect.x = pellet.x
        pellet.y = 560 - (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 5:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 270
        pellet.rect.x = pellet.x
        pellet.y = 560 - (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 3:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 270 - (i * 16)
        pellet.rect.x = pellet.x
        pellet.y = 496
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 3:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 330 + (i * 16)
        pellet.rect.x = pellet.x
        pellet.y = 496
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 4:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 100
        pellet.rect.x = pellet.x
        pellet.y = 170 + (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 7:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 560 - (i * 16)
        pellet.rect.x = pellet.x
        pellet.y = 496
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 7:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 36 + (i * 16)
        pellet.rect.x = pellet.x
        pellet.y = 496
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 0
    while i < 4:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 380
        pellet.rect.x = pellet.x
        pellet.y = 496 - (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 0
    while i < 4:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 215
        pellet.rect.x = pellet.x
        pellet.y = 496 - (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 4:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 90
        pellet.rect.x = pellet.x
        pellet.y = 496 - (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 4:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 510
        pellet.rect.x = pellet.x
        pellet.y = 496 - (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 0
    while i < 16:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 154
        pellet.rect.x = pellet.x
        pellet.y = 496 - (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 0
    while i < 20:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 440
        pellet.rect.x = pellet.x
        pellet.y = 496 - (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 0
    while i < 7:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 36 + (i * 16)
        pellet.rect.x = pellet.x
        pellet.y = 300
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 0
    while i < 3:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 510 + (i * 16)
        pellet.rect.x = pellet.x
        pellet.y = 430
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 0
    while i < 17:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 170 + (i * 16)
        pellet.rect.x = pellet.x
        pellet.y = 432
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 4:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 42 + (i * 16)
        pellet.rect.x = pellet.x
        pellet.y = 430
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 0
    while i < 4:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 42
        pellet.rect.x = pellet.x
        pellet.y = 430 - (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 4:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 265
        pellet.rect.x = pellet.x
        pellet.y = 430 - (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 4:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 335
        pellet.rect.x = pellet.x
        pellet.y = 430 - (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 0
    while i < 4:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 560
        pellet.rect.x = pellet.x
        pellet.y = 430 - (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 0
    while i < 7:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 560 - (i * 16)
        pellet.rect.x = pellet.x
        pellet.y = 300
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 0
    while i < 6:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 540 - (i * 16)
        pellet.rect.x = pellet.x
        pellet.y = 235
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 0
    while i < 7:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 56 + (i * 16)
        pellet.rect.x = pellet.x
        pellet.y = 235
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 0
    while i < 28:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 100 + (i * 16)
        pellet.rect.x = pellet.x
        pellet.y = 165
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 0
    while i < 15:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 50 + (i * 16)
        pellet.rect.x = pellet.x
        pellet.y = 90
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 0
    while i < 10:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 375 + (i * 16)
        pellet.rect.x = pellet.x
        pellet.y = 90
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 5:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 525
        pellet.rect.x = pellet.x
        pellet.y = 90  + (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 8:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 555
        pellet.rect.x = pellet.x
        pellet.y = 120 + (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 8:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 295
        pellet.rect.x = pellet.x
        pellet.y = 74 + (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 9:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 50
        pellet.rect.x = pellet.x
        pellet.y = 90 + (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 0
    while i < 15:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 560 - (i * 16)
        pellet.rect.x = pellet.x
        pellet.y = 365
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 0
    while i < 15:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 266 - (i * 16)
        pellet.rect.x = pellet.x
        pellet.y = 365
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 17:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 218
        pellet.rect.x = pellet.x
        pellet.y = 365 - (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1

    i = 1
    while i < 17:
        pellet = Pellet(ai_settings, screen)
        pellet.x = 377
        pellet.rect.x = pellet.x
        pellet.y = 365 - (i * 16)
        pellet.rect.y = pellet.y
        pellets.add(pellet)
        pellets_number += 1
        i += 1


def create_mazeblock(ai_settings, screen, pacman, mazeblock, mazeblocks, mazeblock_number):

    i = 0
    while i < 37:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = (i * 16) + 4
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 582
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 35:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = (i * 16) + 4
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 54
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 1
    while i < 17:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 4
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 582 - (i * 16)
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 1
    while i < 15:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 4
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 278 - (i * 16)
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 1
    while i < 7:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 68
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 214 - (i * 16)
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 8:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 180 - (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 118
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 4:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 180 - (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 182
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 3:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 132 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 198
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 1
    while i < 8:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 4 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 326
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 1
    while i < 8:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 4 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 262
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 1
    while i < 8:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 580 - (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 326
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 1
    while i < 8:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 580 - (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 262
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 3:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 20 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 454
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 11:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 68 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 518
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 11:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 516 - (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 518
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 1
    while i < 17:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 580
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 582 - (i * 16)
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 1
    while i < 12:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 580
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 278 - (i * 16)
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 3:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 564 - (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 454
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 4:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 468
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 454 - (i * 16)
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 9:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 404
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 326 - (i * 16)
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 9:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 180
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 326 - (i * 16)
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 4:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 116
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 454 - (i * 16)
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 4:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 116 - (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 390
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 4:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 180 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 390
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 4:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 356 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 390
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 4:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 292
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 390 - (i * 16)
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 7:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 244 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 326
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 0:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 260 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 198
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 1:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 324 + 16
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 198
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 1:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 244 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 198
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 3:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 244
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 246 - (i * 16)
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 3:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 340
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 246 - (i * 16)
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 7:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 244 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 262
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 2:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 244 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 134
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 2:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 324 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 134
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 4:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 324
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 118 - (i * 16)
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 4:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 340
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 118 - (i * 16)
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 2:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 244 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 118
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 6:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 404 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 118
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 6:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 404 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 134
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 2:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 548 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 102
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 3:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 548
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 86 - (i * 16)
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 4:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 468 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 196
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 4:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 468 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 390
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 4:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 404
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 502 - (i * 16)
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 4:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 180
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 502 - (i * 16)
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 4:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 292
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 518 - (i * 16)
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1

    i = 0
    while i < 7:
        mazeblock = Mazeblock(ai_settings, screen)
        mazeblock.x = 244 + (i * 16)
        mazeblock.rect.x = mazeblock.x
        mazeblock.y = 454
        mazeblock.rect.y = mazeblock.y
        mazeblocks.add(mazeblock)
        mazeblock_number += 1
        i += 1


def create_mazeblocks(ai_settings, screen, pacman, mazeblock, mazeblocks, mazeblock_number):
    mazeblock = Mazeblock(ai_settings, screen)
    create_mazeblock(ai_settings, screen, pacman, mazeblock, mazeblocks, mazeblock_number)



