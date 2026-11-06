# #exercise1
#
# def marker(x):
#     if x >= 90:
#         return "A"
#     elif x > 80:
#         return "B"
#     elif x >= 70:
#         return "C"
#     elif x >= 60:
#         return "D"
#     else:
#         return "F"
#
# note = int(input("Enter a note: "))
# print(marker(note))

# #exercise2
# import turtle
#
# def drawBar(t,height,gap):
#     t.penup()
#     t.left(90)
#     t.forward(height+gap)
#     t.write(" "+str(height))
#     t.backward(height+gap)
#     t.rt(90)
#     t.pendown()
#
#     t.fillcolor(choose_color(height))
#     t.begin_fill()
#     t.left(90)
#     t.fd(height)
#     t.rt(90)
#     t.fd(40)
#     t.rt(90)
#     t.fd(height)
#     t.lt(90)
#     t.end_fill()
#
# def bar(data):
#     maxheight = max(data)
#     num_bars = len(data)
#     border = 10
#     gap = (maxheight-border)/25
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#
#     right = 40 * num_bars +border
#     top = maxheight +4 * border
#
#     wn.setworldcoordinates(-border,-border,right,top)
#     t = turtle.Turtle()
#     t.color("blue")
#
#     t.pensize(3)
#
#     for height in data:
#         drawBar(t, height, gap)
#
#
#     wn.exitonclick()
#
# def choose_color(height):
#     if height >= 200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "green"
#
#
#
# data = [48,117,-200,240,160,260,220]
#
# bar(data)

# #exercise3
#
# import turtle
#
# def drawBar(t,height,gap):
#
#     if (height >= 0):
#         labelY = (height + gap)
#     else:
#         labelY = (gap)
#     t.penup()
#     t.left(90)
#     t.forward(labelY+gap)
#     t.write(" "+str(height))
#     t.backward(labelY+gap)
#     t.rt(90)
#     t.pendown()
#
#     t.fillcolor(choose_color(height))
#     t.begin_fill()
#     t.left(90)
#     t.fd(height)
#     t.rt(90)
#     t.fd(40)
#     t.rt(90)
#     t.fd(height)
#     t.lt(90)
#     t.end_fill()
#
# def bar(data):
#     maxheight = max(data)
#     minheight = min(data)
#     num_bars = len(data)
#     border = 10
#     gap = (maxheight-border)/25
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#
#     right = 40 * num_bars +border
#     top = maxheight +4 * border
#     bottom = min(minheight,0) - border
#
#
#     wn.setworldcoordinates(-border,bottom,right,top)
#     t = turtle.Turtle()
#     t.color("blue")
#
#     t.pensize(3)
#
#     for height in data:
#         drawBar(t, height, gap)
#
#
#     wn.exitonclick()
#
# def choose_color(height):
#     if height >= 200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "green"
#
#
#
# data = [48,117,-200,240,160,260,220]
#
# bar(data)

# #exercise4
# import math
# def findHypot(x,y):
#
#     hypo = math.sqrt(x**2+y**2)   ##---We can write it like math.hypot(x,y)
#     return hypo
#
# print(findHypot(opp,adj))

# def calc_without_math(x,y):
#     hypom = (x**2+y**2) ** 0.5
#     return hypom
#
# opp = int(input("Opposite side:"))
# adj = int(input("Adjacent side:"))
#
# print(calc_without_math(opp,adj))




