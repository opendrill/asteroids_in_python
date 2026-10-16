from constants import *
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x 
        self.y = y
        self.colour = "White"
    
    def draw(self, game_window):
        pygame.draw.circle(game_window, self.colour, self.position, self.radius)
    
    def update(self, dt):
        self.position += (self.velocity * dt)