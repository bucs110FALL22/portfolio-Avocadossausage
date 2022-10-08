import pygame
import random
import math

pygame.init()

## Variables

window = pygame.display.set_mode((500, 500))
screen_size = pygame.display.get_window_size()
width = screen_size[0]
height = screen_size[1]
radius = width/2
midp1 = width/2
midp2 = height/2 
n = 10
bluescore = 0
redscore = 0
guess = True
playerchoice = ""

Rectangle1 = pygame.Rect(0, 0, 250, 250)
Rectangle2 = pygame.Rect(250, 0, 250, 250)
pygame.draw.rect(window, "red", Rectangle1)
pygame.draw.rect(window, "blue", Rectangle2)
pygame.display.update()

while guess:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.pos[0] > 250:  
        playerchoice == "blue"
        guess = False
      elif event.pos[0] < 250:
        playerchoice == "red"
        guess = False


window.fill("white")
pygame.draw.circle(window, "pink", (midp1, midp2), radius, 0)
pygame.draw.line(window, "black", (midp1, 0), (midp2, height), 5)
pygame.draw.line(window, "black", (0, midp2), (width, midp2), 5)
pygame.display.update()
      
for i in range(n):
  dartpos_x = random.randrange(0, width)
  dartpos_y = random.randrange(0, height)
  dartpos_x2 = random.randrange(0, width)
  dartpos_y2 = random.randrange(0, height)
          
  distance_from_center = math.hypot(dartpos_x - midp1, dartpos_y - midp2)
  is_in_circle = distance_from_center <= width/2
  distance_from_center2 = math.hypot(dartpos_x2 - midp1, dartpos_y2 - midp2)
  is_in_circle2 = distance_from_center2 <= width/2
          
  if is_in_circle == True:
    pygame.draw.circle(window, "blue", (dartpos_x, dartpos_y), 10, 0)
    bluescore += 1
    pygame.display.update()
    pygame.time.delay(200)
      
  else:
    pygame.draw.circle(window, "black", (dartpos_x, dartpos_y), 10, 0)
    pygame.display.update()
    pygame.time.delay(200)
          
  if is_in_circle2 == True:
    pygame.draw.circle(window, "red", (dartpos_x2, dartpos_y2), 10, 0)
    redscore += 1
    pygame.display.update()
    pygame.time.delay(200)
      
  else:
    pygame.draw.circle(window, "black", (dartpos_x2, dartpos_y2), 10, 0)
    pygame.display.update()
    pygame.time.delay(200)

if playerchoice == "blue" and bluescore > redscore:
  print("You win!")
elif redscore < bluescore:
  print("You lose!")
else:
  print("Tie!")

pygame.time.delay(10000)