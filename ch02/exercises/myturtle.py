import turtle

my_turtle = turtle.Turtle() 
window = turtle.Screen()
my_turtle.shape("turtle")
colors = ["red", "purple", "green"]
circle_deg = 90
length = 50

sides = 4
for c in colors: 
  my_turtle.color(c)
  for i in [0]*sides:
    my_turtle.left(circle_deg / sides)
    my_turtle.forward(length)

    my_turtle.penup()
    my_turtle.forward(100)
    my_turtle.pendown()
  
window.exitonclick()