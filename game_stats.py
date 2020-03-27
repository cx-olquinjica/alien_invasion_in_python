# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 00:31:56 2020

@author: _$aturn0_
"""
class GameStats():
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_settings):
        """Initialize statistics."""
        
        # High score shoulfd never be reset.
        self.high_score = 0
        
        self.ai_settings = ai_settings
        self.reset_stats()
      # Start Alien Invasion in an inactive state.
        self.game_active = False
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        

