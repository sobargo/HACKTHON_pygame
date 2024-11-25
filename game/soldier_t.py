import pygame
from pygame.sprite import Sprite
from pygame import Vector2
import math
class Soldier(Sprite):
    def __init__(self,tw_game,tank_pos,self_pos):
        super().__init__()
        self.original_image = pygame.image.load(r"asset\image\map_Obstacles_png\soldier_r.png")
        self.image = self.original_image.copy()
        self.screen = tw_game.screen
        self.settings = tw_game.settings
        self.rect = self.image.get_rect(center=tank_pos)
        self.rect.center = tw_game.player_tank.rect.center
        direction_vector = Vector2(tank_pos) - Vector2(self_pos)
        self.angle = direction_vector.angle_to(Vector2(0, -1))
        self.velocity = direction_vector.normalize() * self.settings.soldier_speed
        self.position = Vector2(tank_pos)
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
