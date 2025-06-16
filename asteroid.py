import pygame
import random

from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            velocity = self.velocity * 1.2
            velocity = velocity.rotate(random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            self.spawn(new_radius, self.position, velocity)
            velocity = velocity.rotate(-random_angle)
            self.spawn(new_radius, self.position, velocity)   

    def kill(self):
        pygame.sprite.Sprite.kill(self)