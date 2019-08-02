import random


def check_order(a, increase=True):
    l = len(a)
    for i in range(l-1):
        if (a[i] > a[i+1]) == increase:
            return False
    return True


def init_arr(length, min_value = -100, max_value=100):
    a = [0] * length

    for i in range(length):
        a[i] = random.randint(min_value, max_value)
    return a


def check_arr_increase(a):
    b = a.copy()
    b.sort()
    return b == a
