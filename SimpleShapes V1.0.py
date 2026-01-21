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
i = 0

#Function Section
def triangleSide ():
    my_turtle.forward(100)
    my_turtle.right(60)
    #Last angle: 45 degrees

def hexagonSide ():
    my_turtle.forward(100)
    my_turtle.right(30)
    #Last angle: 30 degrees

def octogonSide ():
    my_turtle.forward(100)
    my_turtle.right(45)
    #Last angle: 20 degrees

def triangleDraw ():
    while i < 3:
        triangleSide()
        i+1


#here is where we will call our functions in the order that we need them
triangleDraw()
