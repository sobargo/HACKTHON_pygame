import pygame
from pygame.sprite import Sprite
from pygame import Vector2
class Bullet(Sprite):
    def __init__(self,tw_game):
        super().__init__()
        self.image = pygame.image.load(r"asset\image\bullet.png")
        self.screen = tw_game.screen
        self.settings = tw_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        tank_pos = tw_game.player_tank.rect.center
        mouse_pos = pygame.mouse.get_pos()
        direction_vector = Vector2(mouse_pos) - Vector2(tank_pos)
        self.velocity = direction_vector.normalize() * self.settings.bullet_speed
        self.rect.center = tank_pos
        self.position = Vector2(tank_pos)
    def update(self):
        self.position+=self.velocity
        self.rect.center = self.position
        
        

    def draw_bullet(self):  
        self.screen.blit(self.image,self.rect)

