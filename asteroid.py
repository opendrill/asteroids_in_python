import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = "white"

    def draw(self, game_window):
        pygame.draw.circle(game_window, self.colour, self.position , self.radius)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            #Create a random angle between 20 and 50 degrees.
            random_angle = random.uniform(20, 50)
            
            #Determining a new vector for the new asteroids to move in.
            new_vector_1 = self.velocity.rotate(random_angle)
            new_vector_2 = self.velocity.rotate(-random_angle) #They must move in opposing directions.
            
            #Split asteroids must be smaller so we subtract the min radius from the current.
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            #Instantiate new asteroid objects.
            split_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            
            #Set the prevously determined velocities for the new asteroids.
            split_asteroid_1.velocity = new_vector_1 * 1.2
            split_asteroid_2.velocity = new_vector_2 * 1.2

    def update(self, dt):
        self.position += self.velocity * dt

    
