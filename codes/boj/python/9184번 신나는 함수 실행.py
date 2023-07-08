import sys


def input(type_=str):
    return type_(sys.stdin.readline().rstrip())


def input_n(type_):
    return list(map(type_, input().split()))


def w_cache(w_func):
    cache = {}

    def wrapper(*args):
        key = args
        if key not in cache:
            # 캐시가 없으면 업데이트
            cache[key] = w_func(*args)

        return cache[key]

    return wrapper


@w_cache
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if a < b and b < c:
        return w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)

    return (
        w(a - 1, b, c)
        + w(a - 1, b - 1, c)
        + w(a - 1, b, c - 1)
        - w(a - 1, b - 1, c - 1)
    )


while True:
    a, b, c = input_n(int)
    if a == -1 and b == -1 and c == -1:
        break
    val = w(a, b, c)
    print(f"w({a}, {b}, {c}) = {val}")
