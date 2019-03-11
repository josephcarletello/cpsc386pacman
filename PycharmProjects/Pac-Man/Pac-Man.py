import pygame
import pygame.ftfont
from pygame.sprite import Group
from time import sleep
from settings import Settings
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from pacman import Pacman
from mazeblock import Mazeblock
from pellet import Pellet
from powerpellet import PowerPellet
from blinky import Blinky
from pinky import Pinky
from inky import Inky
from clyde import Clyde
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Pac-Man")

    # Make the Play button.
    # high_button = Button1(ai_settings, screen, "")
    play_button = Button(ai_settings, screen, "Play Now")

    high_score_file = open("high_score.txt", "r")
    high_score = int(high_score_file.read())
    high_score_file.close()

    pygame.mixer.music.load('Pac-Man Fever.mp3')
    pygame.mixer.music.play(-1)


    # Make a ship, a group of bullets, and a group of aliens.
    pacman = Pacman(ai_settings, screen)

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats, high_score)
    mazeblock = Mazeblock(ai_settings, screen)
    pellet = Pellet(ai_settings, screen)
    blinky = Blinky(ai_settings, screen)
    pinky = Pinky(ai_settings, screen)
    inky = Inky(ai_settings, screen)
    clyde = Clyde(ai_settings, screen)

    sb.high_score = high_score

    mazeblocks = Group()
    pellets = Group()
    powerpellets = Group()
    pacmans = Group()
    ghosts = Group()
    pacmans.add(pacman)
    ghosts.add(blinky)
    ghosts.add(pinky)
    ghosts.add(inky)
    ghosts.add(clyde)

    mazeblock_number = 0
    pellets_number = 0

    gf.create_mazeblocks(ai_settings, screen, pacman, mazeblock, mazeblocks, mazeblock_number)
    gf.create_pellets(ai_settings, screen, pacman, mazeblock, mazeblocks, mazeblock_number, pellets, pellets_number)
    gf.create_powerpellets(ai_settings, screen, pacman, powerpellets)

    pacman.seconds = 0
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, pacman, pacmans, blinky, pinky, inky, clyde, ghosts, mazeblocks, play_button, high_score)

        if stats.game_active:
            gf.update_positions(pacman, pacmans, mazeblocks, blinky, pinky, clyde, inky)
            gf.update_pellets(ai_settings, screen, stats, sb, pacman, pacmans, mazeblock, mazeblocks, mazeblock_number, pellets, powerpellets, pellets_number, ghosts, blinky, pinky, inky, clyde, high_score)
            if pacman.power == 1:

                gf.update_positions(pacman, pacmans, mazeblocks, blinky, pinky, clyde, inky)
                gf.turnghostsblue(blinky, pinky, inky, clyde)
                gf.update_screen(ai_settings, screen, stats, sb, pacman, play_button, mazeblock, mazeblocks,mazeblock_number, pellets, powerpellets, pellets_number, ghosts, blinky, pinky, inky,clyde)
                gf.update_pellets(ai_settings, screen, stats, sb, pacman, pacmans, mazeblock, mazeblocks, mazeblock_number, pellets, powerpellets, pellets_number, ghosts, blinky, pinky, inky, clyde, high_score)
                # gf.check_eat_ghosts(pacmans, ghosts)
                pacman.seconds += 1
                if pacman.seconds > 2283:  # if more than 10 seconds close the game
                    pacman.power = 0
                    pacman.seconds = 0

        gf.update_screen(ai_settings, screen, stats, sb, pacman, play_button, mazeblock, mazeblocks, mazeblock_number, pellets, powerpellets, pellets_number, ghosts, blinky, pinky, inky, clyde)


run_game()
