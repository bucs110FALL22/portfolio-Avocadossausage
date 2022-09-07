import turtle

my_turtle = turtle.Turtle() 
window = turtle.Screen()
my_turtle.color('purple')
my_turtle.shape("turtle")

my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)

my_turtle.color('red')
my_turtle.penup()
my_turtle.backward(100)
my_turtle.pendown()

my_turtle.backward(50)
my_turtle.left(90)
my_turtle.backward(50)
my_turtle.left(90)
my_turtle.backward(50)
my_turtle.left(90)
my_turtle.backward(50)

window.exitonclick()