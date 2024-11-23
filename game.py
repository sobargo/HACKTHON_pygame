import sys
import pygame
class tank_war:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Tank War")
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
if __name__ == '__main__':
    tw = tank_war()
    tw.run_game()            