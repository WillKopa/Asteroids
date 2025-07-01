import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: int):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.display):
        # sub-classes must override
        pass

    def update(self, dt: float):
        # sub-classes must override
        pass

    def isColliding(self, other: "CircleShape"):
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius
            
