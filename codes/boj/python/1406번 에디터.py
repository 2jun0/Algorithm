import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def attach_nodes(ns):
  for idx in range(len(ns)-1):
    if ns[idx]:
      ns[idx].attach_right(ns[idx+1])
    if ns[idx+1]:
      ns[idx+1].attach_left(ns[idx])
  return ns[-1]

def remove_node(n):
  attach_nodes([n.left, n.right])

def print_nodes(head):
  while head.v != -1:
    head = head.left

  s = ''
  head = head.right
  while head != None:
    s += head.v
    head = head.right
  
  print(s)

class Node:
  def __init__(self, v):
    self.left = None
    self.right = None
    self.v = v

  def attach_left(self, n):
    self.left = n
  
  def attach_right(self, n):
    self.right = n

head = attach_nodes([Node(-1)]+[Node(c) for c in input(str)])
K = input(int)
for _ in range(K):
  cmds = input_n(str)

  if cmds[0] == 'L':
    if head.left:
      head = head.left
  
  if cmds[0] == 'D':
    if head.right:
      head = head.right
    
  if cmds[0] == 'B':
    if head.v != -1:
      tmp = head.left
      remove_node(head)
      head = tmp
  
  if cmds[0] == 'P':
    n = Node(cmds[1])
    attach_nodes([n, head.right])
    attach_nodes([head, n])
    head = n

print_nodes(head)