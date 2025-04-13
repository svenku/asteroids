import pygame
import random
from circleshape import CircleShape
from constants import WHITE, ASTEROID_LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_SPEED_MULTIPLIER

class Asteroid(CircleShape):

  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, WHITE, self.position, self.radius, ASTEROID_LINE_WIDTH)

  def update(self, dt):
    self.position += self.velocity * dt
  
  def split(self):
    self.kill()
    # Check if the asteroid can be split
    if self.radius <= ASTEROID_MIN_RADIUS:  # Minimum size for splitting
        return
    # Split the asteroid into two smaller asteroids
    central_angle = random.uniform(20, 50)  # Random angle for splitting
    angle_left = self.velocity.rotate(-central_angle)
    angle_right = self.velocity.rotate(central_angle)

    new_radius = self.radius - ASTEROID_MIN_RADIUS
    # Create two new asteroids with the same position but different velocities
    # and smaller radius
    split_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
    split_asteroid1.velocity = angle_left * ASTEROID_SPLIT_SPEED_MULTIPLIER

    split_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
    split_asteroid2.velocity = angle_right * ASTEROID_SPLIT_SPEED_MULTIPLIER




