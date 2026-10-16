import pygame
from shot import Shot
from circleshape import CircleShape
from constants import *

#We inherit from Cicleshape for hitbox
class Player(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.rotation = 0
        self.colour = "white"
        self.shot_cooldown = 0

    #The actual visual representation of the player, defining how to draw the triangle in this function:
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    #Polymorphism, override the draw method inherited from CircleShape.
    def draw(self, game_window):
        #Draws the triangle.
        pygame.draw.polygon(game_window, self.colour, self.triangle(), LINE_WIDTH)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        #Creates a vector (an arrow) for deciding direction of movement.
        unit_vector = pygame.Vector2(0, 1)
        
        #Turns vector to match the object's rotation.
        rotated_vector = unit_vector.rotate(self.rotation)

        #Scales the arrow to the distance the object will trabel in a frame. Decides the new position of the object.
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        
        #Updates the objects position.
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shot_cooldown > 0:
            pass
        else:
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN
            shot_instance = Shot(self.position.x, self.position.y)
            shot_instance_vector = pygame.Vector2(0, 1)
            rotated_shot_instance = shot_instance_vector.rotate(self.rotation)
            shot_instance.velocity = rotated_shot_instance * PLAYER_SHOOT_SPEED

    def update(self, dt):
        #This function should run every frame.
        keys = pygame.key.get_pressed()
        
        self.shot_cooldown -= dt

        #MOVEMENT, FORWARD/BACKWARD
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        
        #TURNING
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)

        #SHOOTING
        if keys[pygame.K_SPACE]:
            self.shoot()