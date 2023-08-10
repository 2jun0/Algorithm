import sys


def input(type_=str):
    return type_(sys.stdin.readline().rstrip())


def input_n(type_):
    return list(map(type_, input().split()))


def cost(a, b):
    r = 0
    for i in range(4):
        if a[i] != b[i]:
            r += 1
    return r


MBTI = [
    "ISTJ",
    "ISFJ",
    "INFJ",
    "INTJ",
    "ISTP",
    "ISFP",
    "INFP",
    "INTP",
    "ESTP",
    "ESFP",
    "ENFP",
    "ENTP",
    "ESTJ",
    "ESFJ",
    "ENFJ",
    "ENTJ",
]


def dfs(cnts, total_cnts, a, dep, A):
    if cnts[a] > total_cnts[a]:
        return 99

    if dep == 0:
        return cost(A[0], A[1]) + cost(A[0], A[2]) + cost(A[2], A[1])

    rs = 99
    for b in MBTI:
        cnts[b] += 1
        rs = min(rs, dfs(cnts, total_cnts, b, dep - 1, A + [b]))
        cnts[b] -= 1

    return rs


T = input(int)
for _ in range(T):
    N = input(int)
    A = input_n(str)

    total_cnts = {a: 0 for a in MBTI}

    for i, a in enumerate(A):
        total_cnts[a] += 1

    rs = 99
    for a in MBTI:
        cnts = {b: 0 for b in MBTI}
        cnts[a] += 1
        rs = min(rs, dfs(cnts, total_cnts, a, 2, [a]))
        cnts[a] -= 1

    print(rs)
