__author__ = 'kmd1712'
import turtle
import random

def init():
    trees = int(input("Enter total number of trees to draw "))
    house = input("Do you need house in forest ?, press y/n ")
    turtle.penup()
    turtle.setposition(-330,-100)
    if(trees == 0 and house == "y"):
        drawHouse()
        maxHeight = 150
    else:
        maxHeight = drawTrees(trees, house)
    turtle.penup()
    turtle.left(90)
    turtle.forward(maxHeight + 10)
    drawStar()
    turtle.hideturtle()
    input("Press enter to exit")

def drawStar():
    turtle.pendown()
    turtle.forward(30)
    turtle.back(15)
    turtle.right(90)
    turtle.back(15)
    turtle.forward(30)
    turtle.back(15)
    turtle.left(45)
    turtle.forward(15)
    turtle.back(30)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.back(30)
    turtle.forward(15)


def drawHouse():
        turtle.pendown()
        turtle.left(90)
        turtle.forward(100)
        turtle.right(45)
        turtle.forward(50*(2**.5))
        turtle.right(90)
        turtle.forward(50*(2**.5))
        turtle.right(45)
        turtle.forward(100)
        turtle.left(90)
        turtle.back(100)
        turtle.forward(100)

def spaceBetween(treenumber,totaltree):

    if treenumber < totaltree-1:
        turtle.forward(100)
    turtle.penup()


def drawTrees (trees, decision):
    maxheight = 150
    for counter in range(0, trees):

        if counter+1 == trees and decision == "y":
            drawHouse()
            turtle.forward(100)


        which = random.randint(1, 3)
        if which == 1:
            height = drawPine(random.randint(50, 200), counter, trees)

        elif which == 2:
            height = drawMaple(random.randint(50, 150), counter, trees)

        else:
            height = drawMyTree(random.randint(50, 100), counter, trees)

        if height > maxheight:
            maxheight = height
    return maxheight

def drawMyTree(trunk,treenumber,totaltree):
    drawTrunk(trunk)
    turtle.right(60)
    turtle.forward(30)
    turtle.left(60)
    turtle.forward(60)
    turtle.left(60)
    turtle.forward(30)
    turtle.left(60)
    turtle.forward(30)
    turtle.left(60)
    turtle.forward(60)
    turtle.left(60)
    turtle.forward(30)
    turtle.right(60)
    turtle.forward(trunk)
    turtle.left(90)
    spaceBetween(treenumber,totaltree)
    height = trunk + (30 * (3 ** .5) + 60)
    return height

def drawMaple(trunk,treenumber,totaltree):
    drawTrunk(trunk)
    turtle.penup()
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.pendown()
    turtle.circle(40)
    turtle.penup()
    turtle.back(trunk+40)
    turtle.right(90)
    turtle.back(40)
    turtle.pendown()
    spaceBetween(treenumber,totaltree)
    height = trunk + 80
    return height

def drawPine(trunk,treenumber,totaltree):
    drawTrunk(trunk)
    turtle.left(90)
    turtle.forward(35)
    turtle.right(120)
    turtle.forward(70)
    turtle.right(120)
    turtle.forward(70)
    turtle.right(120)
    turtle.forward(35)
    turtle.left(90)
    turtle.forward(trunk)
    turtle.left(90)
    spaceBetween(treenumber,totaltree)
    height = trunk + (3**.5)*35
    return height

def drawTrunk(trunk):
    turtle.pendown()
    turtle.left(90)
    turtle.forward(trunk)

if __name__ == '__main__':
    init()
