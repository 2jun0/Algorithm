import sys

def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

class Tree1D:
  def __init__(self, line, N):
    self.tree = [-1]*(4*N)
    self.idx2node = [-1]*N
    self.N = N
    
    self._init_tree(1, line, 0, N-1)
  
  def _init_tree(self, node, line, left, right):
    if left == right:
      # leaf
      self.tree[node] = line[left]
      self.idx2node[left] = node
      return self.tree[node]
    
    mid = (left + right) // 2
    self.tree[node] = self._init_tree(node*2, line, left, mid)\
                    + self._init_tree(node*2+1, line, mid+1, right)
    return self.tree[node]
  
  def query(self, node, left, right, srt, end):
    '''query'''
    if right < srt or end < left:
      return 0
    if srt <= left and right <= end:
      return self.tree[node]
    
    mid = (left + right) // 2
    return self.query(node*2, left, mid, srt, end) + self.query(node*2+1, mid+1, right, srt, end)

  def update(self, pos, diff):
    node = self.idx2node[pos]
    while node > 0:
      self.tree[node] += diff
      node //= 2

  def __add__(self, other):
    added = Tree1D([0]*self.N, self.N)
    added.tree = [a + b for a, b in zip(self.tree, other.tree)]
    return added

class Tree2D:
  
  def __init__(self, table, N):
    self.tree = [-1]*(4*N)
    self.idx2node = [-1]*N
    self.N = N
    self._init_tree(1, table, 0, N-1) 
  
  def _init_tree(self, node, table, left, right):
    if left == right:
      # leaf
      self.tree[node] = Tree1D(table[left], self.N)
      self.idx2node[left] = node
      return self.tree[node]
    
    mid = (left + right) // 2
    self.tree[node] = self._init_tree(node*2, table, left, mid)\
                    + self._init_tree(node*2+1, table, mid+1, right)
    return self.tree[node]

  def query(self, node, left, right, srts, ends):
    '''query'''
    if right < srts[0] or ends[0] < left:
      return 0
    if srts[0] <= left and right <= ends[0]:
      v = self.tree[node].query(node=1, left=0, right=self.N-1, srt=srts[1], end=ends[1])
      return v
    
    mid = (left + right) // 2
    return self.query(node*2, left, mid, srts, ends) + self.query(node*2+1, mid+1, right, srts, ends)
  
  def update(self, pos, diff):
    node = self.idx2node[pos[0]]
    while node > 0:
      self.tree[node].update(pos[1], diff)
      node //= 2

N, M = input_n(int)
table = [input_n(int) for _ in range(N)]
tree2D = Tree2D(table, N)

for _ in range(M):
  cmds = input_n(int)
  if cmds[0] == 0:
    _, y, x, c = cmds
    x, y = x-1, y-1
    diff = c - table[y][x]
    tree2D.update((y,x), diff)
    table[y][x] = c
  elif cmds[0] == 1:
    _, y1, x1, y2, x2 = cmds
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    print(tree2D.query(1, 0, N-1, (y1,x1), (y2,x2)))