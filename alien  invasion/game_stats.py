class Gamestats():
    """track statistics for alien invasion."""

    def __init__(self,ai_settings):
        """initialize statics for alien ivasion."""
        self.ai_settings = ai_settings
        self.reset_stats()
        #start alien invasion in an inacive state.
        self.game_active = False
        # high score should never be reset.
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """initialize statistics."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0