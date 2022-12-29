import sys

def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

def query(tree, node, left, right, start, end):
  if end < left or right < start:
    return 0
  if start <= left and right <= end:
    return tree[node]
  mid = (left + right)//2
  v = query(tree, node*2, left, mid, start, end)
  v+= query(tree, node*2+1, mid+1, right, start, end)
  return v
  
def update_up(tree, node, diff):
  while node > 0:
    tree[node] += diff
    node //= 2
  
def init_idx2node(idx2node, node, left, right):
  if left == right:
    idx2node[left] = node
  else:
    mid = (left + right)//2
    init_idx2node(idx2node, node*2, left, mid)
    init_idx2node(idx2node, node*2+1, mid+1, right)
    
def preprocess(A):
  nums = sorted(set(A))
  num2idx = {num: idx for idx, num in enumerate(nums)}
  return [num2idx[a] for a in A]

N = input(int)
A = [input(int) for _ in range(N)]
A = preprocess(A)

tree = [0]*(N*4)
idx2node = [None]*N
init_idx2node(idx2node, 1, 0, N-1)
for idx, a in enumerate(A):
  print(min(idx, query(tree, 1, 0, N-1, a, N-1))+1)
  update_up(tree, idx2node[a], 1)