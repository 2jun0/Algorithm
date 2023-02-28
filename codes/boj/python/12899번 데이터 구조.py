import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))  

def init_tree(tree, idx2node, node, left, right):
  if left == right:
    idx2node[left] = node
    return
  mid = (left + right) // 2
  init_tree(tree, idx2node, node*2, left, mid)
  init_tree(tree, idx2node, node*2+1, mid+1, right)

def add_tree(tree, node):
  while node > 0:
    tree[node] += 1
    node //= 2
    
def sub_tree(tree, node):
  while node > 0:
    tree[node] -= 1
    node //= 2

def query_tree(tree, node, left, right, x):
  '''x번째로 작은 수는?'''
  
  if left == right:
    # leaf node, 이제 결정해야 할 시기!
    return left
  
  mid = (left + right) // 2
  lcnt = tree[node*2]
  
  if x <= lcnt:
    # 왼쪽에 속하는가?
    return query_tree(tree, node*2, left, mid, x)
  else:
    # 오른쪽이구나
    x -= lcnt
    return query_tree(tree, node*2+1, mid+1, right, x)

N = input(int)
MAX = 2_000_000
tree = [0]*(4*MAX)
idx2node = [-1]*(MAX+1)
init_tree(tree, idx2node, 1, 0, MAX)
for _ in range(N):
  t, x = input_n(int)
  
  if t == 1:
    add_tree(tree, idx2node[x])
  if t == 2:
    searched = query_tree(tree, 1, 0, MAX, x)
    print(searched)
    sub_tree(tree, idx2node[searched])