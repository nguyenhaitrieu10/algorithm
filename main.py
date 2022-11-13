def sqrt(n):
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

n = 2
a = sqrt(n)
print(a)