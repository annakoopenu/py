
# next step
# import
import turtle
import random

# color mode & screen color
turtle.colormode(255)
turtle.bgcolor(0,0,0)   # background color - black

def spirala(t):
    """
	Draws a spiral with a given tartle object (t)
	Starting point is random 
    Color is random blue
    Width is random
    """
    t.penup()
    t.setx(random.randrange(-200,200))
    t.sety(random.randrange(-200,200))
    t.pencolor(random.randrange(0,255),random.randrange(0,255),200)
    t.width(random.randrange(2,13))
    t.pendown()

    for i in range(120):
    	t.forward(20+i)
    	t.left(30 - i/1.5)
# -- end of spirala(t)

def spiralaa(x,y):
    """
	Draws a spiral with a given tartle object (t)
	Starting point is random 
    Color is random blue
    Width is random
    """
    #print('inside')
    #turtle.setx(x)
    #turtle.sety(y)
    #t.pendown()
    turtle.home()
                # Random color
    turtle.pencolor(random.randrange(0,255),random.randrange(0,255),200)
                # Random width
    turtle.width(random.randrange(2,13))
                # Random direction
    turtle.setheading(random.randrange(1,360))

    for i in range(70):
    	turtle.forward(20+i)
    	turtle.left(30 - i/1.5)
# -- end of spirala(t)

def turn(x,y):
    t2.left(70)
    t2.forward(77)

#def draw_random_spirala():
        

#####################
  ###   Main      ###
#####################

# init turtle
wn = turtle.Screen()
# some motion
turtle.write('Hellœ', font=18)
turtle.speed(1)
turtle.forward(200) 
#spiralaa(turtle.xcor(),turtle.ycor())

#print(turtle.getpen())
#turtle.pencolor('blue') 
#turtle.penup()
#turtle.home()
#turtle.pendown()
turtle.onclick(spiralaa)
#turtle.forward(100)
#turtle.onclick(spiralaa)

#t1 = turtle.Turtle()
#t1.speed(0)
#t1.shape('circle')
#spirala(t1)

#ttt = turtle.Turtle()
#spirala(ttt)

#ttt.onclick(spiralaa)
#ttt.onclick(spiralaa)
#ttt.onclick(spiralaa)


#t2 = turtle.Turtle()
#t2.shape('turtle')
#t2.pencolor('red')
#t2.forward(100)

#t2.onclick(turn)
#t2.forward(200)

#t1.onclick(spirala)

#Drawing 3 spirals with random position, color and width
#for z in range(3):
#    spirala(t1)

# https://pythonprogramminglanguage.com/user-input-python/
#name = input("Enter a name: ")
#print(name)    

turtle.done()
