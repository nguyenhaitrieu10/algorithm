
def sqrt(n, delta = 0.0001):
    result = n
    while abs(result * result - n) > delta:
        result = 0.5 * (result + n / result)
    return result