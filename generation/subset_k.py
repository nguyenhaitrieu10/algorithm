n = 5
k = 3

a = [i + 1 for i in range(k)]

while True:
    print(a)
    i = k - 1
    while i >= 0 and a[i] == n + i - k + 1:
        i -= 1

    if i < 0:
        break

    a[i] += 1
    j = i + 1
    while j < k:
        a[j] = a[j-1] + 1
        j += 1

