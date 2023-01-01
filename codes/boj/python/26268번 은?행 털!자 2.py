import sys

def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

def query(tree, node, srt, end, l, r):
  if r < srt or end < l:
    return 0
  if l <= srt and end <= r:
    return tree[node]
  v = query(tree, node*2, srt, (srt+end)//2, l, r)
  v = max(v, query(tree, node*2+1, (srt+end)//2+1, end, l, r))
  return v

def update(tree, node, v):
  tree[node] = v
  node //= 2
  while node > 0:
    tree[node] = max(tree[node*2], tree[node*2+1])
    node //= 2

def init(index2node, node, srt, end):
  if srt == end:
    index2node[srt] = node
  else:
    init(index2node, node*2, srt, (srt+end)//2)
    init(index2node, node*2+1, (srt+end)//2+1, end)

def pre_t(A):
  ts = sorted(set([t for t,c in A]))
  t2idx = {t: idx for idx, t in enumerate(ts)}
  for i in range(len(A)):
    A[i][0] = t2idx[A[i][0]]

N = input(int)
A = []
for _ in range(N):
  X, T, C = input_n(int)
  A.append([T-X,C])

pre_t(A)
tree = [0]*(N*4)
index2node = [0]*N
init(index2node, 1, 0, N-1)

rs = 0
for t, c in A:
  v = query(tree, 1, 0, N-1, 0, t)  
  update(tree, index2node[t], v+c)
  rs = max(rs, v+c)

print(rs)

# 5
# 0 2 4  2 4
# 1 6 1  5 1
# 2 4 4  2 4
# 3 8 10 5 10
# 4 5 2  1 2
# 5 9 5  4 5