import sys
import pygame
import random
import time
from player_tank import Player_tank
from settings import Settings
from base import Base
from bullet import Bullet
from bullet1 import Bullet1
from cannon import Turret
from allradios import Mixaudio
from soldier_b import Soldier_b
from soldier_t import Soldier_t
from explosion import Explosion
from danyao import Danyao
from xuebao import Xuebao
from dig import Dig
import pygame.mixer
class Tank_war:
    def __init__(self):
        pygame.init()
        #物品刷新定时
        self.RANDOM1 = pygame.USEREVENT
        pygame.time.set_timer(self.RANDOM1, 1000)
        # 设置发射频率（每秒发射的子弹数）
        self.fire_rate = 10
        self.fire_interval = 1000 // self.fire_rate

        # 设置鼠标左键按下的计时器
        self.left_mouse_pressed = False
        self.press_start_time = 0

        self.flag_1 = 0
        
        pygame.mixer.init()
<<<<<<< HEAD
 
        pygame.time.set_timer(pygame.USEREVENT, 1500)#刷怪频率1000ms
=======
        pygame.time.set_timer(pygame.USEREVENT, 2000)#定时器，每2000ms触发一次
<<<<<<< HEAD
>>>>>>> parent of 464526b (奥数魔刃更新)
=======
>>>>>>> parent of 464526b (奥数魔刃更新)
        self.collision2_sound = pygame.mixer.Sound(r'asset\sounds\small_explosion1.mp3')
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Tank war") # 设置窗口标题
        self.bases = pygame.sprite.Group() 

        self.background_image = pygame.image.load(r"asset\image\background.png")

        self.player_tank = Player_tank(self)
        self.bullets = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.digs = pygame.sprite.Group()
        self.bullets1 = pygame.sprite.Group()
        self.enemy_tanks = pygame.sprite.Group()
        self.danyaos = pygame.sprite.Group()
        self.xuebaos = pygame.sprite.Group()
        self._create_base()
        self.cannon = Turret(self,self.player_tank)
        self.audio = Mixaudio()
        self.soldier_bs = pygame.sprite.Group() # 自爆小车
        self.soldier_ts = pygame.sprite.Group() # 自爆步兵
        self.score = 0 #设置初始分数
        # 设置最大子弹数量
        self.remaining_bullets = 150 # 普通子弹
        self.remaining_bullets1 = 10 # 特殊子弹

    def _create_base(self):
        self.base = Base(self)
        self.bases.add(self.base)
    

        
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT: # 退出游戏
                    sys.exit()
                elif event.type == pygame.KEYDOWN: # 按键按下事件
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event) # 按键释放事件
                elif event.type == pygame.MOUSEBUTTONDOWN: # 鼠标按下事件
                    if event.button == 1:  # 鼠标左键
                        self._fire_bullet() # 发射普通子弹
                        
                        self.left_mouse_pressed = True
                        self.press_start_time = pygame.time.get_ticks()  # 记录按下时间
                    if event.button == 3: # 鼠标右键
                        self._fire_bullet1()  # 发射特殊子弹
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:  # 鼠标左键
                        self.audio.sound_machinegun_key = False
                        self.left_mouse_pressed = False 
                if event.type == pygame.USEREVENT: # 定时器事件
                    self._make_soldier_b()
                    self._make_soldier_t()
                if self.left_mouse_pressed:
                    current_time = pygame.time.get_ticks()
                    if current_time - self.press_start_time > 0.5:  # 如果持续按下超过500毫秒
                        if (current_time % self.fire_interval) < 15:
                            self._fire_bullet()  # 以fire_interval为周期发射子弹
                if event.type == self.RANDOM1: #随机生成道具
                    a = random.randint(1,2)
                    if a == 1:
                        self.spawn_sprite1() # 生成弹药
                    if a == 2:
                        self.spawn_sprite2() # 生成血包


                            
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
        
    def spawn_sprite1(self):
        # 随机位置
        x = random.randint(30, 1890)
        y = random.randint(30, 1050)
        self_pos =(x,y)
        new_sprite = Danyao(self,self_pos)
        self.danyaos.add(new_sprite)
        
        pygame.display.flip()


    def spawn_sprite2(self):
        # 随机位置
        x = random.randint(30, 1890)
        y = random.randint(30, 1050)
        self_pos =(x,y)
        new_sprite = Xuebao(self,self_pos)
        self.xuebaos.add(new_sprite)
        
        pygame.display.flip()
   
        

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
            # self.collision2_sound.play()
            self.score += 1  # 击中敌人时增加分数
            self.remaining_bullets+=1
            
            
        collisions2 = pygame.sprite.groupcollide(self.bullets,self.soldier_bs,True,True)
        for bullet,enemies in collisions2.items():
            self.collision2_sound.play()
            self.score += 1  # 击中敌人时增加分数
            self.remaining_bullets+=2
            x,y = bullet.rect.centerx,bullet.rect.centery
            explosion = Explosion(self,x,y)
            self.explosions.add(explosion)
            collision10 = pygame.sprite.groupcollide(self.explosions,self.soldier_bs,False,True)
            collision11 = pygame.sprite.groupcollide(self.explosions,self.soldier_ts,False,True)
            
            dig = Dig(self, x, y)
            self.digs.add(dig)
    def _update_explosion(self):
         
         self.explosions.update()
    def _update_digs(self):
        self.digs.update()
    
    def _update_bullets1(self):
        self.bullets1.update()
        
        for bullet in self.bullets1.copy():
                if bullet.rect.bottom<=0 or bullet.rect.top>=self.settings.screen_height or bullet.rect.left<=0 or bullet.rect.right>=self.settings.screen_width:
                    self.bullets1.remove(bullet)
        # collisions1 = pygame.sprite.groupcollide(self.bullets1,self.soldier_ts,True,True)
        # for bullet,enemies in collisions1.items():
        #     self.collision2_sound.play()


        #     self.score += 1  # 击中敌人时增加分数
        #     self.remaining_bullets1+=2
        #     x, y = bullet.rect.centerx, bullet.rect.centery
        #     dig = Explosion(self, x, y)
        #     self.digs.add(dig)
        # collisions2 = pygame.sprite.groupcollide(self.bullets1,self.soldier_bs,True,True)
        # for bullet,enemies in collisions2.items():
        #     self.collision2_sound.play()
        #     self.score += 1  # 击中敌人时增加分数
        #     self.remaining_bullets+=2
        #     x, y = bullet.rect.centerx, bullet.rect.centery
        #     dig = Explosion(self, x, y)
        #     self.digs.add(dig)   

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
            
        
    def _fire_bullet1(self):
        self.audio.sound_cannon_key = True
        # 检查当前子弹数量是否超过限制
        if self.remaining_bullets1 >0:
            tank_pos_x,tank_pos_y = self.player_tank.rect.center
            tank_pos = tank_pos_x,tank_pos_y
            mouse_pos_X,momouse_pos_Y = pygame.mouse.get_pos()
            mouse_pos = mouse_pos_X,momouse_pos_Y
            new_bullet1 = Bullet1(self,mouse_pos,tank_pos)
            self.bullets.add(new_bullet1)
            self.remaining_bullets1 -=1 #子弹数减1
    

    def _update_spawn_sprite(self):
        self.danyaos.update()
        self.xuebaos.update()
        
        for bullet in self.xuebaos.copy():
                
                #判断碰撞 
            if pygame.sprite.collide_rect(bullet, self.player_tank):
                self.player_tank.hp += 1
                    
                self.xuebaos.remove(bullet)
        for bullet in self.danyaos.copy():
            if pygame.sprite.collide_rect(bullet,self.player_tank):
                self.remaining_bullets+=10
                self.remaining_bullets1+=1
                self.danyaos.remove(bullet)

        

    def _update_soldier_b(self):
        self.soldier_bs.update()
        for bullet in self.soldier_bs.copy():
                if bullet.rect.bottom<=0 or bullet.rect.top>=self.settings.screen_height or bullet.rect.left<=0 or bullet.rect.right>=self.settings.screen_width:
                    self.soldier_bs.remove(bullet)
                
                #判断碰撞 
                if pygame.sprite.collide_rect(bullet, self.player_tank):
                    self.player_tank.hp -= 1
                    self.audio.sound_smallExplosion1_key = True
                    self.soldier_bs.remove(bullet)
        
        
                    
    def _update_soldier_t(self):
        tank_pos_x,tank_pos_y = self.player_tank.rect.center
        tank_pos = tank_pos_x,tank_pos_y 
        self.soldier_ts.update(tank_pos)
        for bullet in self.soldier_ts.copy():
                if bullet.rect.bottom<=0 or bullet.rect.top>=self.settings.screen_height or bullet.rect.left<=0 or bullet.rect.right>=self.settings.screen_width:
                    self.soldier_ts.remove(bullet)
                if pygame.sprite.collide_rect(bullet, self.player_tank):
                    self.player_tank.hp -= 1
                    self.audio.sound_smallExplosion1_key = True
                    self.soldier_ts.remove(bullet)
        
                
        


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
    
    #坦克碰撞后调用(废弃)
    # def _tank_hit(self):
    #     self.audio.sound_smallExplosion1_key = True
    #     for bullet in self.soldier_ts.copy():
    #         self.soldier_ts.remove

    def _draw_score(self):
        font1 = pygame.font.SysFont("arial", 30)  # 创建字体对象
        score_text1 = font1.render(f"Score: {self.score}", True, (255, 0, 0)) 
        self.screen.blit(score_text1, (200,100 ))  # 将分数显示在屏幕的左上角

        # 显示剩余子弹数量
        bullets_text = font1.render(f"Bullets1: {self.remaining_bullets}/150", True, (0, 255, 0))
        self.screen.blit(bullets_text, (200, 125))  # 将剩余子弹显示在屏幕上
        #tank hp
        tank_hp_text = font1.render(f"Tank Hp: {self.player_tank.hp}", True, (0, 255, 255))
        self.screen.blit(tank_hp_text, (200, 75))

        base_hp_text = font1.render(f"Base Hp: {self.base.hp}", True, (255, 255,0))
        self.screen.blit(base_hp_text, (200, 175))

        bullets2_text = font1.render(f"Bullets2: {self.remaining_bullets1}/10", True, (0, 255, 0))
        self.screen.blit(bullets2_text, (200, 150))  # 将剩余子弹显示在屏幕上


    def _update_screen(self):
        
        self.screen.blit(self.background_image, [0, 0])
        self.bases.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() 
        for bullet in self.bullets1.sprites():
            bullet.draw_bullet()
        for soldier in self.soldier_bs.sprites():
            soldier.draw_soldier()
        for soldier in self.soldier_ts.sprites():
            soldier.draw_soldier()
        for explosion in self.explosions.sprites():
            explosion.draw_explosion()
        for danyao in self.danyaos.sprites():
            danyao.draw_danyao()
        for xuebao in self.xuebaos.sprites():
            xuebao.draw_xuebao()
        for dig in self.digs.sprites():
            dig.draw_dig()
        
        
        self.enemy_tanks.draw(self.screen)
        self.player_tank.draw1()
        self.cannon.draw(self.screen,self.player_tank)
        self._draw_score()
        pygame.display.flip()
    
 #====================以上为初始化===================        


    def run_game(self):
