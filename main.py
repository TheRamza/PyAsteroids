import pygame
from constants import *
run_game = True

def main():
    pygame.init()
    screen_fps = pygame.time.Clock()
    dt = 0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while run_game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = screen_fps.tick(60) / 1000
        print(dt)





if __name__ == "__main__":
    main()