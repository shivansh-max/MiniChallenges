# print("Hello World")
import turtle
import random

win = turtle.Screen()
win.bgcolor("black")
win.title("TREES")
win.setup(width=700,height=700)


BRANCH_COUNT = 9
TURN_ANGLE = 10
SHRINK_FACTOR = 0.8


def tree(size, depth):
    if depth >= 1:
        if random.random() > 0.33:
            turt.width(depth)
            turt.color(get_color(depth))
            turt.forward(size)
            turt.right(TURN_ANGLE)
            tree(size*SHRINK_FACTOR, depth-1)
            turt.right(TURN_ANGLE)
            tree(size*SHRINK_FACTOR, depth-1)
            turt.left(3*TURN_ANGLE)
            tree(size*SHRINK_FACTOR, depth-1)
            turt.left(TURN_ANGLE)
            tree(size*SHRINK_FACTOR, depth-1)
            turt.right(2*TURN_ANGLE)
            turt.color(get_color(depth))
            turt.backward(size)

def get_color(depth):
    if BRANCH_COUNT - depth < 3:
        return 'blue'
    else:
        return 'purple'



if __name__ == '__main__':
    random.seed(46)
    turt = turtle.Turtle()
    turt.setheading(90)
    turt.speed(-10)
    turtle.colormode(255)
    turt.goto(0,-100)
    tree(100, BRANCH_COUNT)
    turtle.done()

turtle.done()