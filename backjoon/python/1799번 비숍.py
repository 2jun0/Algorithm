import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]
def avg(l): return sum(l)/len(l)

N = input(int)
table = [input_n(int) for _ in range(N)]
EVEN_A = []
ODD_A = []
for y in range(N):
  for x in range(N):
    if table[y][x] == 1: 
      if (x+y)%2 == 0: EVEN_A.append((y,x))
      else: ODD_A.append((y,x))

EVEN = [0]*20 # y, x = y, 2i + y
EVEN_re = [0]*20 # y, x = y, 2i - y
ODD = [0]*20 # y, x = y, 1+2i + y
ODD_re = [0]*20 # y, x = y, 1+2i - y

def get_EVEN_idx(y, x): return (x-y)//2, (x+y)//2
def get_ODD_idx(y, x): return (x-y-1)//2, (x+y-1)//2

def func(y, x, v=1):
  if (x+y)% 2 == 0:
    idx, re_idx = get_EVEN_idx(y, x)
    EVEN[idx]+=v
    EVEN_re[re_idx]+=v
  else:
    idx, re_idx = get_ODD_idx(y, x)
    ODD[idx]+=v
    ODD_re[re_idx]+=v

def ok(y, x):
  if (x+y)% 2 == 0:
    idx, re_idx = get_EVEN_idx(y, x)
    if EVEN[idx] == 0 and EVEN_re[re_idx] == 0: return True
  else:
    idx, re_idx = get_ODD_idx(y, x)
    if ODD[idx] == 0 and ODD_re[re_idx] == 0: return True
  return False

def dfs(A, i):
  y,x = A[i]
  func(y,x)
  max_v = 0
  for ti in range(i+1, len(A)):
    ty,tx = A[ti]
    if ok(ty,tx): max_v = max(max_v, dfs(A, ti))
  func(y,x,-1)
  return max_v+1

max_even_v = 0
for i in range(len(EVEN_A)):
  max_even_v = max(max_even_v, dfs(EVEN_A, i))
max_odd_v = 0
for i in range(len(ODD_A)):
  max_odd_v = max(max_odd_v, dfs(ODD_A, i))

print(max_odd_v + max_even_v)