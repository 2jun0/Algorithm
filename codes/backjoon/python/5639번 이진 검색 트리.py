import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')

preorder = []

while True: 
  try:preorder.append(input(int))
  except:break
postorder = []
def func(start, end):
  if start >= end: return
  p_x = preorder[start]
  # [p_x ~~ ~~]
  # [~~ ~~ p_x]
  right_start = start+1
  while right_start<end and preorder[right_start] < p_x: right_start+=1
  func(start+1, right_start)
  func(right_start, end)
  postorder.append(p_x)
func(0, len(preorder))
print_n(postorder,'\n')