
def linear_search(a, value):
    l = len(a)
    for i in range(a):
        if a[i] == value:
            return i
    return -1


def bsearch(a, left, right, value):
    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] == value:
            return mid
        if a[mid] > value:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def binary_search(a, value):
    right = len(a) - 1
    left = 0
    return bsearch(a, left, right, value)


def bsearch_first(a, left, right, value):
    find = -1
    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] == value:
            find = mid
            right = mid - 1
        if a[mid] > value:
            right = mid - 1
        else:
            left = mid + 1

    return find


def binary_search_first_element(a, value):
    right = len(a) - 1
    left = 0
    return bsearch_first(a, left, right, value)






