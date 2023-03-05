import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def init_tree(tree, idx2node, node, left, right):
  if left == right:
    idx2node[left] = node
  else:
    mid = (left + right) // 2
    init_tree(tree, idx2node, node*2, left, mid)
    init_tree(tree, idx2node, node*2+1, mid+1, right)

def query_tree(tree, node, left, right, srt, end):
  if right < srt or end < left:
    return 0
  if srt <= left and right <= end:
    return tree[node]
  
  mid = (left + right) // 2
  return query_tree(tree, node*2, left, mid, srt, end)\
    + query_tree(tree, node*2+1, mid+1, right, srt, end)
    
def update_tree(tree, node, v):
  while node > 0:
    tree[node] += v
    node //= 2

def x2idx(x):
  return x - MIN_X

MIN_X = -2*10**5
MAX_X = 2*10**5
MAX_IDX = x2idx(MAX_X)
MOD = 10**9 + 7

tree = [0]*(MAX_IDX*4)
idx2node = [None]*(MAX_IDX+1)
init_tree(tree, idx2node, 1, 0, MAX_IDX)

N = input(int)
Ax_by_y = {}
for _ in range(N):
  x, y = input_n(int)
  Ax_by_y.setdefault(y, []).append(x)
  
rs = 0
for y in sorted(Ax_by_y.keys(), reverse=True):
  for x in Ax_by_y[y]:
    idx = x2idx(x)
    a_cnt = query_tree(tree, 1, 0, MAX_IDX, 0, idx-1)
    b_cnt = query_tree(tree, 1, 0, MAX_IDX, idx+1, MAX_IDX)
    rs = (rs + (a_cnt * b_cnt) % MOD) % MOD
  for x in Ax_by_y[y]:
    idx = x2idx(x)
    update_tree(tree, idx2node[idx], 1)

print(rs)