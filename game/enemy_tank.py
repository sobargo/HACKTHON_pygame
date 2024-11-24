import pygame
from pygame.sprite import Sprite
class Enemy_tank(Sprite):
    def __init__(self,tw_game):
        super().__init__()
        self.screen = tw_game.screen
        self.image = pygame.image.load(r'asset\image\map_Obstacles_png\0253cdb426ca4aa69e69a82f5fffab51.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)