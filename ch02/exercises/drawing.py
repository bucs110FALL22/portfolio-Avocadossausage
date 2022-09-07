import turtle

my_turtle = turtle.Turtle() 
my_screen = turtle.Screen()
## variable = modile.object 
## capital letter creates an object
my_turtle.color('purple')
my_turtle.shape("turtle")

sides = int(input("Please input number of sides"))
length = int(input("Please input length"))
angle = 360 / sides

for num in [angle] * sides:
  my_turtle.forward(length)
  my_turtle.left(num)

window = turtle.Screen()
window.bgcolor("yellow")
window.exitonclick() ##always last line of code
## most data should be saved in a variable (exception is a constant)