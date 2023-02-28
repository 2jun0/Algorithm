import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))  

def init_tree(tree, idx2node, node, left, right):
  if left == right:
    if left == 0:
      tree[node] = 0
    else:
      tree[node] = 1
      
    idx2node[left] = node
    return tree[node]
  
  mid = (left + right) // 2
  tree[node] = init_tree(tree, idx2node, node*2, left, mid)\
              + init_tree(tree, idx2node, node*2+1, mid+1, right)
              
  return tree[node]
    
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

N, K = input_n(int)
tree = [0]*(4*N)
idx2node = [-1]*(N+1)
init_tree(tree, idx2node, 1, 0, N)
rs = []
k = 1
remain = N

while remain > 0:
  k += K-1
  if k > remain:
    k %= remain 
    if k == 0:
      k = remain
  
  x = query_tree(tree, 1, 0, N, k)
  rs.append(x)
  sub_tree(tree, idx2node[x])
  remain -= 1
  
print('<'+', '.join(map(str, rs))+'>')