# Ivana Zdravevska
# CS 100 2019F Section 039
# HW 04, September 19, 2019

# 1.

a=3
b=4
c=5

if a < b:
    print("OK")
elif c < b:
    print("OK")
elif (a+b)==c:
    print("OK")
elif ((a**2)+(b**2))==(c**2):
    print("OK")
else:
    print("NOT OK")


# 2.

import turtle

aScreen = turtle.Screen()
shelly = turtle.Turtle()

length = None
while not length:
    try:
        length = float(input('Enter your turtle line length: '))
    except ValueError:
        print('Sorry, try again. You need to enter a number')

width = None
while not width:
    try:
        width = int(input('Enter your turtle line width: '))
    except ValueError:
        print('Sorry, try again. You need to enter a positive integer')
    else:
        if width < 1:
            print('Sorry, try again. You need to enter a positive integer')
            width = None

color = None
while not color:
    color = input('Enter your turtle line color: ')
    try:
        shelly.pencolor(color)
    except:
        print('Sorry, try again. You need to enter a different color.')
        color = None

shape = None
while not shape:
    shape = input('What shape do you want: a line, triangle, or square: ')
    if shape.lower() not in ['line', 'triangle', 'square']:
        shape = None
        print('Sorry, try again. Enter either line, triangle, or square.')


shelly.pensize(width)
if shape.lower() == 'line':
    shelly.forward(length)
elif shape.lower() == 'triangle':
    shelly.forward(length)
    shelly.right(120)
    shelly.forward(length)
    shelly.right(120)
    shelly.forward(length)
else:
    shelly.forward(length)
    shelly.right(90)
    shelly.forward(length)
    shelly.right(90)
    shelly.forward(length)
    shelly.right(90)
    shelly.forward(length)

aScreen.exitonclick()

