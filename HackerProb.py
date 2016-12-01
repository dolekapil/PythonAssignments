import sys
import itertools

def main():
    n = int(sys.stdin.readline())
    for count in range(n):
        myList = [int(num) for num in sys.stdin.readline().strip().split(' ')]        
        bits = sys.stdin.readline().strip()
        processInput(myList, bits)
        
def checkPeriodic(bits):
    i = (bits+bits).find(bits, 1, -1)
    if i == -1:
        return False
    else:
        return True

def processInput(myList, bits):
    count = 0
    length = myList[0]
    comb = myList[1]
    comList = [int(i) for i in range(length)]
    bitsList = [(bit) for bit in bits]
    
    if checkPeriodic(bits) == False:
        count+=1
    
    for j in range(1,comb+1):
        for subset in itertools.combinations(comList, j):
            for ec in subset:
                if bitsList[ec] == '1':
                    bitsList[ec]='0'
                else:
                    bitsList[ec]='1'
            newBits = ''.join(bitsList)
            if checkPeriodic(newBits) == False:
                count+=1    
            bitsList = [bit for bit in bits]
    print(count)
            
if __name__ =='__main__':
    main()