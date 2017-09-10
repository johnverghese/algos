import math

def heapsort(a):
    heapify(a)

def heapify(a):
    for i in range(2**int(math.log(len(a), 2))):
        print( i)
        while a[i] > a[2*i+1] or a[i] > a[2*i+2]:
           percolate(a, i)


def percolate(a, i):
    print(i)
    print(a)
    #no children
    if len(a) < 2*i+2:
        return a
    #left child only
    elif len(a) == 2*i+2:
        if a[i] > a[2*i+1]:
            a[i], a[2*i+1] = a[2*i+1], a[i]
            return percolate(a, 2*i+1)
        else:
            return a
    else:
        if a[i] > a[2*i+1]:
            a[i], a[2*i+1] = a[2*i+1], a[i]
            return percolate(a, 2*i+1)
        elif a[i] > a[2*i+2]:
            a[i], a[2*i+2] = a[2*i+2], a[i]
            return percolate(a, 2*i+2)
        else:
            return a


heapify([9, 4, 7, 3, 6, 8, 10, 1])

