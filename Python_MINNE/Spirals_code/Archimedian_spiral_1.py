"""
Based on # https://github.com/AllenDowney/ThinkPython - page 36
Draws an Archimedean spiral
"""
import turtle
import math

def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them.  t is a turtle.
    """
    for i in range(n):
        t.forward(length)
        t.left(angle)

def square(t, length):
    """Draws a square with a given side length 
    """
    for i in range(4):
        t.forward(length)
        t.right(90)

def polygon(t, n, length):
    """Draws an n sides polygon with a given side length 
    """
    ang = 360/n
    for i in range(n):
        t.forward(length)
        t.right(ang)

def circle(t, r):
    """Draws aproximal circle with a given radius r 
    """
    circumference = 2 * math.pi * r
    n = 60
    side =  circumference / 60

    t.circle(r)
    t.pencolor('red')
    polygon(t, n, side)

def arc(t, r, angle):
    """Draws aproximal arc with a given radius r and part of the arc defined ny angle
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1     #helps make the curve smuth in effective way
    step_length = arc_length / n
    step_angle = float(angle) / n
    
    t.pencolor('green')
    
    polyline(t, n, step_length, step_angle)   


def spiral(t):
    """Draws Archimedian spiral by drawing 360 arcs each one is 1/4 of a circle each 1/4 becoming 1 unit bigger.
    Check out more about https://en.wikipedia.org/wiki/Archimedean_spiral
    """
    for i in range(36):
        arc(t, 7*i, 90)

#############
### Main
#############

width,height=600,600
    
screen = turtle.Screen()
screen.setup(width,height)
screen.delay(0)
screen.colormode(255)
screen.bgcolor(0,0,0)
screen.title ('Archimedian_spiral')


t1 = turtle.Turtle()  
t1.shape('circle')

t1.color('blue','black')
t1.begin_fill()

spiral(t1)

turtle.done()