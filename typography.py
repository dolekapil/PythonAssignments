__author__ = 'kmd1712'

"""
CSCI-603 (Lab 1): Computational problem solving Typography
Author: Kapil Dole (kmd1712@g.rit.edu)

This is a program that draws my own name. In the given program,
various functions been used that can be reused.
"""

import turtle

def init():

    """
    Initializing turtle pointer location for drawing to left of window.
    :pre: pos (0,0), heading (west), left
    :post: pos (-350,0), heading (east), right
    :return: None
    """

    turtle.up()
    turtle.left(180)
    turtle.forward(350)
    turtle.right(180)

def drawI():

    """
    Drawing character "I".
    :pre: (relative) pos (-350,0), heading (east), right
    :post: (relative) pos (-245,0), heading (east), right
    :return: None
    """

    turtle.down()
    turtle.forward(50)
    turtle.back(25)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(25)
    turtle.back(50)
    turtle.up()
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(30)

def drawA():

    """
    Drawing character "A".
    :pre: (relative) pos (-245,0), heading (east), right
    :post: (relative) pos (-165,0), heading (east), right
    :return: None
    """

    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.back(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.up()
    turtle.forward(30)

def drawM():

    """
    Drawing character "M".
    :pre: (relative) pos (-165,0), heading (east), right
    :post: (relative) pos (-60,0), heading (east), right
    :return: None
    """

    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(100)
    turtle.back(100)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(100)
    turtle.up()
    turtle.left(90)
    turtle.forward(30)

def drawK():

    """
    Drawing character "K".
    :pre: (relative) pos (-60,0), heading (east), right
    :post: (relative) pos (20,0), heading (east), right
    :return: None
    """

    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    turtle.back(50)
    turtle.right(45)
    turtle.forward(70.7)
    turtle.back(70.7)
    turtle.right(90)
    turtle.forward(70.7)
    turtle.up()
    turtle.left(45)
    turtle.forward(30)

def drawP():

    """
    Drawing character "P".
    :pre: (relative) pos (20,0), heading (east), right
    :post: (relative) pos (100,0), heading (east), right
    :return: None
    """

    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.back(50)
    turtle.left(90)
    turtle.up()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(30)


def drawL():

    """
    Drawing character "L".
    :pre: (relative) pos (100,0), heading (east), right
    :post: (relative) pos (205,0), heading (east), right
    :return: None
    """

    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    turtle.back(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.up()
    turtle.forward(30)

def drawName():

    """
    The main function for drawing name.
    :pre: pos (0,0), heading (east), right
    :post: pos (0,0), heading (east), right
    :return: None
    """

    init()
    drawI()
    turtle.forward(25)
    drawA()
    drawM()
    turtle.forward(25)
    drawK()
    drawA()
    drawP()
    drawI()
    drawL()
    turtle.forward(25)
    turtle.hideturtle()
    input('Press enter to close...')

if __name__ == '__main__':
    drawName()


