__author__ = 'dolek'


import collections
import sys

FACING = ['north','east','south','west']
laser = collections.namedtuple("orientation",['x','y','orinum','maxsum'])
def main():
    filename = input("please enter file name")

    try:
        newFile=open(filename)
    except FileNotFoundError:
        print("invalid")
        sys.exit(0)
    noOfLaser= input("input no of lasers")
    if noOfLaser.isalpha():
        sys.exit(0)
    myNewList=getFileList(newFile, noOfLaser)


def getFileList(file,no):
    mynewlist= []
    for line in file:
        x=line.strip()
        y=x.split(' ')
        mynewlist.append(y)
    return mynewlist

if __name__=='__main__':
    main()