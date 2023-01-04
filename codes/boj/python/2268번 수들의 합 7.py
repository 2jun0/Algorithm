import sys

def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

def query(tree, node, left, right, start, end):
  if end < left or start > right:
    return 0
  if start <= left and right <= end:
    return tree[node]

  mid = (left + right) // 2
  v = query(tree, node*2, left, mid, start, end)
  v+= query(tree, node*2+1, mid+1, right, start, end)
  return v

def update_up(tree, node, v):
  diff = v - tree[node]
  while node > 0:
    tree[node] += diff
    node //= 2

def init_idx2node(idx2node, node, left, right):
  if left == right:
    idx2node[left] = node
    return
  
  mid = (left + right) // 2
  init_idx2node(idx2node, node*2, left, mid)
  init_idx2node(idx2node, node*2+1, mid+1, right)

N, M = input_n(int)
tree = [0]*(N*4)
idx2node = [0]*N
init_idx2node(idx2node, 1, 0, N-1)
for _ in range(M):
  t, a, b = input_n(int)
  
  if t == 0:
    a, b = min(a,b), max(a,b)
    print(query(tree, 1, 0, N-1, a-1, b-1))
  if t == 1:
    update_up(tree, idx2node[a-1], b)
