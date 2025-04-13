import pygame
import random
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (updatable, drawable, asteroids)
  AsteroidField.containers = (updatable)
  Shot.containers = (updatable, drawable, shots)

  player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
  asteroid_field = AsteroidField()
  
  print('Starting asteroids!')
  print(f'Screen widtht : {SCREEN_WIDTH}')
  print(f'Screen height: {SCREEN_HEIGHT}')

  while True:
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        return

    for obj in updatable:
      obj.update(dt)

    for asteroid in asteroids:
      for shot in shots:
        if asteroid.check_collision(shot):
          print("Hit!")
          shot.kill()
          asteroid.split()
          break

    for obj in asteroids:
      if obj.check_collision(player):
        print("Game over!")
        pygame.quit()
        return
    
    screen.fill(BLACK)
    
    for obj in drawable:
      obj.draw(screen)  

    pygame.display.flip()
    dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
