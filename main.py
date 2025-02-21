import pygame
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    screen =   pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    updatables.add(player)
    drawables.add(player)

    asteroid = Asteroid(100, 100, ASTEROID_MAX_RADIUS)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60) / 1000
        
        updatables.update(dt)

        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        
        

if __name__ == "__main__":
    main()