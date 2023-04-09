import sys

def input(type_=str):
	return type_(sys.stdin.readline().rstrip())
def input_n(type_):
	return list(map(type_, input().split()))

N, M, K = input_n(int)
cap = 0
min_t = N
rec = [input_n(int) for _ in range(M)]
for i, (t, r) in enumerate(rec):
  cap += r
  min_t = min(min_t, t-1)
  if cap > K:
    print(i+1, min_t+1)
    break
else:
  print(-1)