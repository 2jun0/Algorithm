import sys


def input(_type=str):
    return _type(sys.stdin.readline().strip())


def input_n(_type=str):
    return list(map(_type, input().split()))


S = input()
star_pos = -1
a = 0
for i, s in enumerate(S):
    if s == "*":
        star_pos = i
        continue

    if i % 2 != 0:
        a += 3 * int(s)
    else:
        a += int(s)


if star_pos % 2 != 0:
    for star in range(10):
        if (a + 3 * star) % 10 == 0:
            print(star)
            break
else:
    for star in range(10):
        if (a + star) % 10 == 0:
            print(star)
            break
