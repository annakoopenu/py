import random
from turtle import *


### import turtle

#wn = turtle.Screen()
#wn.title('Chudesnye spirali')
#wn.bgcolor('black')
#wn.setup(width=800, height=600)
#wn.tracer()

#spirala1 = turtle.Turtle()
#spirala2 = turtle.Turtle()
#spirala3 = turtle.Turtle()

#spirala1.setposition(100,0)
#spirala2.setposition(0,0)
#spirala3.setposition(-100,0)

#spirala1.pencolor('red')
#spirala2.pencolor('green')
#spirala3.pencolor('blue')

#spirala1.forward(20)
#spirala2.forward(50)
#spirala3.forward(70)

#spirala1.onclick
#####################################


class Spirartle(Turtle):

    def __init__(self,position):
        """ Create a new Turtle as Spirala and rundomize it's 
            - starting position
            - pen color
            - width            
        """        
        Turtle.__init__(self,shape='triangle')
        rrr = random.randrange(0,255)
        ggg = random.randrange(0,77)
        bbb = random.randrange(150,255)
        color = (rrr, ggg, bbb)
        self.color(color) # set color
        self.goto(position) # positioning

    def onclick(self):
        self.color = (200,0,0)
        self.setposition = self.position - 70   

#####################################
######################## Main 
width,height=600,600
    
screen = Screen()
screen.setup(width,height)
screen.delay(0)
screen.colormode(255)
screen.bgcolor(0,0,0)
screen.title ('Random color triangles')
startx = -150
starty = 150 
for row in range(4):
    for col in range(4):
        xcor = startx + col * 100
        ycor = starty - row * 100
        Spirartle((xcor,ycor))
            
done()