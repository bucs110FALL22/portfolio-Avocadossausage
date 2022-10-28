import turtle

window = turtle.Screen()
window.bgcolor("pink")
window.screensize(1000, 1000)
spook = turtle.Turtle()

spook.color("white")

spook.pd()
spook.begin_fill()
spook.circle(50)
spook.end_fill()
turtle.exitonclick()

