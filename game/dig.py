import pygame
class Dig(pygame.sprite.Sprite):
    def __init__(self,tw_game, x, y):
        super().__init__()
        self.screen = tw_game.screen
        self.game = tw_game
        self.image = pygame.image.load(r'asset\image\map_Obstacles_png\dig.png').convert_alpha()  # 使用透明背景的爆炸图片
        self.image = pygame.transform.scale(self.image, (72, 72))  # 调整大小，根据需要调整
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.lifespan = 500  # 弹坑显示的帧数（或时间，如果与帧率关联）
        self.age = 0
 
    def update(self):
        self.age += 1
        if self.age >= self.lifespan:
            self.kill()
    def draw_dig(self):
        self.screen.blit(self.image,self.rect.center)