class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        # Pacman settings.
        self.pacman_limit = 3

        # Portal settings
        self.portals_allowed = 3

        # How quickly the game speeds up.
        self.speedup_scale = 1.3
        # How quickly the alien point values increase.
        self.score_scale = 1.25

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.pacman_speed_factor = 0.30
        self.portal_speed_factor = 3
        self.ghost_speed_factor = 0.15

        # Scoring.
        self.pellet_points = 10
        self.powerpellet_points = 50

    def increase_speed(self):
        """Increase speed settings and ghost point values."""
        self.pacman_speed_factor *= self.speedup_scale
        self.portal_speed_factor *= self.speedup_scale
        self.ghost_speed_factor *= self.speedup_scale

        self.pellet_points = int(self.pellet_points * self.score_scale)
        self.powerpellet_points = int(self.powerpellet_points * self.score_scale)
