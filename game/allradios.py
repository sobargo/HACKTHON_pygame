'''
音频模块:
    此模块主要使用了pygame的mixer方法,调用Mixaudio类可以实现对音频的控制
'''
import pygame
class  Mixaudio:
    def  __init__(self) -> None:
        self.music1 = r'asset\sounds\bgm3.mp3'
        self.music2 = r'asset\music\BLUE DRAGON_小林.mp3'
        self.music3 = r'asset\sounds\bgm2.mp3'
        
        self.sound1 = r'asset\sounds\cannon1.mp3'
        self.sound2 = r'asset\sounds\powerup10.mp3'
        self.sound3 = r'asset\sounds\small_explosion1.mp3'
        self.sound4 = r"asset\sounds\machingun.wav"      
        self.sound5 = r'asset\sounds\敌人寄.wav'
        self.sound6 = r'asset\sounds\发射.wav'
        self.sound7 = r'asset\sounds\发射2.wav'
        self.sound8 = r'asset\sounds\捡起道具.wav'
        self.sound9 = r'asset/sounds/警报,开场.wav'
        self.sound10= r'asset\sounds\受击.wav'
        self.sound11= r'asset\sounds\运动.wav'

        
        #导入音乐音效
        #这里sound1代表cannon1,sound2代表powerup,sound3代表small_explosion1

        pygame.mixer.init()
        pygame.mixer.music.load(self.music1)
        #初始化音乐   
        
        self.music_lst = [self.music1,self.music2,self.music3]
        self.bgm_key = True
        self.bgm_num = 0
        self.bgm_num_temp = self.bgm_num
        #初始化音乐控制

        self.sound1 = pygame.mixer.Sound(self.sound1)
        self.sound2 = pygame.mixer.Sound(self.sound2)
        self.sound3 = pygame.mixer.Sound(self.sound3)
        self.sound4 = pygame.mixer.Sound(self.sound4)
        self.sound5 = pygame.mixer.Sound(self.sound5)
        self.sound6 = pygame.mixer.Sound(self.sound6)
        self.sound7 = pygame.mixer.Sound(self.sound7)
        self.sound8 = pygame.mixer.Sound(self.sound8)

        self.sound_cannon_key = False 
        self.sound_powerup_key = False
        self.sound_smallExplosion1_key = False
        self.sound_machinegun_key = False
        #初始化音效控制

    def music_player(self):
        '''
        音乐控制代码
        '''

        if (self.bgm_key == True) and (not pygame.mixer.music.get_busy()):
            pygame.mixer.music.load(self.music_lst[self.bgm_num])
            pygame.mixer.music.play(loops=-1)
            #开始音乐
        elif (self.bgm_key == False) and (pygame.mixer.music.get_busy()):
            pygame.mixer.music.pause()
            #暂停音乐
        elif  self.bgm_num_temp != self.bgm_num :
            pygame.mixer.music.load(self.music_lst[self.bgm_num])
            pygame.mixer.music.play(loops=-1)
            self.bgm_num_temp = self.bgm_num
            #切换并重新开始播放新音乐

    def sound_player(self):
        '''
        音效控制代码
        '''
        if self.sound_cannon_key == True:
            pygame.mixer.Sound.play(self.sound7,loops=0)
            self.sound_cannon_key = False
        
        if self.sound_powerup_key == True:
            pygame.mixer.Sound.play(self.sound2,loops=0)
            self.sound_powerup_key = False

        if self.sound_smallExplosion1_key == True:
            pygame.mixer.Sound.play(self.sound3,loops=0)
            self.sound_smallExplosion1_key = False
        if self.sound_machinegun_key == True:
            pygame.mixer.Sound.play(self.sound10,loops=0)
            self.sound_machinegun_key = False
