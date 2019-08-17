import math

def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    sqrt_n = int(math.sqrt(n) + 0.5)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_fractors(n):
    result = []

    assert n > 0

    if n == 1:
        return [[1, 1]]

    if n % 2 == 0:
        result.append([2, 1])
        n = n // 2
        while n % 2 == 0:
            result[-1][1] += 1
            n = n // 2

    sqrt_n = int(math.sqrt(n) + 0.5)

    i = 3
    while i < sqrt_n + 1:
        if n % i == 0:
            result.append([i, 1])
            n = n // i
            while n % i == 0:
                result[-1][1] += 1
                n = n // i
            sqrt_n = int(math.sqrt(n) + 0.5)
        i += 2

    if n > 2:
        result.append([n, 1])

    return result


from constants import MAXN
def compute_smallest_primes():
    sf = [i for i in range(MAXN + 1)]

    for i in range(4, MAXN + 1, 2):
        sf[i] = 2

    SQRT_MAXN = int(math.sqrt(MAXN) + 0.5)
    for i in range(3, SQRT_MAXN + 1, 2):
        if sf[i] == i:
            for j in range(i ** 2, MAXN + 1, i):
                if sf[j] == j:
                    sf[j] = i

    return sf

def prime_fractors_multy_query(n, sf=[]):
    if not sf:
        sf = compute_smallest_primes()

    assert n > 0
    if n == 1:
        return sf, [[1, 1]]

    result = []
    while n > 1:
        k = sf[n]
        result.append([k, 1])
        n = n // k

        while n % k == 0:
            result[-1][1] += 1
            n = n // k

    return sf, result



