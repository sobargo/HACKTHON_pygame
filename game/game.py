import sys
import pygame
import random
from player_tank import Player_tank
from settings import Settings
from base import Base
from bullet import Bullet

from cannon import Turret
from allradios import Mixaudio
from soldier_b import Soldier_b
from soldier_t import Soldier_t
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
        self.audio = Mixaudio()
        self.soldier_bs = pygame.sprite.Group()
        self.soldier_ts = pygame.sprite.Group()
        self.score = 0 #设置初始分数
        # 设置最大子弹数量
        self.remaining_bullets = 1000



    def _create_base(self):
        base = Base(self)
        self.bases.add(base)
        
    


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
        elif event.key == pygame.K_SPACE:
            self._make_soldier_b()
            self._make_soldier_t()
        

        

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
        collisions1 = pygame.sprite.groupcollide(self.bullets,self.soldier_ts,True,True)
        for bullet,enemies in collisions1.items():
            self.collision2_sound.play()
            self.score += 1  # 击中敌人时增加分数
                
        collisions2 = pygame.sprite.groupcollide(self.bullets,self.soldier_bs,True,True)
        for bullet,enemies in collisions2.items():
            self.collision2_sound.play()
            self.score += 1  # 击中敌人时增加分数

    def _fire_bullet(self):
        # 检查当前子弹数量是否超过限制
        if self.remaining_bullets >0:
            tank_pos_x,tank_pos_y = self.player_tank.rect.center
            tank_pos = tank_pos_x,tank_pos_y
            mouse_pos_X,momouse_pos_Y = pygame.mouse.get_pos()
            mouse_pos = mouse_pos_X,momouse_pos_Y
            new_bullet = Bullet(self,mouse_pos,tank_pos)
            self.bullets.add(new_bullet)
            self.remaining_bullets -=1 #子弹数减1

    def _update_soldier_b(self):
        self.soldier_bs.update()
        for bullet in self.soldier_bs.copy():
                if bullet.rect.bottom<=0 or bullet.rect.top>=self.settings.screen_height or bullet.rect.left<=0 or bullet.rect.right>=self.settings.screen_width:
                    self.soldier_bs.remove(bullet)
                print(len(self.soldier_bs))
    def _update_soldier_t(self):
        tank_pos_x,tank_pos_y = self.player_tank.rect.center
        tank_pos = tank_pos_x,tank_pos_y 
        self.soldier_ts.update(tank_pos)
        for bullet in self.soldier_ts.copy():
                if bullet.rect.bottom<=0 or bullet.rect.top>=self.settings.screen_height or bullet.rect.left<=0 or bullet.rect.right>=self.settings.screen_width:
                    self.soldier_ts.remove(bullet)
                print(len(self.soldier_ts))
        if pygame.sprite.spritecollideany(self.player_tank,self.soldier_ts):
            self._tank_hit()
        

    def _make_soldier_b(self):
        type1 = random.randint(1,4)
        if type1 == 1:
            x1 = random.randint(20,1910)
            self_pos = x1,20
        elif type1 == 2:
            y1 = random.randint(20,1060)
            self_pos = 1900,y1
        elif type1 == 3:
            x1 = random.randint(20,1900)
            self_pos = x1,1060
        elif type1 == 4:
            y1 = random.randint(20,1060)
            self_pos = 20,y1
        new_soldier1 = Soldier_b(self,(960,540),self_pos)
        self.soldier_bs.add(new_soldier1)
    def _make_soldier_t(self):
        type1 = random.randint(1,4)
        if type1 == 1:
            x1 = random.randint(20,1910)
            self_pos = x1,20
        elif type1 == 2:
            y1 = random.randint(20,1060)
            self_pos = 1900,y1
        elif type1 == 3:
            x1 = random.randint(20,1900)
            self_pos = x1,1060
        elif type1 == 4:
            y1 = random.randint(20,1060)
            self_pos = 20,y1
        tank_pos_x,tank_pos_y = self.player_tank.rect.center
        tank_pos = tank_pos_x,tank_pos_y
        new_soldier1 = Soldier_t(self,tank_pos,self_pos)
        self.soldier_ts.add(new_soldier1)
    

    def _tank_hit(self):
        pass

    def _draw_score(self):
        font1 = pygame.font.SysFont("arial", 30)  # 创建字体对象
        score_text1 = font1.render(f"Score: {self.score}", True, (255, 0, 0)) 
        self.screen.blit(score_text1, (200,100 ))  # 将分数显示在屏幕的左上角

        # 显示剩余子弹数量
        bullets_text = font1.render(f"Bullets: {self.remaining_bullets}", True, (0, 255, 0))
        self.screen.blit(bullets_text, (200, 150))  # 将剩余子弹显示在屏幕上
    
    def _update_screen(self):
        self.screen.blit(self.background_image, [0, 0])
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() 
        for soldier in self.soldier_bs.sprites():
            soldier.draw_soldier()
        for soldier in self.soldier_ts.sprites():
            soldier.draw_soldier()
        self.enemy_tanks.draw(self.screen)
        self.bases.draw(self.screen)
        self.player_tank.draw1()
        self.cannon.draw(self.screen,self.player_tank)
        self._draw_score()

        
        
        pygame.display.flip()
 #====================以上为初始化===================        


    def run_game(self):
        while True:
            self._check_events()
            self.player_tank.update()
            self.bullets.update()
            self.cannon.rotate_towards_mouse()
            self._update_bullets()
            self._update_soldier_b()
            self._update_soldier_t()
            self._update_screen()
            self.mouse()
            self.audio.music_player()
            self.audio.sound_player()
            self.clock.tick(60)
            self._draw_score()
if __name__ == '__main__':
    
    tw = Tank_war()
    tw.run_game()