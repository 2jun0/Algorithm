import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]
def avg(l): return sum(l)/len(l)

R, C = input_n(int)
table = [input() for _ in range(R)]
s = [(0,0,0,1)]
max_cnt = 0
while len(s) > 0:
  r, c, mask, cnt = s.pop()

  alpha_idx = ord(table[r][c]) - ord('A')
  if mask & (1 << alpha_idx) != 0: continue

  mask |= 1 << alpha_idx
  max_cnt = max(max_cnt, cnt)

  for tr, tc in [(r+1, c),(r-1, c),(r, c+1),(r, c-1)]:
    if 0<=tr<R and 0<=tc<C: s.append((tr, tc, mask, cnt+1))

print(max_cnt)