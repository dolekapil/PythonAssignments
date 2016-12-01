__author__ = 'dolek'

def InsertionSort(list):

    for counter in range(1, len(list)):
        val = list[counter]
        index = counter

        while index > 0 and list[index-1] > list[index]:
            list[index] = list[index-1]
            index -= 1
        list[index] = val
    return list

def main():
    list = InsertionSort([3,1,45,12,6,9])
    print(list)
if __name__ == '__main__':
    main()