import pygame
from constants import *
from circleshape import *
from player import *

run_game = True

def main():
    pygame.init()
    screen_fps = pygame.time.Clock()
    dt = 0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while run_game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()

        # FPS Control
        dt = screen_fps.tick(60) / 1000





if __name__ == "__main__":
    main()