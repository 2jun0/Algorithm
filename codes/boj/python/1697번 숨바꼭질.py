import sys

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

N, K = input_n(int)
table = [1000000]*100001

table[N] = 0
s = [N]
while len(s) > 0:
  a = s.pop(0)
  a1, a2, a3 = (a-1, a+1, a*2)

  if a == K:
    if N == K:
      table[K] = 0
    break

  if a1 >= 0:
    if table[a1] > table[a]+1:
      table[a1] = table[a]+1
      s.append(a1)
  if a2 <= K:
    if table[a2] > table[a]+1:
      table[a2] = table[a]+1
      s.append(a2)
  if a3 <= 100000:
    if table[a3] > table[a]+1:
      table[a3] = table[a]+1
      s.append(a3)

print(table[K])