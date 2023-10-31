import sys


def input(_type=str):
    return _type(sys.stdin.readline().strip())


def input_n(_type=str):
    return list(map(_type, input().split()))


UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
M, N = input_n(int)
top = 1
left = 1
bottom = M
right = N

d = RIGHT
turn = 0

shortcut = min(N - 1, M - 1) // 2
top += shortcut
left += shortcut
bottom -= shortcut
right -= shortcut
turn += shortcut * 4

while True:
    if d == UP:
        left += 1
    elif d == RIGHT:
        top += 1
    elif d == DOWN:
        right -= 1
    elif d == LEFT:
        bottom -= 1

    if not (top <= bottom and left <= right):
        if d == UP:
            left += -1
        elif d == RIGHT:
            top += -1
        elif d == DOWN:
            right -= -1
        elif d == LEFT:
            bottom -= -1
        break

    d = (d + 1) % 4
    turn += 1

rs_y, rs_x = 0, 0


if d == UP:
    rs_y, rs_x = top, left
elif d == RIGHT:
    rs_y, rs_x = top, right
elif d == DOWN:
    rs_y, rs_x = bottom, left
elif d == LEFT:
    rs_y, rs_x = top, left

print(turn)
print(rs_y, rs_x)
