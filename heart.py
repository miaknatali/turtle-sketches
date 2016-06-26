import turtle

ada = turtle.Turtle()  # Creating ada turtle


def make_heart(t):
    t.begin_fill()
    t.left(60)
    t.forward(100)
    t.left(30)
    t.circle(25, 180)
    t.left(180)
    t.circle(25, 180)
    t.left(30)
    t.forward(100)
    t.left(60)
    t.end_fill()

ada.color('purple', 'pink')
ada.penup()

make_heart(ada)

turtle.done()
