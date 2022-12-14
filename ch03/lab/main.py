import turtle
import random
import pygame
import math


window = turtle.Screen()  # 2.  Create a screen
window.bgcolor("white")

michelangelo = turtle.Turtle()  # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color("orange")
leonardo.color("blue")
michelangelo.shape("turtle")
leonardo.shape("turtle")

michelangelo.up()  # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)
michelangelo.speed(1)
leonardo.speed(1)

## 5. Your PART A code goes here

randnum = random.randrange(1, 101)
michelangelo.forward(randnum)
leonardo.forward(randnum)

michelangelo.setposition(-100, 20)
leonardo.setposition(-100, -20)

for looper in [1, 11]:
    randnum = random.randrange(0, 11)
    michelangelo.forward(randnum)
    leonardo.forward(randnum)

window.exitonclick()




# PART B - complete part B here

pygame.init()
window = pygame.display.set_mode((500, 500))

def shapeDrawer(num_sides):

    coords = []
    num_sides = num_sides
    side_length = 25
    offset = 100

    for i in range(num_sides):
        theta = (2.0 * math.pi * i) / num_sides
        x = side_length * math.cos(theta) + offset
        y = side_length * math.sin(theta) + offset
        coords.append([x, y])

    return coords

window.fill("white")
pygame.display.flip()

pygame.draw.polygon(window, "red", shapeDrawer(3))
pygame.display.flip()
pygame.time.delay(500)

window.fill("white")
pygame.display.flip()

pygame.draw.polygon(window, "green", shapeDrawer(4))
pygame.display.flip()
pygame.time.delay(500)

window.fill("white")
pygame.display.flip()

pygame.draw.polygon(window, "purple", shapeDrawer(6))
pygame.display.flip()
pygame.time.delay(500)

window.fill("white")
pygame.display.flip()

pygame.draw.polygon(window, "yellow", shapeDrawer(9))
pygame.display.flip()
pygame.time.delay(500)

window.fill("white")
pygame.display.flip()

pygame.draw.polygon(window, "blue", shapeDrawer(360))
pygame.display.flip()
pygame.time.delay(500)

window.fill("white")
pygame.display.flip()
##test
pygame.quit()
