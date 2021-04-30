# print("Hello world")

# keep players in zone
# edges should hit the ball


import turtle
import time
import winsound

# Setup:
win=turtle.Screen()
win.title("Pong")
win.bgcolor("Black")
win.setup(width=800, height=600)
win.tracer()

# Divider:
div=turtle.Turtle()
div.speed(5)
div.penup()
div.goto(0,300)
div.pendown()
div.color("white")
div.pensize(13)
div.hideturtle()
div.left(180)
div.forward(400)
div.left(90)
div.forward(600)
div.left(90)
div.forward(800)
div.left(90)
div.forward(600)
div.left(90)
div.forward(400)
div.left(90)
for i in range(60):
    div.showturtle()
    div.pensize(1)
    div.speed(5)
    div.forward(5)
    div.penup()
    div.forward(5)
    div.pendown()
div.hideturtle()

# Score variables
scorea=0
scoreb=0


# Attacker~1:
a1=turtle.Turtle()
a1.speed(0)
a1.shape("square")
a1.color("red")
a1.shapesize(stretch_wid=5,stretch_len=1,)
a1.penup()
a1.goto(-350,0)

# Attacker~2:
a2=turtle.Turtle()
a2.speed(0)
a2.shape("square")
a2.color("blue")
a2.shapesize(stretch_wid=5,stretch_len=1,)
a2.penup()
a2.goto(350,0)

# BALL:
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
dang=5
ball.dx=dang
ball.dy=-dang

# Pen/score:
pen=turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.up()
pen.hideturtle()
pen.goto(0,260)
pen.write("RED:0  BLUE:0",align="center",font=("Rock",24,"normal"))

# Functions:
def a1u():
    y=a1.ycor()
    y+=20
    a1.sety(y)

def a1d():
    y=a1.ycor()
    y-=20
    a1.sety(y)

def a2u():
    y=a2.ycor()
    y+=20
    a2.sety(y)

def a2d():
    y=a2.ycor()
    y-=20
    a2.sety(y)  

# Keyboard calling
win.listen()
win.onkeypress(a1u,"w")
win.onkeypress(a1d,"s")
win.onkeypress(a2u,"Up")
win.onkeypress(a2d,"Down")

# Main Game Loop:
bob=True
while bob==True:
    win.update()
    # Movment of the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        # ball.goto(0,0)
        ball.dx *= -1
        # scorea -=1
        # pen.clear()
        # pen.write("RED:{}  BLUE:{}".format(scoreb,scorea), align="center", font=("Rock", 24, "normal"))

    if ball.xcor() < -390:
        # ball.goto(0, 0)
        ball.dx *= -1
        # scoreb -= 1
        # pen.clear()
        # pen.write("RED:{}  BLUE:{}".format(scoreb,scorea), align="center", font=("Rock", 24, "normal"))

    if scorea ==10:
        pen.color("blue")
        pen.clear()
        pen.write("BLUE HAS WON THE GAME", align="center", font=("Rock", 24, "normal"))
        time.sleep(10)
        bob==False
        break

    if scoreb ==10:
        pen.color("red")
        pen.color()
        pen.clear()
        pen.write("RED  HAS WON THE GAME", align="center", font=("Rock", 24, "normal"))
        time.sleep(10)
        bob==False
        break

    dash=4000
    if (ball.xcor() > 340 and ball.xcor() < dash)and(ball.ycor() < a2.ycor() + 40 and ball. ycor() > a2.ycor()-50):
        ball.setx(340)
        ball.dx *= -1
        scorea += 1
        pen.clear()
        pen.write("RED:{}  BLUE:{}".format(scoreb, scorea), align="center", font=("Rock", 24, "normal"))
        # if scorea == -1:
        #     scorea = 0
    if (ball.xcor() < -340 and ball.xcor() > -dash)and(ball.ycor() < a1.ycor() + 40 and ball. ycor() > a1.ycor()-50):
        ball.setx(-340)
        ball.dx *= -1
        scoreb += 1
        pen.clear()
        pen.write("RED:{}  BLUE:{}".format(scoreb, scorea), align="center", font=("Rock", 24, "normal"))
        if scoreb == -1:
            scoreb=0
    if a1.ycor()>300:
        a1.ycor(300)

while bob==True:
    winsound.PlaySound("Songs", winsound.SND_ASYNC)