import pygame
import random

class Logo:
    '''Logo class'''
    def __init__(self, main):
        #Logo design
        self.FONT = pygame.font.SysFont('8-BIT WONDER', 50, bold = True)
        self.DVD = self.FONT.render('DVD', 1, (0,0,0))
        self.width = 100
        self.height = 60
        self.color = (255,255,255)

        #Logo position and speed
        self.x = 300
        self.y = 300
        self.speed_x = 1
        self.speed_y = 1

        #Screen
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()
        
    def color_shuffle(self):
        '''Randomize logo color'''
        r,g,b = random.randint(1,255),random.randint(1,255),random.randint(1,255)
        self.color = (r,g,b)

    def update(self):
        '''Logo movement'''
        self.x += self.speed_x
        self.y += self.speed_y
        self.check_collision()

    def check_collision(self):
        '''Border-Logo collision'''
        if self.x > self.screen_rect.width - self.width or self.x < 0:
            self.speed_x *= -1
            self.color_shuffle()
        elif self.y > self.screen_rect.height - self.height or self.y < 0:
            self.speed_y *= -1
            self.color_shuffle()

    def draw(self):
        '''Draw the Logo on the screen'''
        pygame.draw.rect(self.screen,self.color,[self.x,self.y,self.width,self.height])
        self.screen.blit(self.DVD,(self.x+10,self.y+10))
        
