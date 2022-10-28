import turtle

window = turtle.Screen()
window.bgcolor("pink")
window.screensize(1000, 1000)
spook = turtle.Turtle()

spook.color("white")

def circle(r):
  spook.pd()
  spook.begin_fill()
  spook.circle(r)
  spook.end_fill()
  spook.pu()

  



def wavy_bottom(num_waves):
  x = 270
  y = 0
  spook.pu()
  ## num 10
  for i in range(num_waves):
    spook.goto(x, y)
    circle(60)
    x = x - 60



wavy_bottom(5)
