"""
CSCI-603: Lab 3
Author-1: Kapil Dole (kmd1712@g.rit.edu)
Author-2: Pratik kulkarni (psk7534@g.rit.edu)

This program draws a recursive tree based on the inputs given by user. It takes 4 inputs from user which are:
1. levels of recursion, a positive integer which determines depth of our recursive function.
2. Height of the tree, a positive integer which is height of tree and based of height of tree we determine
size of trunk which goes to our recursive function for drawing tree.
3. bushiness, this is floating point parameter between 0 and 1, which determines how many branches will come out
at the last level of recursion and how often they pop out. 0 is minimum value and 1 is maximum.
4. leafiness, this is also floating point parameter between 0 and 1, which decides probability of drawing leaves at
the end of sub branches. bigger the number, higher the chances of leaf appearing at the end of sub branch.
0 is minimum value and 1 is maximum.
every time you run the program, different tree will appear even the parameters you are passing are same, as we are
randomly displaying sub branches and leaves. At the last of the program, it will print total number of leaves on the
given tree and asks user to press enter for finishing the program.
"""

import turtle
import math
import random
import sys

leafCount = 0

def main():

    """
    The main method. It takes input from the user and draws tree according to the
    preference of the user and displays total number of leaves on given tree.
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (north), up
    :return: None
    """

    (layers, treeHeight, bushiness, leafiness) = takeInput()
    trunkHeight = getTrunkHeight(layers, treeHeight)
    drawGround(trunkHeight)
    drawTree(layers, trunkHeight, bushiness, leafiness)
    turtle.hideturtle()
    print("\nTotal number of leaves on tree are "+str(leafCount))
    input("\nPress enter to finish.")

def takeInput():

    """
    This method takes input from the user, validates the input and if input is
    right it will return a tuple of the input preferences.
    If any of the input is invalid then it will print an error message and
    program will terminate.

    :return:  tuple in format (layers(int), treeHeight(int), bushiness(float),
                                leafiness(float))
    """

    global leafCount
    layers = input("Please enter number of layers for our recursive tree.\n")
    if layers.isdigit() and int(layers) >= 0:
        layers = int(layers)
    else:
        print("Invalid input, numeric value expected.")
        sys.exit(0)
    treeHeight = input("Enter overall expected height of tree in pixels.\n")
    if treeHeight.isdigit() and int(treeHeight) > 0:
        treeHeight = int(treeHeight)
    else:
        print("Invalid input, numeric value expected.")
        sys.exit(0)
    bushiness = input("Enter Bushiness parameter in between 0 to 1, with 0 being lowest and 1 being highest.\n")
    if not bushiness.isalpha():
        bushiness = float(bushiness)
        if not (bushiness >= 0 and bushiness <= 1):
            print("Invalid input, floating value between 0 and 1 expected.")
            sys.exit(0)
    else:
        print("Invalid input, numeric value expected.")
        sys.exit(0)
    bushiness = math.ceil(bushiness * 5)
    leafiness = input("Enter leafiness parameter in between 0 to 1, with 0 being lowest and 1 being highest.\n")
    if not leafiness.isalpha():
        leafiness = float(leafiness)
        if not (leafiness >= 0 and leafiness <= 1):
            print("Invalid input, floating value between 0 and 1 expected.")
            sys.exit(0)
    else:
        print("Invalid input, numeric value expected.")
        sys.exit(0)
    leafiness = math.ceil(leafiness * 10)
    return(layers, treeHeight, bushiness, leafiness)



def drawGround(trunkHeight):

    """
    This function basically draws ground for tree which is in proportion to
    its trunk size. It will take trunk size of tree as input to draw the ground.
    :pre: (relative) pos (0,0), heading (east), right
    :post: (relative) pos (0,trunkHeight/2), heading (east), right
    :param: trunkHeight: height of the trunk.
    :return: None
    """

    turtle.up()
    turtle.setposition(0, -250)
    turtle.down()
    turtle.forward(trunkHeight/2)
    turtle.back(trunkHeight)
    turtle.forward(trunkHeight/2)
    turtle.left(90)
    turtle.pensize(3)
    turtle.speed(0)


def drawTree(layers, height, bushiness, leafiness):

    """
    This function is used for drawing recursive tree.
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (north), up
    It will take 4 parameters as input,
    :param: layers (Numeric value) - Total number of layers for our recursion tree.
    :param: height (Positive integer) - Height of the trunk of the tree.
    :param: bushiness (floating value between 0 and 1) - This parameter will decide how many
    branches will pop out at the last level of recursion and how often sub branches will
    appear. So, bigger the bushiness input, more sub branches will pop out at the end of
    branch. 0 is the lowest value and 1 is highest value for bushiness.
    :param: leafiness (floating value between 0 and 1) - This parameter will decide, whether
    to draw leaves at the end of each sub branch or not. So, bigger value means, more
    probability that leaf will pop out at the end of the last sub branch. Again,
    0 is the lowest value and 1 is highest value for leafiness.
    :return: None
    """

    turtle.pencolor("brown")
    if bushiness != 0:
        baseAngle = 25 + 20 * bushiness
        branchAngle = (2 * baseAngle)/bushiness
    else:
        baseAngle = 45
        branchAngle = 90
    if layers > 0:
        turtle.forward(height)
        turtle.left(baseAngle)
        turtle.pensize(1)
        drawTree(layers-1, height/2, bushiness, leafiness)

        if bushiness != 0:
            for counter in range(bushiness):
                turtle.right(branchAngle)
                if layers == 2:
                    if random.randint(0, 1) == 1:
                        drawTree(layers-1, height/2, bushiness, leafiness)

                else:
                    drawTree(layers-1, height/2, bushiness, leafiness)
                    if layers == 1:
                        if random.randint(1, 11) <= leafiness:
                            drawLeaf(height/math.pow(2, layers))
                            turtle.pencolor("brown")
        else:
            turtle.right(branchAngle)
            drawTree(layers-1, height/2, bushiness, leafiness)
            if layers == 1:
                if random.randint(1, 11) <= leafiness:
                    drawLeaf(height/math.pow(2, layers))
                    turtle.pencolor("brown")
        turtle.left(baseAngle)
        turtle.back(height)



def getTrunkHeight(layers, treeHeight):

    """
    This method will return possible height of the trunk of the tree depending
    upon number of layers user wants and maximum height of the tree as specified
    by user. This trunk height will be used to draw the trunk and according to
    that branches will be drawn.

    :param layers:      number of layers
    :param treeHeight:  maximum height of the tree
    :return: height of the trunk
    """

    counter = 1
    trunkHeight = counter
    for counter in range(1, layers):
        trunkHeight = trunkHeight + 1/(2*counter)
    trunkHeight = 1/trunkHeight
    trunkHeight = trunkHeight * treeHeight
    return trunkHeight


def drawLeaf(leafSize):

    """
    This function will draw the leaves. The leaves will be green in color and
    they will be filled in green color. The leaves drawn by this method will
    shape of the spade.
    :param leafSize: Size of the side of the spade(leaf)
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (north), up
    :return: None
    """

    global leafCount
    turtle.pencolor("green")
    turtle.fillcolor("green")
    turtle.right(45)
    turtle.begin_fill()
    for counter in range(4):
        turtle.forward(leafSize)
        turtle.left(90)
    turtle.left(45)
    turtle.end_fill()
    leafCount = leafCount + 1

if __name__ == '__main__':
    main()


