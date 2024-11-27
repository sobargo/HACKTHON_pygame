'''
子弹模块:
    此模块主要处理子弹相关内容,使用了pygame的精灵方法
'''

import pygame
from pygame.sprite import Sprite
from pygame import Vector2
import math
class Bullet(Sprite):
    def __init__(self,tw_game,mouse_pos,tank_pos):
        '''
        加载子弹图像
        设置屏幕和游戏设置
        坦克位置决定子弹出发点
        坦克和鼠标相对位置决定子弹方向
        '''
        super().__init__()
        self.original_image = pygame.image.load(r"asset\image\bullet.png")
        self.image = self.original_image.copy()   #图像
        self.screen = tw_game.screen   
        self.settings = tw_game.settings
        self.rect = self.image.get_rect(center=tank_pos) 
        self.rect.center = tw_game.player_tank.rect.center  #初始位置
        direction_vector = Vector2(mouse_pos) - Vector2(tank_pos) #方向
        self.angle = direction_vector.angle_to(Vector2(0, -1))
        self.velocity = direction_vector.normalize() * self.settings.bullet_speed
        self.position = Vector2(tank_pos)
        self.image = self.original_image
    def update(self):
        '''
        用于子弹开始移动
        '''
        self.position+=self.velocity
        self.rect.center = self.position
        self.rotate_image()
        
    def rotate_image(self):
        '''
        用于子弹旋转
        '''
        rotated_image = pygame.transform.rotate(self.original_image, self.angle)
        self.image = rotated_image
        self.rect = self.image.get_rect(center=self.rect.center)

        
        

    def draw_bullet(self):  
        '''
        绘制子弹
        '''
        self.screen.blit(self.image,self.rect.topleft)


