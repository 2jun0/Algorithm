import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

is_belong = [False] * 31
for _ in range(28):
  a = input(int)
  is_belong[a] = True

for a in range(1, 31):
  if not is_belong[a]:
    print(a)