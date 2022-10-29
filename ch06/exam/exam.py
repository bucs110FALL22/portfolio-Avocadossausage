import turtle
import random
window = turtle.Screen()
window.bgcolor("pink")
window.screensize(1000, 1000)
spook = turtle.Turtle()

def circle(r):
  spook.pd()
  spook.begin_fill()
  spook.circle(r)
  spook.end_fill()
  spook.pu()

def rectangle(l,w): 
  unique_sides = 2
  spook.goto(150, 0)
  spook.pd()
  spook.begin_fill()
  for i in range(unique_sides):
    spook.right(90)
    spook.forward(l)
    spook.right(90)
    spook.forward(w)
  spook.end_fill()
  spook.pu()

def eye_highlight():
  colors = ["yellow", "white", "pink"]
  chosen_color = random.choice(colors)
  return chosen_color ##returns random color out of colors
  
def wavy_bottom(num_waves):
  x = 112.5
  y = -330
  spook.pu()
  for i in range(num_waves):
    spook.goto(x, y)
    circle(37.5)
    x = x - 75

def ghost_base():
  spook.pu()
  spook.color("white")
  spook.goto(0, -150)
  circle(150)
  rectangle(300, 300)
  wavy_bottom(4)

def eyes():
  spook.color("black")
  spook.goto(-55, 0)
  circle(40)
  spook.goto(55, 0)
  circle(40)
  spook.color(eye_highlight())
  spook.goto(-35, 30)
  circle(5)
  spook.goto(75, 30)
  circle(5)
  
def mouth():
  spook.color("pink")
  spook.goto(0, -75)
  circle(20)

def main():
  spook.color("white")
  spook.hideturtle()
  ghost_base()
  eyes()
  mouth()
  window.exitonclick()

main()