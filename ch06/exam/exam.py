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

  
def rectangle(l,w): 
  unique_sides = 2
  spook.goto(150, 0)
  spook.pd()
  spook.begin_fill()
  spook.goto(150, 0)
  for i in range(unique_sides):
    spook.right(90)
    spook.forward(l)
    spook.right(90)
    spook.forward(w)
  spook.end_fill()
  spook.pu()


def wavy_bottom(num_waves):
  x = 285
  y = 0
  ## num 10
  for i in range(num_waves):
    spook.goto(x, y)
    circle(30)
    x = x - 15

def ghost_base():
  spook.color("white")
  spook.goto(0, -150)
  circle(150)
  rectangle(500, 300)
  wavy_bottom(10)

  
def eyes():
  spook.color("black")
  spook.goto(-55, 0)
  circle(40)
  spook.goto(55, 0)
  circle(40)

def mouth():
  spook.color("pink")
  spook.goto(0, -75)
  circle(20)


ghost_base()
eyes()
mouth()
