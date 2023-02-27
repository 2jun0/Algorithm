import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

class Tree:
  def __init__(self, N, expr, worst_val):
    self.N = N
    self.tree = [None]*(20*N)
    self.expr = expr
    self.worst_val = worst_val
    self.idx2node = [-1]*N
    
    self._init_tree(1, 0, N-1)
  
  def _init_tree(self, node, left, right):
    '''O(nlogn)'''
    if left == right:
      self.tree[node] = left
      self.idx2node[left] = node
      return self.tree[node]
    
    mid = (left + right) // 2
    self.tree[node] = self.expr(
      self._init_tree(node*2, left, mid), 
      self._init_tree(node*2+1, mid+1, right))
    return self.tree[node]
  
  def _query(self, node, left, right, srt, end):
    '''O(logn)'''
    if right < srt or end < left:
      return self.worst_val
    if srt <= left and right <= end:
      return self.tree[node]

    mid = (left + right) // 2
    
    return self.expr(
      self._query(node*2, left, mid, srt, end), 
      self._query(node*2+1, mid+1, right, srt, end))
    
  def query(self, srt, end):
    return self._query(1, 0, self.N-1, srt, end)
    
  def update(self, idx, updated):
    node = self.idx2node[idx]
    self.tree[node] = updated
    node //= 2

    while node > 0:
      self.tree[node] = self.expr(
        self.tree[node*2], self.tree[node*2+1])
      node //= 2
      
  def get_leaf_val(self, idx):
    return self.tree[self.idx2node[idx]]

def switch_dvd(min_tree: Tree, max_tree: Tree, a, b):
  a_dvd = min_tree.get_leaf_val(a)
  b_dvd = min_tree.get_leaf_val(b)
  # b위치에 있는 dvd를 a위치로 이동
  min_tree.update(a, b_dvd)
  max_tree.update(a, b_dvd)
  # a위치에 있는 dvd를 b위치로 이동
  min_tree.update(b, a_dvd)
  max_tree.update(b, a_dvd)
  
def query_dvds(min_tree: Tree, max_tree: Tree, a, b):
  return min_tree.query(a, b) == a and max_tree.query(a, b) == b

T = input(int)
for _ in range(T):
  N, K = input_n(int)
  min_tree = Tree(N, lambda a, b: min(a,b), N)
  max_tree = Tree(N, lambda a, b: max(a,b), -1)
  
  for _ in range(K):
    Q, A, B = input_n(int)
  
    if Q == 0:
      switch_dvd(min_tree, max_tree, A, B)
    elif Q == 1:
      if query_dvds(min_tree, max_tree, A, B):
        print('YES')
      else:
        print('NO')