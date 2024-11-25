import sys
import pygame
from player_tank import Player_tank
from settings import Settings
from base import Base
from bullet import Bullet
from pygame.sprite import Sprite
from cannon import Turret
from enemy_tank import Enemy_tank 
from allradios import Mixaudio
import pygame.mixer
class Tank_war:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.collision2_sound = pygame.mixer.Sound(r'asset\sounds\small_explosion1.mp3')
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Tank war")
        self.bases = pygame.sprite.Group() 

        self.background_image = pygame.image.load(r"asset\image\background.jpg")

        self.player_tank = Player_tank(self)
        self.bullets = pygame.sprite.Group()
        self.enemy_tanks = pygame.sprite.Group()
        self._create_base()
        self.cannon = Turret(self,self.player_tank)
        self._create_enemy_tanks()
        self.audio = Mixaudio()



    def _create_base(self):
        base = Base(self)
        self.bases.add(base)
        
    def _create_enemy_tanks(self):
        enemy_tank = Enemy_tank(self)
        self.enemy_tanks.add(enemy_tank)


    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self._fire_bullet()


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
        elif event.key == pygame.K_i:#i键下一首
            if self.audio.bgm_num ==(len(self.audio.music_lst)-1):
                self.audio.bgm_num = 0
            else:
                self.audio.bgm_num += 1 
        elif event.key == pygame.K_o: #o键开始播放
            self.audio.bgm_key = True 
        elif event.key == pygame.K_p: #p键停止播放
            self.audio.bgm_key = False
        elif event.key == pygame.K_l:  #暂定,用l按键测试音效
            self.audio.sound_cannon_key = True
        

        

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
    
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
                if bullet.rect.bottom<=0 or bullet.rect.top>=self.settings.screen_height or bullet.rect.left<=0 or bullet.rect.right>=self.settings.screen_width:
                    self.bullets.remove(bullet)
                print(len(self.bullets))
        collisions1 = pygame.sprite.groupcollide(self.bullets,self.bases,True,False)
        collisions2 = pygame.sprite.groupcollide(self.bullets,self.enemy_tanks,True,True)
        for bullet,enemies in collisions2.items():
            self.collision2_sound.play()

    def _fire_bullet(self):
        tank_pos_x,tank_pos_y = self.player_tank.rect.center
        tank_pos = tank_pos_x,tank_pos_y
        mouse_pos_X,momouse_pos_Y = pygame.mouse.get_pos()
        mouse_pos = mouse_pos_X,momouse_pos_Y
        new_bullet = Bullet(self,mouse_pos,tank_pos)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.blit(self.background_image, [0, 0])
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() 
        self.enemy_tanks.draw(self.screen)
        self.bases.draw(self.screen)
        self.player_tank.draw1()
        self.cannon.draw(self.screen,self.player_tank)
        
        pygame.display.flip()
 #====================以上为初始化===================        


    def run_game(self):
        while True:
            self._check_events()
            self.player_tank.update()
            self.bullets.update()
            self.cannon.rotate_towards_mouse()
            self._update_bullets()
            self._update_screen()
            self.mouse()
            self.audio.music_player()
            self.audio.sound_player()
            self.clock.tick(60)
if __name__ == '__main__':
    
    tw = Tank_war()
    tw.run_game()