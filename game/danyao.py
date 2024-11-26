import pygame
from pygame.sprite import Sprite
class Danyao(Sprite):
    def __init__(self,tw_game,self_pos):
        super().__init__()
        self.original_image = pygame.image.load(r"asset\image\map_Obstacles_png\danyao.png")
        self.image = self.original_image.copy()
        self.screen = tw_game.screen
        self.settings = tw_game.settings
        self.rect = self.image.get_rect(center=self_pos)
        self.lifespan = 500
        self.age = 0
    def draw_danyao(self):  
        self.screen.blit(self.image,self.rect.topleft)

    def update(self):
        self.age += 0.5
        if self.age >= self.lifespan:
            self.kill()