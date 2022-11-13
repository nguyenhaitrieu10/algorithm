
def sqrt(n, delta = 0.0001):
    result = n
    while abs(result * result - n) > delta:
        result = 0.5 * (result + n / result)
    return result

def sqrt2(n):
    left = 0
    right = n
    mid = (left+right) / 2
    while abs(mid**2 - n) > 0.0001:
        if mid**2 > n:
            right = mid
        else:
            left = mid
        mid = (left+right) / 2
    return mid