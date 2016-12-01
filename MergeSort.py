
import sys
import math

def InsertionSort(list):
    for counter in range(1, len(list)):
        val = list[counter]
        index = counter
        while index > 0 and list[index-1] > val:
            list[index] = list[index-1]
            index -= 1
        list[index] = val
    return list


def BucketSort(list):
    n = len(list)
    buckets = [[] for counter in range(n)]
    for counter in range(n):
        loc = math.floor(n*list[counter])
        buckets[loc].append(list[counter])

    for counter in range(n):
        res = InsertionSort(buckets[counter])
        buckets[counter] = res

    result = []

    for counter in range(n):
        if len(buckets[counter]) > 0:
            result.extend(buckets[counter])

    return result


def MergeSort(list):
    if len(list) < 2:
        return list
    else:
        mid = len(list)//2
        leftHalf = MergeSort(list[:mid])
        rightHalf = MergeSort(list[mid:])
        return Merge(leftHalf, rightHalf)

def Merge(left, right):
    leftPtr = 0
    rightPtr = 0
    result = []
    while leftPtr < len(left) and rightPtr < len(right):
        if left[leftPtr] < right[rightPtr]:
            result.append(left[leftPtr])
            leftPtr += 1
        else:
            result.append(right[rightPtr])
            rightPtr += 1
    if leftPtr < len(left):
        result.extend(left[leftPtr:])
    elif rightPtr < len(right):
            result.extend(right[rightPtr:])
    return result

def main():
    n = int(input().strip())
    list = []
    for counter in range(n):
        list.append(float(input().strip()))

    print(MergeSort(list))
    print(InsertionSort(list))
    print(BucketSort(list))

if __name__ == '__main__':
    main()