import pygame
import math
from settings import Settings
class Player_tank:
    #=====车身四种变换=====
    #body_up = pygame.image.load(r"asset\image\map_Obstacles_png\tank1_body_u.png")
    #body_right = pygame.image.load(r"asset\image\map_Obstacles_png\tank1_body_r.png")
    #body_down = pygame.image.load(r"asset\image\map_Obstacles_png\tank1_body_d.png")
    #body_left = pygame.image.load(r"asset\image\map_Obstacles_png\tank1_body_l.png")
    #===================
    def __init__(self,tw_game):
        self.screen = tw_game.screen
        self.settings = tw_game.settings
        self.screen_rect = tw_game.screen.get_rect()


        self.image = pygame.image.load(r"asset\image\map_Obstacles_png\tank1_body_r.png")
        #默认车身向上
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.angle = 0  # 初始旋转角度为0



    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.angle += 0.1
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
        if self.moving_left and self.rect.left>0:
            self.angle -= 0.1
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.rect.x -= 1.5 * math.cos(math.radians(self.angle))
            self.rect.y += 1.5 * math.sin(math.radians(self.angle))
        if self.moving_up and self.rect.top>0:
            self.rect.x += 1.5 * math.cos(math.radians(self.angle))
            self.rect.y -= 1.5 * math.sin(math.radians(self.angle))
        # self.rect.x = self.x
        # self.rect.y = self.y
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    

