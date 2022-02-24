"""TODO: This is a forest with a sun and blue sky."""

__author__ = "730411898"

from random import randint
from turtle import _Screen, Screen, Turtle, TurtleScreen, colormode, done
colormode(255)

def main() -> None:
    main_turtle: Turtle = Turtle()
    main_turtle.speed(50)
    """This is a forest with a sun and blue sky."""
    sun(main_turtle)
    tree(main_turtle, 280, -250)
    leaves(main_turtle, 265, -70)
    tree(main_turtle, 180, -250)
    leaves(main_turtle, 165, -70)
    tree(main_turtle, 80, -250)
    leaves(main_turtle, 65, -70)
    tree(main_turtle, -20, -250)
    leaves(main_turtle, -35, -70)
    tree(main_turtle, -120, -250)
    leaves(main_turtle, -135, -70)
    tree(main_turtle, -220, -250)
    leaves(main_turtle, -235, -70)
    sky(main_turtle)
    done()

def sun(a_turtle: Turtle) -> None:
    """This is a sphere representing a sun."""
    z: int = 0
    z = z + randint(0,10)
    while z > 5:
        a_turtle.color(255,215,0)
        a_turtle.begin_fill()
        a_turtle.pensize(1)
        a_turtle.penup()
        a_turtle.goto(-250, 180)
        a_turtle.setheading(0)
        a_turtle.pendown
        a_turtle.circle(40)
        a_turtle.end_fill()
        break
    while z < 5:
        a_turtle.color(255,215,0)
        a_turtle.begin_fill()
        a_turtle.pensize(1)
        a_turtle.penup()
        a_turtle.goto(250, 180)
        a_turtle.setheading(0)
        a_turtle.pendown
        a_turtle.circle(40)
        a_turtle.end_fill()
        break

def tree(b_turtle: Turtle, x: float, y: float) -> None:
    """This is a rectangle that is brown"""
    b_turtle.color(165, 42, 42)
    b_turtle.begin_fill()
    b_turtle.pensize(0)
    b_turtle.penup()
    b_turtle.goto(x, y)
    b_turtle.setheading(90)
    b_turtle.pendown
    b_turtle.forward(200)
    b_turtle.left(90)
    b_turtle.forward(30)
    b_turtle.left(90)
    b_turtle.forward(200)
    b_turtle.left(90)
    b_turtle.forward(30)
    b_turtle.end_fill()

def leaves(c_turtle: Turtle, x: float, y: float) -> None:
    """This is the leaves on the tree."""
    c_turtle.color(127, 255, 0)
    c_turtle.begin_fill()
    c_turtle.pensize(3)
    c_turtle.penup()
    c_turtle.goto(x, y)
    c_turtle.circle(50)
    c_turtle.setheading(90)
    c_turtle.pendown
    c_turtle.end_fill()

def sky(d_turtle: Turtle) -> None:
    """This is a blue sky"""
    d_turtle.screen.bgcolor(135,206,235)


if __name__ == "__main__":
    main()
else:
    print(__name__)