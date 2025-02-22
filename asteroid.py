import pygame
from player import *
from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity = None):
        super().__init__(x,y, ASTEROID_MAX_RADIUS)
        self.radius = radius
        self.velocity = velocity or pygame.Vector2(100,0)
        self.rect = pygame.Rect(int(self.position.x - self.radius),
                                int(self.position.y - self.radius),
                                int(self.radius * 2),
                                int(self.radius * 2))
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
        self.rect.center = (int(self.position.x), int(self.position.y))
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            angle = random.uniform(20, 50)  
            v1, v2 = self.velocity.rotate(angle), self.velocity.rotate(-angle)  

            new_r = self.radius - ASTEROID_MIN_RADIUS

            a1 = Asteroid(self.position.x, self.position.y, new_r)
            a2 = Asteroid(self.position.x, self.position.y, new_r)

            a1.velocity = v1 * 1.2
            a2.velocity = v2 * 1.2

            self.kill()