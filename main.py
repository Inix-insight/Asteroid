import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state


def main():
    game_timer = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    dt = 0
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#    print(f"Starting Asteroids with pygame version: {pygame.version.ver }")
 #   print(f"Screen width: {SCREEN_WIDTH}")
  #  print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        dt = game_timer.tick(60) / 1000
        updatable.update(dt)

if __name__ == "__main__":
    main()
