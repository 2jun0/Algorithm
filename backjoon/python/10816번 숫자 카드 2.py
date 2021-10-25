import sys

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

N = input(int)
A = input_n(int)
M = input(int)
A2 = input_n(int)

cnt = {}
for a in A:
  if not a in cnt.keys(): cnt[a] = 0

  cnt[a] += 1

for a in A2[:-1]:
  if not a in cnt.keys(): print(0, end=' ')
  else: print(cnt[a], end=' ')
if not A2[-1] in cnt.keys(): print(0)
else: print(cnt[A2[-1]])