import pygame
from settings import Settings
class Base:
    def __init__(self,tw_game):
        self.screen = tw_game.screen
        self.settings = tw_game.settings
        self.screen_rect = tw_game.screen.get_rect()


        self.image = pygame.image.load(r"asset\image\map_Obstacles_png\temp_base.png")
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    