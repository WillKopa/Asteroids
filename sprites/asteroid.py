import pygame
from sprites.circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.display):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt: int):
        self.position = self.position + (self.velocity * dt)