
class Rectangle:
  
  def __init__(self, x, y, h, w):

    self.x = x
    self.y  = y
    self.h = h
    self.w = w

    if self.x < 0:
        self.x = 0
    if self.y < 0:
        self.y = 0
    if self.h < 0:
        self.h = 0
    if self.w < 0:
        self.w = 0
      
  def __str__(self):
    
    dimensions = str(self.x, self.y, self.h, self.w)
    return dimensions

