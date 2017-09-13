#####################################3
#Notes on merge sort:
# This sort should run in O(nlogn) time. The logn term comes from the merge_sort
# routine, which will run logn times, splitting the input in half each time. The
# merge routine will run in worst case n time, if we take n to be the combined
# size of the inputs. We're depending on the comparator function being properly
# implemented for the objects being compared.


def merge_sort(a):
    # base case
    if len(a) == 1:
        return a

    else:
        sorted_first_half = merge_sort(a[:len(a)//2])
        sorted_second_half = merge_sort(a[len(a)//2:])
        return merge(sorted_first_half, sorted_second_half)


def merge(a, b):
    merged = []
    i, j = 0, 0 
    while i <= len(a) and j <= len(b):
        if i == len(a):
            merged.extend(b[j:])
            j = len(b) + 1
        elif j == len(b):
            merged.extend(a[i:])
            i = len(a) + 1
        elif a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    return merged


