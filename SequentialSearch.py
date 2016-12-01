
COUNT =0
def OrdSeqSer(list,value):
    global COUNT
    first =0
    last = len(list)-1

    found =False
    while first<=last and not found:
        print(COUNT)
        COUNT = COUNT+1
        mid = first+last//2
        if list[mid]== value:
            found = True
        else:
            if list[mid]<value:
                first = mid +1
            else:
                last =mid-1
    return found


def main():
    print(OrdSeqSer([3,5,7,9,17,79],79))


if __name__ == '__main__':
    main()