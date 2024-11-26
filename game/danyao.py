import pygame
import sys
import random
class Danyao(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
    
    def _update_danyao():
        danyao = Danyao(sprite_image, (random.randint(0, 800 - sprite_image.get_width()), random.randint(0, 600 - sprite_image.get_height())))
            sprite_group.add(new_sprite)