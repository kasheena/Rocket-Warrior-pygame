import pygame
from ship import Ship
from alien import Alien
import functions as gf
from settings import Settings
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard
from game_stats import GameStats

def run_game():
    pygame.init()
    ai_settings = Settings()
    #set a screen 
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Rocket Warrior")

    #make a play button
    play_button = Button(ai_settings, screen, "PLAY")


    #Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #make a ship,a group of bullets and a group of aliens
    aliens = Alien(ai_settings, screen)
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()
    #Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #main loop
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)    
            
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
             
run_game()                   
 