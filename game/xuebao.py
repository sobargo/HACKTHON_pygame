import pygame
from pygame.sprite import Sprite
class Xuebao(Sprite):
    def __init__(self,tw_game,self_pos):
        super().__init__()
        self.original_image = pygame.image.load(r"asset\image\map_Obstacles_png\xuebao.png")
        self.image = self.original_image.copy()
        self.screen = tw_game.screen
        self.settings = tw_game.settings
        self.rect = self.image.get_rect(center=self_pos)

    def draw_xuebao(self):  
        self.screen.blit(self.image,self.rect.topleft)