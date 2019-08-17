def fast_power(n, k):
    result = 1

    while k > 0:
        if (k & 1) == 1:
            result *= n

        k = k >> 1
        n = n ** 2

    return result

print(fast_power(2, 5))
        