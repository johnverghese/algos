##############################
#Notes on quicksort:
# Quicksort runs in O(nlogn) time.
# The basic idea is to pick a pivot, and to then find its proper place in the
# sorted array by pushing everything smaller than the pivot to the left, and
# everything larger to the right. You can then recurse on the two sub-arrays
# thus created.

# This version picks the middle of the list as the pivot. This is a naive
# way of picking the pivot that can lead to sub-optimal results.


def partition(a):
    ##base case
    if len(a) <= 1:
        return a
        
    pivot_idx = len(a)//2
    pivot = a.pop(pivot_idx)
   
    left, right = [], []

    for el in a:
        if el < pivot:
            left.append(el)
        else:
            right.append(el)

    return partition(left) + [pivot] + partition(right)

def quicksort(a):
    return partition(a)
    
    
