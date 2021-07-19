### From: https://stackoverflow.com/questions/54972470/python-turtle-module-using-onclick-to-make-turtle-disappear

import turtle
import time
import random
from random import uniform
import math
import tkinter
from tkinter import *


def close_window():
    window.destroy()



def onclick1():
    isClicked == True


def game():
    turtle.setup(2000,1080)
    wn = turtle.Screen()
    wn.title("Commands")
    Jimmy=turtle.Turtle()
    Jimmy.shape("circle")
    Jimmy.penup()
    numOfCircles = 0
    Jimmy.hideturtle()
    while numOfCircles < 20:
        xPos = uniform(-400,400)
        yPos = uniform(-400,400)
        #Jimmy.setpos(xPos, yPos)
        for i in range(1,5):
            Jimmy.onclick(onclick1())
            Jimmy.shapesize(i+3,i+5)
            Jimmy.showturtle()
            if(isClicked == True):
                Jimmy.hideturtle()
            time.sleep(.3)
        Jimmy.hideturtle()
        numOfCircles = numOfCircles + 1




def increaseSize():
    while turtlesize==(x,y)<=(20,5): 
        size = Jimmy.turtlesize()
        increase = tuple([10 * num for num in size])
        Jimmy.turtlesize(*increase)
        print(turtlesize)

isClicked = False
window = tkinter.Tk()
window.title("hello")
window.geometry("2000x1080")
label1 = tkinter.Label(window,bg = "green", font = "ArialMS 60 ",width=2000,height=100)
label2 = tkinter.Label(window, text = "Aim Booster", bg = "green", font = "ArialMS 60 ")
open_button = tkinter.Button(window, text = "Start",font = "Arial 36",width=10,height=1,command=game)
close_button = tkinter.Button(window, text = "EXIT",font = "Arial 10",width=5,height=2,command=close_window)

label1.pack()
label2.pack()
label1.place(x = 0, y = -100)

open_button.pack()
open_button.place(x = 650, y=500 )
close_button.pack()
close_button.place(x=10)

window.mainloop()
