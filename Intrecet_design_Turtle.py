import turtle
import random

win = turtle.Screen()
win.title("Design @Shivansh")
win.bgcolor("black")
win.setup(800,700)

x = 1

while x < 400:
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)

    turtle.colormode(r,g,b)

    t = turtle.Turtle()
    t.speed(-1)
    t.pencolor(r,b,g)

    t.fd(50 + x)
    t.rt(90.911)

    x += 1

exitonclick()