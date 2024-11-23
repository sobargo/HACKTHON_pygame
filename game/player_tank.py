import pygame
class Player_tank:
    def __init__(self,tw_game):
        self.screen = tw_game.screen
        self.settings = tw_game.settings
        self.screen_rect = tw_game.screen.get_rect()

        self.image = pygame.image.load()
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False




    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.player_tank_speed
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.player_tank_speed
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.y+=self.settings.player_tank_speed
        if self.moving_up and self.rect.top>0:
            self.y-=self.settings.player_tank_speed
        self.rect.x = self.x
        self.rect.y = self.y
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    

