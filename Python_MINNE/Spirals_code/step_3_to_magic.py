### import 
import random
from turtle import *

### Class  Spirartle inherits Turtle
class Spirartle(Turtle):

    def __init__(self):
        """ Create a new Turtle as Spirala and rundomize it's 
            - starting position
            - pen color
            - width            
        """        
        Turtle.__init__(self,shape='circle')
        self.penup()
        #setRandomColor(self)
        """ set Width """        
        self.width(random.randrange(1,12))
        """ set heading """        
        self.setheading(random.randrange(1,360))

        #self.setRandomPosition()
        
        self.pendown()    

    def setRandomColor():
        """ set Color """
        rrr = random.randrange(0,77)
        ggg = random.randrange(0,77)
        bbb = random.randrange(110,255)
        self.color = (rrr, ggg, bbb)

    def setRandomPosition():
        """ be ready at your position"""
        xx = random.randrange(-1 * int(screen.canvwidth/2), int(screen.canvwidth)/2)
        yy = random.randrange(-1 * int(screen.canvheight/2), int(screen.canvheight)/2)
        self.goto(xx,yy) # positioning

    def drawMe(self):
        """
        """
        for i in range(33):
            self.forward(20+i)
            self.left(30 - i/1.6)                           
        
    def myColor(self):
        return self.color       


def h1():
    print('pressseddd')

#####################################
######################## Main 
width,height=600,600
    
screen = Screen()
screen.setup(width,height)
screen.delay(0)
screen.colormode(255)
screen.bgcolor(0,0,0)
screen.title ('Random color spirals')
#startx = -150
#starty = 150 

s1 = Spirartle()
s2 = Spirartle()
s3 = Spirartle()
s4 = Spirartle()
s5 = Spirartle()
#s6 = Spirartle()
#s7 = Spirartle()

#s1.drawMe()
#s2.drawMe()
s3.drawMe()
s4.drawMe()
s5.drawMe()


#screen.onclick(s3.drawMe())
#ttt = screen.turtles()
#ttt[1].reset()


#screen.onclick(s1.drawMe())
#screen.onclick(s2.drawMe())

screen.onkeypress(s3.reset(), "Up")
screen.onkeypress(s4.reset(), "Down")

screen.onscreenclick(goto(0,0))
screen.listen()
screen.mainloop()