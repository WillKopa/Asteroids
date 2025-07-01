import pygame
import random

from constants import ASTEROID_MIN_RADIUS
from sprites.circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.display):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = v1 * 1.2

            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a2.velocity = v2 * 1.2
        
        self.kill()

    def update(self, dt: float):
        self.position = self.position + (self.velocity * dt)