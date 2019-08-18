
def naive_search(txt, pat):
    n = len(txt)
    m = len(pat)

    result = []
    for i in range(n - m + 1):
        check = True
        for j in range(m):
            if txt[i + j] != pat[j]:
                check = False
                break
        if check:
            result.append(i)
    return result


def preprocess_KMP(pat):
    m = len(pat)
    lsp = [0] * m

    lsp[0] = 0
    for i in range(1, m):
        j = lsp[i - 1]
        while j > 0 and pat[j] != pat[i]:
            j = lsp[j - 1]

        if pat[j] == pat[i]:
            j += 1

        lsp[i] = j

    return lsp


def KMP(txt, pat):
    n = len(txt)
    m = len(pat)

    lsp = preprocess_KMP(pat)
    result = []
    j = 0
    for i in range(n):
        while j > 0 and txt[i] != pat[j]:
            j = lsp[j - 1]

        if txt[i] == pat[j]:
            j += 1
            if j == m:
                result.append(i - m + 1)
                j = lsp[j - 1]

    return result


def compare(a, b, l):
    for i in range(l):
        if a[i] != b[i]:
            return False
    return True

from constants import MAX_CHAR
def anagram_search(txt, pat):
    n = len(txt)
    m = len(pat)

    count_pat = [0] * MAX_CHAR
    count_window = [0] * MAX_CHAR

    position = []
    for i in range(m):
        count_pat[ord(pat[i])] += 1
        count_window[ord(txt[i])] += 1

    if compare(count_pat, count_window, MAX_CHAR):
        position.append(m - 1)

    for i in range(m, n):
        count_window[ord(txt[i])] += 1
        count_window[ord(txt[i - m])] -= 1

        if compare(count_pat, count_window, MAX_CHAR):
            position.append(i)

    result = []
    for r in position:
        result.append((r - m + 1, txt[r - m + 1:r + 1]))

    return result




