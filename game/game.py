import sys
import pygame
from player_tank import Player_tank
from settings import Settings
import base
class Tank_war:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Tank war")

        self.background_image = pygame.image.load(r"asset\image\background.jpg")

        self.player_tank = Player_tank(self)
        


    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)


    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.player_tank.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player_tank.moving_left = True
        elif event.key == pygame.K_UP:
            self.player_tank.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.player_tank.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def mouse(self) -> None:
            mouse_image = pygame.image.load("asset\image\map_Obstacles_png\mouse.png")
            x,y = pygame.mouse.get_pos()
            #鼠标位置
            x -=mouse_image.get_width()/2
            y -=mouse_image.get_height()/2
            #tu pian wei zhi
            self.screen.blit(mouse_image,(x,y))
            pygame.display.flip()


    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.player_tank.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player_tank.moving_left = False
        elif event.key == pygame.K_UP:
            self.player_tank.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.player_tank.moving_down = False

    

    def _update_screen(self):
        self.screen.blit(self.background_image, [0, 0])
        self.player_tank.blitme()

        pygame.display.flip()
 #====================以上为初始化===================        


    def run_game(self):
        while True:
            self._check_events()
            self.player_tank.update()
            self._update_screen()
            self.mouse()

            self.clock.tick(60)
if __name__ == '__main__':
    
    tw = Tank_war()
    tw.run_game()