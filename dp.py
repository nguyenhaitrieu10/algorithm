
def LCS(a, b):
    n = len(a)
    m = len(b)

    DP = [[0]*(m + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                DP[i][j] = DP[i-1][j-1] + 1
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])

    return DP[n][m]


