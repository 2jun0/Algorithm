import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  s = ''
  for l in L[:-1]: s+='{}{}'.format(l, join_str)
  s+='{}'.format(L[-1])
  print(s)

class Node:
  def __init__(self, x, left=None, right=None):
    self.x = x
    self.left=left
    self.right=right

x2node = {chr(x) : Node(chr(x)) for x in range(ord('A'), ord('Z')+1)}

N = input(int)
for _ in range(N):
  b, l, r = input_n()
  if l != '.': x2node[b].left = x2node[l]
  if r != '.': x2node[b].right = x2node[r]

def preorder(node):
  if not node:return ''
  return '{}{}{}'.format(node.x, preorder(node.left), preorder(node.right))
def inorder(node):
  if not node:return ''
  return '{}{}{}'.format(inorder(node.left), node.x, inorder(node.right))
def postorder(node):
  if not node:return ''
  return '{}{}{}'.format(postorder(node.left), postorder(node.right), node.x)

print(preorder(x2node['A']))
print(inorder(x2node['A']))
print(postorder(x2node['A']))