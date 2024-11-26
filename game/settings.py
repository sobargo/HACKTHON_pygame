'''
基础设定:
    储存基础设定
'''
import pygame
class Settings:
    def __init__(self):
        self.player_tank_speed = 1.5 #坦克速度
        self.screen_width = 1920 #屏幕大小
        self.screen_height = 1080 
        self.bullet_speed = 2.0 #子弹速度
        self.bullets_allowed = 3 
        self.bullet_width = 5 
        self.bullet_height =5
        self.bullet_color = (60,60,60)
        self.soldier_speed = 1.0  #敌人速度,此项过高会导致游戏困难
        self.soldier_t_speed = 1.0
