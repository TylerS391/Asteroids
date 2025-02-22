import pygame
from circleshape import CircleShape
from constants import *
from shot import *
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0.0
        self.rect = pygame.Rect(int(self.position.x - self.radius),
                                int(self.position.y - self.radius),
                                int(self.radius * 2),
                                int(self.radius * 2))
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        return pygame.draw.polygon(screen, "white", self.triangle(), 2 )
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_velocity = forward * PLAYER_SHOOT_SPEED
        shot_position = self.position + forward * (self.radius + SHOT_RADIUS)
        Shot(shot_position.x, shot_position.y, shot_velocity)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.rect.center = (int(self.position.x), int(self.position.y))
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_SPACE] and self.shoot_cooldown <= 0:
            self.shoot()
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt