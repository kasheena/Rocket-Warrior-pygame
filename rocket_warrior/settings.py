class Settings():
    
    def __init__(self):
        """Initialize the game's settings"""
        #Screen Settings
        self.screen_width = 600
        self.screen_height = 500 
        self.bg_color = (2,7,80)

        #Ship settings
        self.ship_speed_factor = 2
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed_factor = 6
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #Alien Settings
        self.alien_speed_factor = 10
        self.fleet_drop_speed = 32
        self.fleet_direction = 1

        #How quickly the game speeds up
        self.speedup_scale = 1.1
        #How quickly alein point value increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50


    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale     
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)


  
        