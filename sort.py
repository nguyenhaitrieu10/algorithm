import random

def heapify(a, n, i):
    tmp = a[i]
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        max_value = tmp
        if left < n and a[left] > max_value:
            largest = left
            max_value = a[left]

        if right < n and a[right] > max_value:
            largest = right
            max_value = a[right]

        if i != largest:
            a[i] = max_value
            i = largest
        else:
            a[i] = tmp
            break



def heap_sort(a):
    n = len(a)

    for i in range(n // 2 -1, -1, -1):
        heapify(a, n, i)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)

    return a


def quick_sort(a):
    left = 0
    right = len(a) - 1
    qsort(a, left, right)


def qsort(a, left, right):
    if left >= right:
        return

    key = a[(left + right) // 2]
    i = left
    j = right
    while i <= j:
        while a[i] < key:
            i += 1
        while a[j] > key:
            j -= 1

        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    qsort(a, left, j)
    qsort(a, i, right)

def merge_sort(a, left, right):
    if left >= right:
        return

    mid = (right + left) // 2
    merge_sort(a, left, mid)
    merge_sort(a, mid + 1, right)

    tmp = [0] * (right - left + 1)

    l1 = left
    r1 = mid
    l2 = mid + 1
    r2 = right
    i = l1
    j = l2
    p = 0

    while i <= r1 and j <= r2:
        if a[i] < a[j]:
            tmp[p] = a[i]
            i += 1
        else:
            tmp[p] = a[j]
            j += 1
        p += 1

    while i <= r1:
        tmp[p] = a[i]
        i += 1
        p += 1

    while j <= r2:
        tmp[p] = a[j]
        j += 1
        p += 1

    for i in range(0, right - left+ 1):
        a[i + left] = tmp[i]


def check_order(a, increase=True):
    l = len(a)
    for i in range(l-1):
        if (a[i] > a[i+1]) == increase:
            return False
    return True

def init_arr(a, min_value = 0, max_value=100):
    l = len(a)
    for i in range(l):
        a[i] = random.randint(min_value, max_value)
    return a
