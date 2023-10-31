import sys


def input(_type=str):
    return _type(sys.stdin.readline().strip())


def input_n(_type=str):
    return list(map(_type, input().split()))


N = input(int)
P = input(int)

A = []

if 20 <= N:
    A.append(P // 4 * 3)
if 15 <= N:
    A.append(max(0, P - 2000))
if 10 <= N:
    A.append(P // 10 * 9)
if 5 <= N:
    A.append(max(0, P - 500))

A.append(P)

print(min(A))
