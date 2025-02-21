import pygame
from constants import *
from player import *
from circleshape import *
def main():
    print("Starting Asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    screen =   pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    updatables.add(player)
    drawables.add(player)
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