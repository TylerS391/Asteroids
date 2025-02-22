import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

        self.rect = pygame.Rect(int(self.position.x - self.radius),
                                int(self.position.y - self.radius),
                                int(self.radius * 2),
                                int(self.radius * 2))

        if hasattr(self, "containers"):
            self.add(*self.containers)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = (int(self.position.x), int(self.position.y))

        if (self.position.x < -self.radius or self.position.x > SCREEN_WIDTH + self.radius or
                self.position.y < -self.radius or self.position.y > SCREEN_HEIGHT + self.radius):
            self.kill()

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), int(self.radius), 2)
