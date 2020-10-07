# Ivana Zdravevska
# CS 100 2019F Section 039
# HW 03, September 15, 2019

import turtle
aScreen = turtle.Screen()
shelly = turtle.Turtle()
shelly.shape("turtle")

# equilateral triangle
shelly.fd(100)
shelly.left(120)
shelly.fd(100)
shelly.left(120)
shelly.fd(100)
shelly.left(120)

# square
shelly.reset()
shelly.fd(100)
shelly.left(90)
shelly.fd(100)
shelly.left(90)
shelly.fd(100)
shelly.left(90)
shelly.fd(100)
shelly.left(90)

# regular pentagon
shelly.reset()
shelly.fd(100)
shelly.left(120)
shelly.undo()
shelly.left(72)
shelly.fd(100)
shelly.left(72)
shelly.fd(100)
shelly.left(72)
shelly.fd(100)
shelly.left(72)
shelly.fd(100)
shelly.left(72)

# 2. Write code that uses turtle graphics to draw four concentric circles of radius 50,100,150,200
shelly.reset()
shelly.circle(50)
shelly.right(90)
shelly.penup()
shelly.fd(50)
shelly.left(90)
shelly.pendown()
shelly.circle(100)
shelly.right(90)
shelly.penup()
shelly.fd(50)
shelly.left(90)
shelly.pendown()
shelly.circle(150)
shelly.right(90)
shelly.penup()
shelly.fd(50)
shelly.left(90)
shelly.pendown()
shelly.circle(200)

turtle.Screen().bye()

# 3. Write code that uses the python math module to compute and print out the values:
# a)
import math
print("The factorial of 100 is: ")
print(math.factorial(100))
print(" ")


# b)
print("The log base 2 of 1000000 is: ")
print(math.log(1000000,2))
print(" ")


# c)
print("The greatest common divisor of 63 and 49 is: ")
print(math.gcd(63,49))

