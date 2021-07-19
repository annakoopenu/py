import turtle 
import random



#while True:
#    forward(200)
#    left(170)
#    if abs(pos()) < 1:
# 
#         break
### Class  Spirartle inherits Turtle
class Line_Random(Turtle):

    def __init__(self):
        """ Create a new Turtle as Spirala and rundomize it's 
            - starting position
            - pen color
            - width            
        """        

def line():

    turtle.penup()
    xx = random.randrange(-1 * int(screen.canvwidth/2), int(screen.canvwidth)/2)
    yy = random.randrange(-1 * int(screen.canvheight/2), int(screen.canvheight)/2)        
    turtle.setposition(xx,yy)  # positioning
    print('Starts at x: ', xx, ' y: ', yy)
    turtle.pendown()
    
    xx = random.randrange(-1 * int(screen.canvwidth/2), int(screen.canvwidth)/2)
    yy = random.randrange(-1 * int(screen.canvheight/2), int(screen.canvheight)/2)        
    print('Ends at x: ', xx, ' y: ', yy)
    turtle.goto(xx,yy) # draw the line

###
##  Main
###

#############
### Main
#############

width,height=600,600
    
screen = turtle.Screen()
screen.setup(width,height)
screen.delay(0)
screen.colormode(255)
screen.bgcolor(0,0,0)
screen.title ('Lines Lines Lines')

t_line = turtle.Turtle('circle')
#color('black', 'green')
t_line.color('red', 'yellow')
#turtle.begin_fill()
t_line.speed(7)

#for i in range(1):


line()
line()
line()


#turtle.end_fill()
turtle.done()