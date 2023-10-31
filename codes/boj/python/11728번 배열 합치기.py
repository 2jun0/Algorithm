import sys


def input(_type=str):
    return _type(sys.stdin.readline().strip())


def input_n(_type=str):
    return list(map(_type, input().split()))


N, M = input_n(int)
A = input_n(int)
B = input_n(int)
C = sorted(A + B)
print(*C)
