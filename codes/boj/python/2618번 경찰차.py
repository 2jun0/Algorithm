import sys
sys.setrecursionlimit(10000)
def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

def get_dist(idx1, idx2):
  return abs(pos[idx1][0] - pos[idx2][0]) + abs(pos[idx1][1] - pos[idx2][1])

def get_opt_dist(a, b):
  if a == len(pos)-1 or b == len(pos)-1:
    return 0
  
  if cache[a][b] != INF:
    return cache[a][b]
  
  nxt = max(a,b)+1
  # move a to nxt
  ad = get_opt_dist(nxt, b) + get_dist(a, nxt)
  # move b to nxt
  bd = get_opt_dist(a, nxt) + get_dist(b, nxt)
    
  cache[a][b] = min(ad, bd)
  return cache[a][b]

def find_path(a, b):
  if a == len(pos)-1 or b == len(pos)-1:
    return 0
  
  nxt = max(a,b)+1
  # move a to nxt
  ad = get_opt_dist(nxt, b) + get_dist(a, nxt)
  # move b to nxt
  bd = get_opt_dist(a, nxt) + get_dist(b, nxt)

  if ad < bd:
    pos2ab[nxt] = 1
    find_path(nxt, b)
  else:
    pos2ab[nxt] = 2
    find_path(a, nxt)

N = input(int)
W = input(int)
INF = 10**8

pos = [(1,1), (N,N)] + [input_n(int) for _ in range(W)]
cache = [[INF]*len(pos) for _ in range(len(pos))]
pos2ab = [1, 2] + [0]*W

print(get_opt_dist(0, 1))
find_path(0, 1)
for idx in range(2, len(pos)):
  print(pos2ab[idx])
