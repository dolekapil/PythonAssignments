__author__ = 'dolek'

def SelectionSort(list):

    for counter in range(len(list)-1,0,-1):
        posOfMax = 0
        for i in range(1,counter+1):
            if list[i]>list[posOfMax]:
                posOfMax = i
        list[posOfMax],list[counter]=list[counter],list[posOfMax]
    return list
def main():
    list=SelectionSort([3,34,7,12,67,2,1])

    print(list)
if __name__ == '__main__':
    main()