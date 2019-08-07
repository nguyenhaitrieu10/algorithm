
def is_palin(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def max_palin_o3(s):
    l = len(s)
    if l < 2:
        return l

    max_length = 1
    start = 0
    end = 0
    for i in range(l - 1):
        for j in range(i+1, l):
            if is_palin(s, i, j):
                if max_length < j - i + 1:
                    max_length = j - i + 1
                    start = i
                    end = j

    return max_length, start , end


def max_palin_dynamic_memory_o1(s):
    l = len(s)
    if l < 2:
        return l

    DP = [True] * l
    max_length = 1
    start = 0
    end = 0

    for i in range(l -2, -1, -1):
        for j in range(l-1, i, -1):
            DP[j] = False
            if s[i] == s[j] and DP[j-1] == 1:
                DP[j] = True
                if max_length < j - i + 1:
                    max_length = j - i + 1
                    start = i
                    end = j

    return max_length, start , end


def max_palin_dynamic_memory_o2(s):
    l = len(s)
    if l < 2:
        return l

    DP = [[True] * l for i in range(l)]
    max_length = 1
    start = 0
    end = 0
    for i in range(l -2, -1, -1):
        for j in range(i + 1, l):
            DP[i][j] = False
            if s[i] == s[j] and DP[i+1][j-1] == 1:
                DP[i][j] = True
                if max_length < j - i + 1:
                    max_length = j - i + 1
                    start = i
                    end = j

    return max_length, start , end