
## 31/10/2022


from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.listen()


def m_forward():
    t.forward(10)


def m_backward():
    t.backward(10)


def m_left():
    t.left(10)


def m_right():
    t.right(10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.onkeypress(m_forward, 'w')
screen.onkeypress(m_backward, 's')
screen.onkey(m_left, 'a')
screen.onkey(m_right, 'd')
screen.onkey(clear, 'c')

screen.exitonclick()
