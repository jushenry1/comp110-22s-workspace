from turtle import Turtle, colormode, done
leo : Turtle = Turtle()

leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)

i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i = i + 1

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

leo.penup()
leo.goto(45, 60)
leo.pendown()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

    leo.color("blue")
    colormode(255)
    leo.color(99, 204, 250)

    leo.begin_fill()
    # code for shape to be filled
    leo.end_fill

    leo.pencolor("pink")
    leo.fillcolor(32, 67, 93)
    leo.color("green", "yellow")

    leo.speed(50)
    leo.hideturtle

bob: Turtle = Turtle()
i: int = 0
while (i < 3):
    bob.color("black")
    bob.penup()
    bob.goto(45,60)
    bob.pendown()
    bob.speed(60)
    bob: Turtle = Turtle()
    bob.forward(120)
    bob.left(40)
    i = i + 1

side_length: int = 300
i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    side_length = side_length * 0.97
    i = i + 1