import pygame
import math


class Turret:
    def __init__(self,tw_game,tank_body):
        self.screen = tw_game.screen
        self.settings = tw_game.settings
        self.screen_rect = tw_game.screen.get_rect()
        self.image = pygame.image.load(r'asset\image\map_Obstacles_png\cannon.png')
        self.rect = self.image.get_rect()
        self.rect.center = tank_body.rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.angle = 0  # 炮塔的旋转角度

    def rotate_towards_mouse(self):
        mouse_x,mouse_y = pygame.mouse.get_pos()
        # 计算鼠标位置与炮塔中心的角度差
        delta_x = mouse_x - self.rect.centerx
        delta_y = mouse_y - self.rect.centery
        self.angle = (math.atan2(delta_y, delta_x) * 180 / math.pi - 90)*(-1)

    def draw(self, surface,tank_body):
        self.rect.center = tank_body.rect.center
        # 旋转炮塔图像
        self.image = pygame.image.load(r'asset\image\map_Obstacles_png\cannon.png')
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        # 获取旋转后的图像的矩形，以炮塔中心为旋转点
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        # 绘制旋转后的图像
        surface.blit(rotated_image, rotated_rect.topleft)