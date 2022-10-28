import turtle
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
  spook.goto(150, 0)
  for i in range(unique_sides):
    spook.right(90)
    spook.forward(l)
    spook.right(90)
    spook.forward(w)
  spook.end_fill()
  spook.pu()

def wavy_bottom(num_waves):
  x = 120
  y = -330
  ## num 10
  spook.pu()
  for i in range(num_waves):
    spook.goto(x, y)
    circle(60)
    x = x - 60

def ghost_base():
  spook.pu()
  spook.color("white")
  spook.goto(0, -150)
  circle(150)
  rectangle(300, 300)
  wavy_bottom(5)

def eyes():
  spook.color("black")
  spook.goto(-55, 0)
  circle(40)
  spook.goto(55, 0)
  circle(40)
  spook.color("white")
  spook.goto(-35, 30)
  circle(5)
  spook.goto(75, 30)
  circle(5)
  
def mouth():
  spook.color("red")
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