import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for l in L: print(l, end=join_str)

n = input(int)
inorder = input_n(int)
x2inorder_idx = {x:i for i, x in enumerate(inorder)}
postorder = input_n(int)
x2postorder_idx = {x:i for i, x in enumerate(postorder)}

preorder = []
def to_preorder(in_start, in_end, post_start, post_end):
  if in_start>=in_end: return
  p_x = postorder[post_end-1]
  preorder.append(p_x)

  p_in_idx = x2inorder_idx[p_x]
  p_post_idx = x2postorder_idx[p_x]

  # in [~~ p ~~] or [~~ p] or [p ~~]
  # post [~~ ~~ p] or [~~ p] or [~~ p]

  l_in_start, l_in_end = in_start, p_in_idx
  r_in_start, r_in_end = p_in_idx+1, in_end
  
  # right
  if r_in_start<r_in_end:
    r_in_start_x = inorder[r_in_start]
    r_post_start, r_post_end = x2postorder_idx[r_in_start_x], p_post_idx
  else:
    r_post_start, r_post_end = p_post_idx, p_post_idx

  # left
  l_post_start, l_post_end = post_start, r_post_start

  to_preorder(l_in_start, l_in_end, l_post_start, l_post_end)
  to_preorder(r_in_start, r_in_end, r_post_start, r_post_end)

to_preorder(0,n,0,n)
# print_n(preorder(T))
print_n(preorder)