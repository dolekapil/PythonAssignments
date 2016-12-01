__author__ = 'dolek'

def QuickSort(list):
    Help(list,0,len(list)-1)
    print(list)
def Help(list,start,end):

    if start<end:
        par = partition(list,start,end)
        Help(list,start,par-1)
        Help(list,par+1,end)
def partition(list,start,end):
    pivot =start
    leftMark = start+1
    rightMark = end

    done = False

    while not done:
        while leftMark<=rightMark and list[pivot]>list[leftMark]:
            leftMark +=1
        while rightMark>=leftMark and list[pivot]<list[rightMark]:
            rightMark-=1
        if leftMark>rightMark:
            done =True
        else:
            list[leftMark],list[rightMark]=list[rightMark],list[leftMark]
    list[pivot],list[rightMark]=list[rightMark],list[pivot]
    return rightMark




def main():
    list = QuickSort([2,87,32,54,1,5,98])
    #print(list)
if __name__ == '__main__':
    main()