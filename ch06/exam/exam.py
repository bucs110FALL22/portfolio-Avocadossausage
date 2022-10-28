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
  
def eyes():
  circle(50)
  spook.goto(0, 100)
  circle(50)
  spook.goto(0, -100)


