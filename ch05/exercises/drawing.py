import turtle

my_screen = turtle.Screen()

def drawEqShape(turt, num_sides, side_length):
  turt.shape("turtle")
  turt.color("green")
  angle = 360 / num_sides
  for num in [angle] * num_sides:
    turt.forward(side_length)
    turt.left(num)

side_length = int(input("Please input side length"))
num_sides = int(input("Please input number of sides"))
turt = turtle.Turtle()

drawEqShape(turt, num_sides, side_length)

my_screen.exitonclick()