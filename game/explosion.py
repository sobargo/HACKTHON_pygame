
import pygame
class Explosion(pygame.sprite.Sprite):
    def __init__(self,tw_game, x, y):
        super().__init__()
        # 假设你有一个表示爆炸的图像序列
        self.images = pygame.image.load(r"asset\image\map_Obstacles_png\61f68263a5a6436d92a78db398899e9f.png")  
        self.image = self.images
        self.screen = tw_game.screen
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width  # // 2  # 居中显示
        self.rect.y = y - self.rect.height # // 2
        #self.frame = 0
        #self.max_frame = len(self.images) - 1
        self.lifespan = 100  # 特效持续时间（帧数）
        self.age = 0
 
    def update(self):
        self.age += 5
        if self.age <= self.lifespan:
            #self.image = self.images[self.frame]
            #self.frame = (self.frame + 1) % (self.max_frame + 1)  # 循环播放动画
            pass
        else:
            self.kill()  # 特效结束，删除精灵
    def draw_explosion(self):
        self.screen.blit(self.image,self.rect.center)