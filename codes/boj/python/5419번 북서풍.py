import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def query(tree, node, start, end, left, right):
  if left <= start and end <= right:
    return tree[node]
  if left > end or start > right:
    return 0
  val = 0
  val += query(tree, node*2, start, (start + end) // 2, left, right)
  val += query(tree, node*2+1, (start + end) // 2 + 1, end, left, right)
  return val

def init_idx2node(idx2node, node, start, end):
  if start == end:
    idx2node[start] = node
    return
  
  init_idx2node(idx2node, node*2, start, (start+end) // 2)
  init_idx2node(idx2node, node*2+1, (start+end) // 2 + 1, end)

def update_up(tree, node, diff):
  while node > 0:
    tree[node] += diff
    node //= 2

T = input(int)
for _ in range(T):
  A = []
  
  n = input(int)
  for idx in range(n):
    x, y = input_n(int)
    A.append([x,y])
  
  # y 압축
  A.sort(key=lambda pos: pos[1])
  y_cnt = 0
  last_y = None
  for idx, pos in enumerate(A):
    if last_y != pos[1]:
      last_y = pos[1]
      y_cnt += 1
    
    A[idx][1] = y_cnt-1
  
  # update_up을 위한 idx2node
  idx2node = [None]*y_cnt
  init_idx2node(idx2node, 1, 0, y_cnt-1)
  
  # 세그먼트 트리에 넣으면서 확인함
  result = 0
  tree = [0]*(y_cnt*4)
  A.sort(key=lambda pos: (pos[0], -pos[1]))
  for x, y in A:
    result += query(tree, 1, 0, y_cnt-1, y, y_cnt-1)
    update_up(tree, idx2node[y], 1)
  
  print(result)
  