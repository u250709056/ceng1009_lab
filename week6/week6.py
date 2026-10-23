
# --getting ready--
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


# --Functions--
def drawPoly(someturtle,somesides, somesize):


    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(360 / somesides)

def drawSpiral(someturtle,angle):
    size = 1
    for i in range(100):
        someturtle.forward(size)
        someturtle.left(angle)
        size = size + 2

def drawEquitriangle(someturtle, somesize):
    drawPoly(someturtle, 3, somesize)
def drawStar(someturtle, size):
    for i in range(5):
        someturtle.forward(size)
        tess.right(144)

def drawSprite(someturtle, numberl, lenghtl):
    angle = 360 / numberl
    for i in range(numberl):
        someturtle.forward(lenghtl)
        someturtle.backward(lenghtl)
        someturtle.left(angle)





# --Exercise 1--
# tess.color("pink")
# tess.pensize(3)
# drawPoly(tess, 8,50)

# --Exercise 2--
# tess.color("blue")
# tess.pensize(3)
# for i in range(25):
#     drawPoly(tess,4,100)
#     sai.left(15)


# --Exercise 3--
# tess.pencolor("blue")
# tess.pensize(3)
# tess.penup()
# tess.goto(-150,0)
# tess.pendown()
# drawSpiral(tess,90)
#
# tess.penup()
# tess.goto(150,0)
# tess.pendown()
# drawSpiral(tess,89)

# --Exercise 4--
# drawEquitriangle(tess, 100)

# --Exercise 5--
# tess.color("hotpink")
# tess.penup()
# tess.goto(-200,0)
# tess.pendown()
# for i in range (5):
#     drawStar(tess,50)
#     tess.penup()
#     tess.forward(350)
#     tess.right(144)
#     tess.pendown()

# -- Exercise 6
# drawSprite(tess,15,20)
# -- Finale
wn.exitonclick()