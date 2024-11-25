import pygame
from pygame.sprite import Sprite
from pygame import Vector2
import math
class Soldier_t(Sprite):
    def __init__(self,tw_game,tank_pos,self_pos):
        super().__init__()
        self.original_image = pygame.image.load(r"asset\image\map_Obstacles_png\soldier_b.png")
        self.image = self.original_image.copy()
        self.screen = tw_game.screen
        self.settings = tw_game.settings
        self.rect = self.image.get_rect(center=self_pos)
        
        self.position = Vector2(self_pos)
        self.tank_pos = Vector2(tank_pos)
        self.rect.center = self.position
        self.image = self.original_image
    def update(self,tank_pos):
        self.tank_pos = Vector2(tank_pos)
        direction_vector = self.tank_pos - self.position
        self.angle = direction_vector.angle_to(Vector2(0, -1))
        self.velocity = direction_vector.normalize() * self.settings.soldier_t_speed
        self.rotate_image()
        self.position+=self.velocity
        self.rect.center = self.position
        
        
    def rotate_image(self):
        rotated_image = pygame.transform.rotate(self.original_image, self.angle)
        self.image = rotated_image
        self.rect = self.image.get_rect(center=self.rect.center)

        
        

    def draw_soldier(self):  
        self.screen.blit(self.image,self.rect.topleft)
