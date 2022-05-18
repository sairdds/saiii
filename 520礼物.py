import os
from turtle import *

def move(x, y, direct, angle):
    penup()
    goto(x, y)
    if direct=="l":
        left(angle)
    else:
        right(angle)
    pendown()

color("red")
pensize(1.5)
hideturtle()
# tracer(False)

move(0, 200, "l", 135)

for i in range(0, 80):
    forward(3)
    if 5<i<20:
        left(5)
    elif 20<i<30:
        right(5)
    elif 30<i<55:
        left(5)
    elif 55<i<60:
        right(20)
    elif 65<i<70:
        left(20)
    elif 70<i<80:
        left(10)

move(-20, 190, "l", 20)

for i in range(0, 45):
    forward(3)
    if 15<i<25:
        right(10)
    if 35<i<45:
        right(10)

move(0, 180, "r", 60)

for i in range(0, 35):
    forward(3)
    if 5<i<15:
        left(7)
    if 25<i<30:
        right(5)

move(-100, 130, "r", 70)

for i in range(0, 50):
    forward(3)
    if 0<i<5:
        right(3)
    elif 10<i<23:
        right(15)
    elif 25<i<42:
        left(5)
    elif 45<i<48:
        right(30)

move(0, 180, "l", 100)

for i in range(0, 40):
    forward(3)
    if 1<i<5:
        right(30)
    elif 7<i<25:
        right(5)

move(0, 180, "l", 70)

for i in range(0, 40):
    forward(3)
    if 0<i<3:
        right(5)
    elif 3<i<10:
        right(15)
    elif 20<i<25:
        left(10)

move(0, 60, "r", 90)

for i in range(0, 215):
    forward(3)
    if 10<i<15:
        right(5)
    elif 30<i<40:
        left(2)
    elif 40<i<50:
        left(3)
    elif 60<i<62:
        left(30)
    elif 62<i<65:
        left(70)
    elif 70<i<80:
        right(5)
    elif 100<i<105:
        left(10)
    elif 115<i<120:
        left(8)
    elif 130<i<135:
        right(5)
    elif 135<i<145:
        right(15)
    elif 155<i<170:
        right(5)
    elif 170<i<190:
        right(1)
    elif 190<i<195:
        right(5)

move(-40, 80, "r", 90)

for i in range(0, 105):
    forward(3)
    if 10<i<15:
        right(2)
    elif 20<i<26:
        left(10)
    elif 40<i<48:
        right(20)
    elif 48<i<55:
        right(5)
    elif 80<i<90:
        right(5)
    elif 90<i<105:
        right(1)

move(-40, 10, "l", 75)
color("green")

for i in range(0, 197):
    forward(3)
    if 95<i<97:
        left(90)
    elif 98<i<100:
        left(90)

move(-25, -45, "l", 0)
color("pink")
pensize(2)

fillcolor("pink")
begin_fill()
circle(10, 360)
end_fill()

move(-30, -50, "l", 0)

seth(10)
forward(40)
seth(120)
forward(50)
seth(240)
forward(50)
seth(180)
forward(50)
seth(-60)
forward(50)
seth(50)
forward(55)


done()
os.system("pause")
