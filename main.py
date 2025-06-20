import pygame
import sys
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

run_game = True

def main():
    pygame.init()
    screen_fps = pygame.time.Clock()
    dt = 0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    AsteroidField.containers = (updatable,)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while run_game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            
        screen.fill("black")
        player.draw(screen)
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_detected(player) == True:
                print("Game over!")
                sys.exit()
        
            for shot in shots:
                if asteroid.collision_detected(shot) == True:
                    asteroid.split()
                    shot.kill()
        
            
        pygame.display.flip()

        # FPS Control
        dt = screen_fps.tick(60) / 1000





if __name__ == "__main__":
    main()