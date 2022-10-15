import pygame
pygame.init()

count = 0
upper_limit = 20
iters = {}
max_so_far = 0
max_val = 0
scale = 5
xcoord = 0
ycoord = 0
maxstring = ""

window = pygame.display.set_mode((200 , 200))
window.fill("white")

for start in range(2, (upper_limit + 1)):
  num = start
  count = 0
  while (num > 1):
    if num % 2 == 0:
      num = num/2
    else:
      num = (3 * num) + 1
    count += 1
    if count > max_so_far:
      max_so_far = count
      max_val = start
  num = start
  iters[num] = count
print(iters)
  
funct_list = list(iters.items())
if len(funct_list) >= 2:
  maxstring = str(max_so_far)
  max_val = funct_list[0]
  pygame.draw.lines(window, "black", False, funct_list)
  new_display = pygame.transform.flip(window, False, True)
  window.blit(new_display, (0,0))
  font = pygame.font.Font(None, 15)
  msg = font.render(maxstring, True,"blue")
  window.blit(msg, (10,10))
else:
  print("Not enough coordinates!")
pygame.display.update()
pygame.time.delay(20000)