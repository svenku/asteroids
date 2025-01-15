import pygame
from constants import *
from player import Player

def main():
  pygame.init()
  
  clock = pygame.time.Clock()
  dt = 0
  
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
  print('Starting asteroids!')
  print(f'Screen width: {SCREEN_WIDTH}')
  print(f'Screen height: {SCREEN_HEIGHT}')

  while True:
    
    screen.fill(BLACK)
    player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    player.draw(screen)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        return
    
    dt = clock.tick(60)/1000
    
    pygame.display.flip()

if __name__ == "__main__":
    main()