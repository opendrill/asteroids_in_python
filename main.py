import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from AsteroidField import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}, Screen width: {SCREEN_WIDTH}, Screen height: {SCREEN_HEIGHT}")

    #Starting pygame
    pygame.init()

    #Defining pygame groups.
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #Must be before instantiation of player objects.
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    #Creating window for game to run in.
    game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #Time.
    clock = pygame.time.Clock()
    fps = 60
    dt = 0.0 #Delta time, time passed.

    center_pos_x = SCREEN_WIDTH / 2
    center_pos_y = SCREEN_HEIGHT / 2
    
    #Create instance of player object:
    player_instance = Player(center_pos_x, center_pos_y)
    #Create instance of asteroid field:
    AsteroidField_instance = AsteroidField()

    #Core game loop
    while True:

        #Checking pygame.events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Setting game background colour.
        game_window.fill("black")

        #Checking the current state of the all updatables.
        for member in updatable:
            member.update(dt)
       
        #Drawing drawable objects.
        for member in drawable:
            member.draw(game_window)
        
        #Collision check
        for asteroid in asteroids:
            #Checking for collisions with players.
            if asteroid.collides_with(player_instance) == True:
                print("GAME OVER!")
                sys.exit()
            #Checking for collisions with shots.
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()

        #Refreshing the screen and ticking the clock.
        pygame.display.flip()
        dt = clock.tick(fps) / 1000 #Enforces FPS #Dividing by 1000 converts the FPS from milliseconds to seconds.

if __name__ == "__main__":
     main()
