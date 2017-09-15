# This version of the algorithm is O(k(n + blogb)), which is slightly worse than
# radix sort's ideal implementation: O(k(n + b)). I think that it's possible the
# ease of implementing in a strongly typed language like python makes this
# (using a dict) an attractive option, but this is worth revisiting.


# works only for a list of integers of the same length
def radixsort(a):
    a = [str(el) for el in a]
    #O(n)
    #O(k(n + blogb) where k is string length)
    for i in range(max([len(el) for el in a])-1, -1, -1):
        a = bucketsort(a, i)
    return a

#O(n + blogb)
def bucketsort(a, i):
    chars = [el[i] for el in a]
    buckets = {}
    a_sorted = []

    #O(n)
    for el in a:
        buckets.setdefault(el[i], []).append(el)

    #blogb where b is number of digit values
    for key in sorted(buckets.keys()):
        a_sorted.extend(buckets[key])

    return a_sorted
 
#only works for integers < 10
def bucketsort_(a):
    buckets = [0] * (max(a) + 1)
    a_sorted = []

    for el in a:
        buckets[el] += 1

    for i in range(len(buckets)):
        a_sorted.extend([i] * buckets[i])

    return a_sorted
        
print(radixsort([31, 42, 18, 21, 53, 22, 25, 20, 91, 17]))
