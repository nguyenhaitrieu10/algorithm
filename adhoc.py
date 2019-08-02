
def find_strange_point(a):
    left = 0
    right = len(a) - 1
    margin = right
    find = -1
    while left <= right:
        mid = left + (right - left) // 2
        if mid < margin and a[mid] > a[mid + 1]:
            find = mid
            right = mid - 1
        elif a[mid] >= a[0]:
            left = mid + 1
        else:
            right = mid - 1

    return find


import search
def sea_search(a, value):
    strange = find_strange_point(a)
    if strange == -1: # increase sorted array
        return search.bsearch_first(a, 0, len(a) - 1, value)

    if value >= a[0]:
        return search.bsearch_first(a, 0, strange, value)

    return search.bsearch_first(a, strange + 1, len(a) - 1, value)
