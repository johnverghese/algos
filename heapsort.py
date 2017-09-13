##########################################
# Heapsort notes:
# 


import math

def heapsort(a):
    return heapify(a)

def heapify(a):
    for i in range(len(a)-1, -1, -1):
        percolate_down(a, i)
    return a

# restore the heap property of the tree rooted at a, 
#assuming that the subtrees of a are heaps
def percolate_down(a, i):
    root_idx = i
    while len(a) > 2*root_idx+1: #while at least one child
        if a[root_idx] > a[2*root_idx+1]:
            a[root_idx], a[2*root_idx+1] = a[2*root_idx+1], a[root_idx] 
            root_idx = 2*root_idx+1
        elif len(a) > 2*root_idx+2: # has right child 
            if a[root_idx] > a[2*root_idx+2]:
                a[root_idx], a[2*root_idx+2] = a[2*root_idx+2], a[root_idx]
                root_idx = 2*root_idx+2
            else: # both children are larger
                root_idx = len(a) # break
                
    return a

print(heapsort([9, 4, 7, 3, 6, 8, 10, 1]))

