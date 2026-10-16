# import random
#
# for i in range (10):
#     k = random.random()
#     print(k)

# import random
#
# for i in range(10):
#     k = random.randrange(25,36)
#     print(k)

# import math
# x = int(input("Give me base:"))
# y = int(input("Give me height:"))
# print("This is your hipotenus", math.hypot(x,y))


# import math
# def areaOfCircle(r) :
#
#     return math.pi * r**2
#
# r = float(input("Enter the radius of the circle: "))
# print(areaOfCircle(r))
#
#
# import turtle
# def star(t , side):
#     for i in range (5):
#         t.forward(side)
#         t.right(144)
#
# screen = turtle.Screen()
# tess= turtle.Turtle()
# star(tess,100)
# screen.exitonclick()

# import turtle
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# sai = turtle.Turtle()
# sai.color("pink")
# sai.pensize(3)
#
# def drawsquare(t,):
#     t.penup()
#     t.goto(-100 , 0)
#     t.pendown()
#
#     for i in range(5):
#
#         for j in range(4):
#             t.fd(20)
#             t.lt(90)
#         t.penup()
#         t.fd(50)
#         t.pendown()
#
# drawsquare(sai)
# wn.exitonclick()

# import turtle
#
# def drawsquare(t,l):
#
#     for j in range(4):
#         t.fd(l)
#         t.lt(90)
#
#
# sai = turtle.Turtle()
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# sai.pencolor("pink")
# sai.pensize(3)
# for l in range(20, 120 ,20):
#     drawsquare(sai, l)
#     sai.penup()
#     sai.backward(10)
#     sai.right(90)
#     sai.forward(10)
#     sai.left(90)
#     sai.pendown()
# wn.exitonclick()
