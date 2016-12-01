import sys
import math

num = 1

for i in range(num):
    count = 6959712971461184279
    gameCounter = 0
    while count != 1:
        counter = 1
        found = False
        while(not found):
            if(int(math.pow(2,counter))==count):
                count = count //2
                found = True
                gameCounter+=1
            elif(int(math.pow(2,counter))<count):
                counter+=1
            else:
                count = counter - 1
                found = True
                gameCounter+=1
    if(gameCounter%2==0):
        print("Richard")
    else:
        print("Louise")
                