import sys


def input(_type=str):
    return _type(sys.stdin.readline().strip())


def input_n(_type=str):
    return list(map(_type, input().split()))


N, A, B = input_n(int)
bus = A
subway = max(N, B)

if bus < subway or N > B:
    print("Bus")
elif bus > subway:
    print("Subway")
else:
    print("Anything")
