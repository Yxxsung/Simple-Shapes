#Hello! This is the file for the Simple Shapes Assignment!
#Class: CGT 115 - Spring 2026
#Sophia Alexander      01/21/26

#For some reason, it will not let me change the branch to main. I think this is what is causing
#the commit and push issue, so I will update it to master and delete main like I did in the
#previous repository.

#import section
import turtle
import time

#Don't forget to add this line to create the 'turtle' from the import def
my_turtle = turtle.Turtle()

#defines the counter i
i= 0

#Function Section
def triangleside ():
    my_turtle.forward(150)
    my_turtle.right(120)
    #Last angle: 120 degrees

def hexagonside ():
    my_turtle.forward(100)
    my_turtle.right(60)
    #Last angle: 30 degrees

def octagonside ():
    my_turtle.forward(75)
    my_turtle.right(45)
    #Last angle: 20 degrees

#This specific function will draw the triangle using the triangleSide fucntion
def triangledraw ():
    #for some reason it wants the conter defined INSIDE the function *eyeroll*
    i = 0
    while i <= 2:
        triangleside()
        i = i+1


def hexagondraw ():
    i = 0
    while i <= 5:
        hexagonside()
        i = i+1


def octagondraw ():
    i = 0
    while i <=7:
        octagonside()
        i = i+1

#here is where we will call our functions in the order that we need them
triangledraw()

#creates a pause to help the viewer follow the 'turtle'
time.sleep(2)

my_turtle.penup()

my_turtle.left(90)

my_turtle.forward(200)

my_turtle.pendown()

hexagondraw()

time.sleep(2)

my_turtle.penup()

my_turtle.left(90)

my_turtle.forward(200)

my_turtle.pendown()

octagondraw()

#Assignment Complete!
