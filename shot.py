import pygame
from circleshape import CircleShape
from constants import RED, SHOT_RADIUS, SHOT_LINE_WIDTH

class Shot(CircleShape):
  def __init__(self, x, y, radius = SHOT_RADIUS):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, RED, self.position, self.radius, SHOT_LINE_WIDTH)

  def update(self, dt):
    self.position += self.velocity * dt