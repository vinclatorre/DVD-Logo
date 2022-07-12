import pygame
import sys
from logo import Logo

class DVD_logo:
    '''Main class'''
    
    def __init__(self):
        '''Inizialize pygame and create Logo'''
        pygame.init()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.logo = Logo(self)

    def run_game(self):
        '''Main loop'''
        while True:
            self.check_events()
            self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def update_screen(self):
        self.screen.fill((0,0,0))
        self.logo.update()
        self.logo.draw()
        pygame.display.update()

if __name__ == '__main__':
    dvd = DVD_logo()
    dvd.run_game()
        

    
