import pygame
from player import *
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, ASTEROID_MAX_RADIUS)
        self.velocity = pygame.Vector2(100,0)
    
    def draw(self, screen):
        return pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            int(self.radius),
            2
        )

    def update(self, dt):
        self.position += self.velocity * dt