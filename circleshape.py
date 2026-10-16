import pygame
#pygame has a default class for sprites that i'll inherit from.
#Circles will be the hitboxes for asteroids and the player character.

class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        #
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        
        #
        else:
            super().__init__()

        #Extra attributes needed for the asteroids and player.
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collides_with(self, other):
         distance_between_objects = self.position.distance_to(other.position)
         radius_sum = self.radius + other.radius
         if distance_between_objects <= radius_sum:
            return True
         else:
            return False