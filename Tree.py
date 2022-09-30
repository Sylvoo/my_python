import turtle

t = turtle.Turtle()
t.speed(-7)
t.setheading(90)
t.penup()
t.goto(0, -200)
t.pendown()


def gałąź(t, len):
    if len == 0: return
    nt = t.clone()
    nt.forward(50)
    nt.left(20)
    gałąź(nt, len - 1)
    nt.right(40)
    gałąź(nt, len - 1)


gałąź(t, 7)
window = turtle.Screen()
window.exitonclick()