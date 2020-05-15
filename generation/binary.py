n = 5

a = ["0"] * n
c = 0

while c < (2**n):
    s = "".join(a)
    print(s)

    i = n - 1
    while a[i] == "1":
        a[i] = "0"
        i -= 1
    a[i] = "1"
    c += 1

