import pygame

class Particle():
  def __init__(self, pos,max, min, stvel = [0,0], graphics='circle'):
    self.x_pos = pos[0]
    self.y_pos = pos[1]
    self.mygraphics = graphics
    self.max_x = max[0]
    self.max_y = max[1]
    self.min_x = min[0]
    self.min_y = min[1]
    self.vel_x = stvel[0]
    self.vel_y = stvel[1]
  def render(self, display_surface):
    pygame.draw.circle(display_surface, (255, 0, 0), (self.x_pos,self.y_pos), 4)
  
  def Phisics(self):
    self.vel_y += 1
    if self.y_pos >= self.max_y:
      self.vel_y *= -0.9
    self.y_pos += self.vel_y