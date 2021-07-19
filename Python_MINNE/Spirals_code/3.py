# import 
import turtle
import random

### Functions ######################################
####################################################
def spiralaaa(x,y):
    turtle.penup() 
    turtle.setposition(x,y)
    turtle.pendown()
    spiralaa()
    
def spiralasBlues():
    """ Draws a spiral on a turtle Screen with random Starting point, Color and Width 
    """
                # Random color
    turtle.penup()            
    turtle.pencolor(random.randrange(0,33),random.randrange(0,77),random.randrange(150,220))
                # Random width
    turtle.width(random.randrange(2,13))
                # Random direction
    turtle.setheading(random.randrange(1,360))
    
    turtle.begin_fill()
    print('Color: ', turtle.pencolor(), ' Heading: ', turtle.heading())
    
    turtle.pendown()
    for i in range(37):
        turtle.forward(20+i)
        turtle.left(30 - i/1.5)
    turtle.end_fill()

def spiralasReds():
    """ Draws a spiral on a turtle Screen with random Starting point, Color and Width 
    """
                # Random color
    turtle.penup()            
    turtle.pencolor(random.randrange(150,200),random.randrange(0,77),random.randrange(0,33))
                # Random width
    turtle.width(random.randrange(4,17))
                # Random direction
    turtle.setheading(random.randrange(1,360))

    turtle.setposition(random.randrange(0,turtle.screensize()[0]), random.randrange(0,turtle.screensize()[1]))
    
    turtle.begin_fill()
    print('Color: ', turtle.pencolor(), ' Heading: ', turtle.heading())
    
    turtle.pendown()
    for i in range(37):
        turtle.forward(20+i)
        turtle.left(30 - i/1.5)
    turtle.end_fill()

### Main code #######################################
#####################################################

# color mode & screen color
turtle.colormode(255) 
turtle.bgcolor(0,0,0)   # background color - black
#turtle.pencolor(255, 200, 175)
turtle.pencolor(200, 0, 20)

turtle.speed(0) # turtle speed to slowest

turtle.penup()
turtle.setposition(0,0)
turtle.pencolor(200, 0, 20)
turtle.pendown()

#yy = random.randrange(0,turtle.screensize[0])
#print(yy)

# draw 70 spirals
for i in range(1170):
    spiralasBlues()
    if i % 10 == 0:
        spiralasReds()


   


# allow user to click           # for some action
#
# turtle.onscreenclick(spiralaaa)

turtle.done()