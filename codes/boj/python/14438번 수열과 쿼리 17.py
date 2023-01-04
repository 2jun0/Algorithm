import sys

def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))
INF = 10**10
def init(A, tree, node, srt, end):
  if srt == end:
    idx2node[srt] = node
    tree[node] = A[srt]
    return tree[node]
  
  mid = (srt+end)//2
  v = init(A, tree, node*2, srt, mid)
  v = min(v, init(A, tree, node*2+1, mid+1, end))
  tree[node] = v
  return tree[node]
    
def query(tree, node, srt, end, l, r):
  if r < srt or end < l:
    return INF
  if l <= srt and end <= r:
    return tree[node]
  
  mid = (srt+end)//2
  v = query(tree, node*2, srt, mid, l, r)
  v = min(v, query(tree, node*2+1, mid+1, end, l, r))
  return v

def update(tree, idx, v):
  node = idx2node[idx]
  tree[node] = v
  node //= 2
  while node > 0:
    tree[node] = min(tree[node*2], tree[node*2+1])
    node //= 2

N = input(int)
A = input_n(int)
M = input(int)

tree = [INF]*(N*4)
idx2node = [-1]*N
init(A, tree, 1, 0, N-1)
for _ in range(M):
  t, i, j = input_n(int)
  
  if t == 1:
    update(tree, i-1, j)
  elif t == 2:
    print(query(tree, 1, 0, N-1, i-1, j-1))