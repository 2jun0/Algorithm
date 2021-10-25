import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')

N, K = input_n(int)
table = [INF]*100001

s1 = []
s2 = [N]
t = 0
cnt = 0
while len(s2) > 0:
  s1, s2 = s2, s1
  while len(s1) > 0:
    a = s1.pop()
    if a < 0 or a > 100000 or table[a] < t: continue
    if a == K: cnt+=1
    table[a] = t
    s2.extend([a+1, a-1, 2*a])
  t+=1
  if cnt > 0: break
print(t-1)
print(cnt)