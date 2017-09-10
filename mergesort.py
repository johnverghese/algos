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


print(merge_sort([9,4,7,3,5,8,10,1]))
