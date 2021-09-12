import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the ship and set its rect
        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #Store adecimal value for the ship's center
        self.center = float(self.rect.centerx)

        #Movement flags
        self.moving_right = False
        self.moving_left = False


    def center_ship(self):
        self.center = self.screen_rect.centerx    

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor 
        
        #Update rect object from self.center
        self.rect.centerx = self.center



    def draw_ship(self):
        self.screen.blit(self.image, self.rect)
