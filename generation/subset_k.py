n = 5
k = 3

a = [i + 1 for i in range(k)]

while True:
    print(a)
    i = k - 1
    while i > -1 and a[i] == n + i - k + 1:
        i -= 1

    if i > -1:
        a[i] += 1
        j = i + 1
        while j < k:
            a[j] = a[j-1] + 1
            j += 1
    else:
        break

