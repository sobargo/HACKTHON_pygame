import pygame
from pygame.sprite import  Sprite
class Bullet(Sprite):
    def __init__(self,tw_game):
        super().__init__()
        self.screen = tw_game.screen
        self.settings = tw_game.settings
        
