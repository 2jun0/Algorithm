import sys


def input(type_=str):
    return type_(sys.stdin.readline().rstrip())


def input_n(type_):
    return list(map(type_, input().split()))


def round(a):
    if a - int(a) >= 0.5:
        return int(a) + 1
    else:
        return int(a)


def avg(a):
    return sum(a) / len(a)


n = input(int)
ranks = [input(int) for _ in range(n)]
ranks.sort()

cut = round(n * 0.15)
if n == 0:
    print(0)
else:
    if cut == 0:
        print(round(avg(ranks)))
    else:
        print(round(avg(ranks[cut:-cut])))
