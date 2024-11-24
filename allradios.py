import pygame
class  Mixaudio:
    def  __init__(self) -> None:
        self.music1 = r'test_game\asset\music\BLUE DRAGON_小林.mp3'
        self.music2 = r'test_game\asset\music\BLUE DRAGON_泽野.mp3'
        self.music3 = r'test_game\asset\music\Matryoshka - Sacred Play Secret Place.mp3'

        self.sound1 = r'test_game\asset\sounds\cannon1.mp3'
        self.sound2 = r'test_game\asset\sounds\powerup10.mp3'
        self.sound3 = r'test_game\asset\sounds\small_explosion1.mp3'
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

        self.sound_cannon_key = False 
        self.sound_powerup_key = False
        self.sound_smallExplosion1_key = False
        #初始化音效控制

    def music_player(self):#音乐控制代码

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

    def sound_player(self):#音效控制代码
        if self.sound_cannon_key == True:
            pygame.mixer.Sound.play(self.sound1,loops=0)
            self.sound_cannon_key = False
        
        elif self.sound_powerup_key == True:
            pygame.mixer.Sound.play(self.sound2,loops=0)
            self.sound_powerup_key = False

        elif self.sound_smallExplosion1_key == True:
            pygame.mixer.Sound.play(self.sound3,loops=0)
            self.sound_smallExplosion1_key = False
        