<<<<<<< HEAD
<<<<<<< HEAD
        
        self.audio.bgm_num = 0
        self.audio.bgm_key = True
        while True: 
=======
=======
>>>>>>> parent of 464526b (奥数魔刃更新)
        while True:
>>>>>>> parent of 464526b (奥数魔刃更新)
            self._check_events()
            self.player_tank.update()
            self.bullets.update()
            self.bullets1.update()
            self.cannon.rotate_towards_mouse()
            self._update_bullets()
            self._update_spawn_sprite()
            self._update_soldier_b()
            self._update_soldier_t()
            self._update_explosion()
            self._update_digs()
            self._update_spawn_sprite()
            self._update_screen()
            
            
            self.mouse()
            collisions3 = pygame.sprite.groupcollide(self.bases,self.soldier_ts,False,True)
            for bullet,enemies in collisions3.items():
                self.collision2_sound.play()
                self.score-=10
                self.base.hp -= 1
                
            collisions4 = pygame.sprite.groupcollide(self.bases,self.soldier_bs,False,True)
            for bullet,enemies in collisions4.items():
                self.collision2_sound.play()
                self.score-=10
                self.base.hp -= 1
                
            #碰撞检测
            self.audio.music_player()
            self.audio.sound_player()
            self.clock.tick(60)
            self._draw_score()
            if self.player_tank.hp <= 0 or self.base.hp <= 0:
                self.audio.bgm_key = False
                self.audio.music_player()           
                break
    def game_start(self):
        self.audio.bgm_num = 3
        self.audio.bgm_key = True
        running = True
        while running:
            self.audio.music_player()
            self.start_image = pygame.image.load(r"asset\image\30.png")
            self.screen.blit(self.start_image, [0, 0])
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
        
        


    def game_over(self):
        self.audio.bgm_num = 1
        self.audio.bgm_key = True
        while True:
            self.audio.music_player()
            self.background_image = pygame.image.load(r"asset\image\map_Obstacles_png\over2.jpg")
            self.game_over1_image = pygame.image.load(r"asset\image\map_Obstacles_png\game_over.png")
            # 获取窗口尺寸
            screen_width, screen_height = self.screen.get_size()
            # 获取图像尺寸
            image_width, image_height = self.game_over1_image.get_size()
            # 计算图像的中心位置
            center_x = (screen_width - image_width) // 2
            center_y = (screen_height - image_height) // 2
            #
            font1 = pygame.font.SysFont("arial", 50)
            over_text1 = font1.render(f"Any  Key  To  Exit", True, (0, 0, 0))
            over_text2 = font1.render(f"YOUR SCORE IS {self.score}", True, (0, 0, 0)) 
            
            #
            self.screen.blit(self.background_image, [0, 0])
            self.screen.blit(self.game_over1_image, (center_x,center_y+200))
            self.screen.blit(over_text2,(800,100))
            self.screen.blit(over_text1, (800,900))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    sys.exit()
            
if __name__ == '__main__':
    
    tw = Tank_war()
    tw.game_start()
    tw.run_game()
    tw.game_over()