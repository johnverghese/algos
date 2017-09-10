

def insertion_sort(a):
    for i in range(1, len(a)):
        el = a.pop(i)
        for j in range(i):
            if el <= a[j]:
                a.insert(j, el)
                break
            elif j == i-1:
                a.insert(i, el)

    return a
            
