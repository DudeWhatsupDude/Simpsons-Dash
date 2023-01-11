import pygame

pygame.init()

class Particle():
  def __init__(self, x, y, xvel, yvel, radius, color, gravity=None):
    self.x = x
    self.y = y
    self.xvel = xvel
    self.yvel = yvel
    self.radius = radius
    self.color = color
    self.gravity = gravity

  def render(self, win):
    self.x += self.xvel
    self.y += self.yvel
    if self.gravity != None:
      self.yvel += self.gravity
      self.radius -= 0.03

    pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)