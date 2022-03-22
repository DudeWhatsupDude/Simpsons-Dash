import pygame

class Player:
  def __init__(self, POS, mygraphic='cube'):
    self.x_pos = POS[0]
    self.y_pos = POS[1]
    self.graphics = mygraphic
    self.y_vel = 0
    self.rect = mygraphic.get_rect()
    self.Alive = True
    
  def Apply_phisics(self, isUp):
    if self.y_pos >= 500:
      self.y_vel = 0
      self.y_pos = 500
      if isUp:
        self.y_vel = -15
    else:
      self.y_vel += 0.75
    self.y_pos += self.y_vel
  def render(self, display_surface):
    self.rect.x = self.x_pos
    self.rect.y = self.y_pos
    
    display_surface.blit(self.graphics, [self.x_pos, self.y_pos])