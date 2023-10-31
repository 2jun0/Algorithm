import sys


def input(_type=str):
    return _type(sys.stdin.readline().strip())


def input_n(_type=str):
    return list(map(_type, input().split()))


T = input(int)
for _ in range(T):
    N = input_n(int)
    N.sort()
    if N[3] - N[1] >= 4:
        print("KIN")
    else:
        print(sum(N[1:4]))
