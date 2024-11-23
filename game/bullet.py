import pygame
from pygame.sprite import  Sprite
class Bullet(Sprite):
    def __init__(self,tw_game):
        super().__init__()
        self.screen = tw_game.screen
        self.settings = tw_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.center = tw_game.player_tank.rect.center
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
    def update(self):
        self.y-=self.settings.bullet_speed
        self.rect.y = self.y
        self.x-=self.settings.bullet_speed.


    def draw_bullet(self):  
        pygame.draw.rect(self.screen,self.color,self.rect)

