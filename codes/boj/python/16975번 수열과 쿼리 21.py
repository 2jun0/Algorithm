import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def init_tree(tree, node, A, left, right):
  if left == right:
    tree[node] = A[left]
    return
  tree[node] = 0
  mid = (left + right) // 2
  init_tree(tree, node*2, A, left, mid)
  init_tree(tree, node*2+1, A, mid+1, right)

def add_tree(tree, node, left, right, srt, end, diff):
  if end < left or right < srt:
    return
  if srt <= left and right <= end:
    tree[node] += diff
    return
  
  mid = (left + right) // 2
  add_tree(tree, node*2, left, mid, srt, end, diff)
  add_tree(tree, node*2+1, mid+1, right, srt, end, diff)

def query_tree(tree, node, idx, left, right):
  if idx < left or right < idx:
    return 0
  if left == right and left == idx:
    return tree[node]
  
  mid = (left + right) // 2
  # propagation
  tree[node*2] += tree[node]
  tree[node*2+1] += tree[node]
  tree[node] = 0
  
  return query_tree(tree, node*2, idx, left, mid) + query_tree(tree, node*2+1, idx, mid+1, right)

N = input(int)
A = input_n(int)
M = input(int)
tree = [-1]*(4*N)
init_tree(tree, 1, A, 0, N-1)
for _ in range(M):
  cmds = input_n(int)
  if cmds[0] == 1:
    a, b, c = cmds[1]-1, cmds[2]-1, cmds[3]
    add_tree(tree, 1, 0, N-1, a, b, c)
  elif cmds[0] == 2:
    x = cmds[1]-1
    print(query_tree(tree, 1, x, 0, N-1))