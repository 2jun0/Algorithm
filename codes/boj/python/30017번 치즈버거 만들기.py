import sys


def input(_type=str):
    return _type(sys.stdin.readline().strip())


def input_n(_type=str):
    return list(map(_type, input().split()))


a, b = input_n(int)
print(min(a - 1, b) * 2 + 1)
