import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def init_sums(sums, E):
  sums[-1] = 0
  for i, e in enumerate(E):
    sums[i] = e + sums[i-1]
  
def query_sums(sums, srt, end):
  if srt == 0:
    return sums[end]
  else:
    return sums[end] - sums[srt - 1]

def init_srt_tree(srt_tree, srt_tree_idx2node, node, left, right):
  '''srt_tree는 s ~ e까지 게시물을 작성할때 실제로 작성되는 s` ~ e의 s`를 구하는 것임'''
  if left == right:
    srt_tree[node] = 0
    srt_tree_idx2node[left] = node
    return srt_tree[node]
  else:
    mid = (left + right) // 2
    srt_tree[node] = max(
      init_srt_tree(srt_tree, srt_tree_idx2node, node*2, left, mid),
      init_srt_tree(srt_tree, srt_tree_idx2node, node*2+1, mid+1, right))
    return srt_tree[node]

def query_srt_tree(srt_tree, node, left, right, srt, end):
  if right < srt or end < left:
    return 0
  elif srt <= left and right <= end:
    return srt_tree[node]
  else:
    mid = (left + right) // 2
    return max(
      query_srt_tree(srt_tree, node*2, left, mid, srt, end),
      query_srt_tree(srt_tree, node*2+1, mid+1, right, srt, end))

def update_srt_tree(srt_tree, node, s):
  while node > 0:
    srt_tree[node] = max(srt_tree[node], s)
    node //= 2

N, Q = input_n(int)
sums = [-1]*N
srt_tree_idx2node = [-1]*N
srt_tree = [-1]*(4*N)

E = input_n(int)

init_sums(sums, E)
init_srt_tree(srt_tree, srt_tree_idx2node, 1, 0, N-1)

for t in range(Q):
  cmds = input_n(int)
  
  if cmds[0] == 1:
    d = cmds[1]-1
    update_srt_tree(srt_tree, srt_tree_idx2node[d+1], d+1)
  if cmds[0] == 2:
    s, e = cmds[1]-1, cmds[2]-1
    s_ = max(s, query_srt_tree(srt_tree, 1, 0, N-1, s, e))
    rs = query_sums(sums, s_, e)
    print(rs)