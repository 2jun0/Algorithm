import sys


def input(_type=str):
    return _type(sys.stdin.readline().strip())


def input_n(_type=str):
    return list(map(_type, input().split()))


N = input(int)
A = []

# 1
A.append((min(N + 8, 210), 1))
# 2
A.append((min(N + 4, 220), 2))
# 3
A.append((min(N + 2, 230), 3))
# 4
A.append((min(N + 1, 240), 4))

print(max(A)[1])
