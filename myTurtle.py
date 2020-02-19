import turtle

myTurtle = turtle.Pen()

myTurtle.pensize(4)
myTurtle.pencolor('pink')
myTurtle.fillcolor('black')
# 画一个六边形，并填充
myTurtle.begin_fill()
for i in range(3):
    myTurtle.forward(12)
    myTurtle.left(60)
    myTurtle.forward(12)
    myTurtle.left(60)
myTurtle.end_fill()
# 写一个数字2
myTurtle.forward(100)
myTurtle.right(90)
myTurtle.forward(100)
myTurtle.right(90)
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(100)

turtle.done()
