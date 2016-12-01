__author__ = 'dolek'


def BubbleSort(list):

    for counter in range(len(list)-1,0,-1):
        for i in range(counter):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
    return list



def main():
    list=BubbleSort([3,34,7,12,67,2,1])
    print(list)
if __name__ == '__main__':
    main()