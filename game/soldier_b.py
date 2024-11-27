'''
自爆卡车'我叫磁力棒'
    
'''
import pygame
from pygame.sprite import Sprite
from pygame import Vector2
import math
class Soldier_b(Sprite):
    def __init__(self,tw_game,base_pos,self_pos):
        super().__init__()
        self.original_image = pygame.image.load(r"asset\image\map_Obstacles_png\soldier_b.png")
        self.image = self.original_image.copy()
        self.screen = tw_game.screen
        self.settings = tw_game.settings
        self.rect = self.image.get_rect(center=self_pos)#从屏幕边缘出现
        self.rect.center = tw_game.player_tank.rect.center
        direction_vector = Vector2(base_pos) - Vector2(self_pos)#指向中心
        self.angle = direction_vector.angle_to(Vector2(0, -1))
        self.velocity = direction_vector.normalize() * self.settings.bullet_speed
        self.position = Vector2(self_pos)
        self.image = self.original_image
    def update(self):
        
        self.position+=self.velocity
        self.rect.center = self.position
        self.rotate_image()
        
    def rotate_image(self):

        rotated_image = pygame.transform.rotate(self.original_image, self.angle)
        self.image = rotated_image
        self.rect = self.image.get_rect(center=self.rect.center)

        
        

    def draw_soldier(self):  
        self.screen.blit(self.image,self.rect.topleft)
