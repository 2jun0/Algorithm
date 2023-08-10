import sys


def input(type_=str):
    return type_(sys.stdin.readline().rstrip())


a = input()
if a == a[::-1]:
    print(1)
else:
    print(0)
