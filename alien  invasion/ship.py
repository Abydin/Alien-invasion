import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        """initialize the ship and set its starting position."""
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store a deci,al value for the ship's center.
        self.center = float(self.rect.centerx)

        #movement flags
        self.moving_right =False
        self.moving_left = False
        #self.moving_up = False
        #self.moving_down = False

    def update(self):
        """update the ship's position based on the movement flag."""
        #update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        #if self.moving_up and self.rect.top> 0:
            #self.rect.bottom -= self.ai_settings.ship_speed_factor
        #if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            #self.rect.bottom += self.ai_settings.ship_speed_factor
                
       
        #update rect object from self.center.
        self.rect.centerx = self.center
       

    def blitme(self):
        """draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """center the ship on the screen."""
        self.center = self.screen_rect.centerx

        
