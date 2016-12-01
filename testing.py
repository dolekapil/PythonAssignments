__author__ = 'dolek'
def checkPeriodic(bits, length):
    #fact = factors(length)
    #for n in fact:
    s = bits
    i = (s+s).find(s, 1, -1)
    if i == -1:
        pass
    else:
        return True
    return False

def factors(length):
    result = []
    for i in range(1, length):
        if length % i == 0:
            result.append(i)
    return result

print(checkPeriodic('0111011',3))