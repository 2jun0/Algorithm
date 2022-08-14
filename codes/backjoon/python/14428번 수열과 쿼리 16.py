import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

INF = 10**10
INF_NODE = (INF, INF)

def init_tree(tree, vals, node, start, end):
  if start == end:
    tree[node] = vals[start]
  else:
    mid = (start+end)//2
    tree[node] = min(
      init_tree(tree, vals, node*2, start, mid),
      init_tree(tree, vals, node*2+1, mid+1, end)
    )
  return tree[node]

def update_tree(tree, idx, val, node, start, end):
  # out of range
  if not (start<=idx<=end): 
    pass
  # leaf 노드
  elif start == idx and idx == end:
    tree[node] = val
  else:
    mid = (start+end)//2
    tree[node] = min(
      update_tree(tree, idx, val, node*2, start, mid),
      update_tree(tree, idx, val, node*2+1, mid+1, end)
    )

  return tree[node]

def min_tree(tree, node, left, right, start, end):
  # out of range
  if not (start<=right and left<=end):
    return INF_NODE

  if left <= start and end <= right:
    return tree[node]

  mid = (start+end)//2
  return min(
    min_tree(tree, node*2, left, right, start, mid),
    min_tree(tree, node*2+1, left, right, mid+1, end)
  )


N = input(int)
A = [INF]+input_n(int)
M = input(int)
tree = [INF_NODE for _ in range(4*N)]

# A 전처리
for i, v in enumerate(A):
  A[i] = (v, i)

init_tree(tree, A, 1, 0, len(A)-1)

for _ in range(M):
  cmd, a, b = input_n(int)

  if cmd == 1:
    #A[a] = (b, a)
    update_tree(tree, a, (b, a), 1, 0, len(A)-1)
  elif cmd == 2:
    v, idx = min_tree(tree, 1, a, b, 0, len(A)-1)
    print(idx)