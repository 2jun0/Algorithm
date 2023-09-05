import sys


def input(_type=str):
    return _type(sys.stdin.readline().strip())


def input_n(_type=str):
    return list(map(_type, input().split()))


def det(t1x, t1y, t2x, t2y):
    return t1x * t2y - t2x * t1y


x1, y1 = input_n(int)
x2, y2 = input_n(int)
x3, y3 = input_n(int)

v1x = x2 - x1
v1y = y2 - y1
v2x = x3 - x1
v2y = y3 - y1

rs = det(v1x, v1y, v2x, v2y)
if rs < 0:
    print(-1)
elif rs > 0:
    print(1)
else:
    print(0)
