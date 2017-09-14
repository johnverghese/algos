


def radixsort(a):
    a = [str(el) for el in a]
    return bucketsort(a, 1)

def bucketsort(a, i):
    chars = [int(el[i]) for el in a]
    buckets = [[]] * (max(chars) + 1)
    a_sorted = []

    for el in a:
        el = int(el)
        buckets[el[i]].append(el)

    for i in range(len(buckets)):
        a_sorted.extend(buckets[i])

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
