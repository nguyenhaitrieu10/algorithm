
def gcd(a, b):
    while b:
        a, b = b, a%b

    return a

def lcm(a, b):
    assert a != 0
    assert b != 0

    _gcd = gcd(a, b)
    
    return a * b // _gcd

def fast_power(n, k):
    result = 1

    while k > 0:
        if (k & 1) == 1:
            result *= n

        k = k >> 1
        n = n ** 2

    return result