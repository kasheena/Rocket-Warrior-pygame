import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen, ship):
        super().__init__()
        self.screen = screen

        #Create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, 8, 20)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Store the bullet's position as a decimal value
        self.y = float(self.rect.y)
        self.color = (230, 230, 230)
        self.speed_factor = 3

    def update(self):
        #Update the decimal up the screen
        self.y -= self.speed_factor
        #Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)        
