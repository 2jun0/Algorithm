import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

class Node:
  def __init__(self, a):
    self.a = a
    self.occupied = False

class Belts:
  def __init__(self, A):
    self.nodes = [Node(a) for a in A]
    self.zero_cnt = A.count(0)
    self.top = 0

  def get_belt(self, idx):
    '''top기준 idx 위치의 벨트를 구함'''
    return self.nodes[(self.top+idx) % len(self.nodes)]

  def move(self):
    '''벨트를 한칸 움직임'''
    self.top = (self.top - 1) % len(self.nodes)

    # 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내림
    self.checkLeaveNode()

  def is_occupied(self,idx):
    '''idx에 로봇이 있는가?'''
    return self.get_belt(idx).occupied
  
  def can_be_occupied(self,idx):
    '''idx에 로봇을 둘 수 있는가?'''
    # 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    node = self.get_belt(idx)
    return not node.occupied and node.a >= 1

  def leave(self, idx):
    '''idx에 있는 로봇을 내린다.'''
    node = self.get_belt(idx)
    assert node.occupied == True

    self.get_belt(idx).occupied = False
  
  def occupy(self,idx):
    '''idx에 로봇을 올린다.'''
    node = self.get_belt(idx)
    assert node.a >= 1

    node.occupied = True
    node.a -= 1

    if node.a == 0:
      self.zero_cnt += 1

    # 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내림
    self.checkLeaveNode()

  def checkLeaveNode(self):
    '''내리는 칸에 로봇 확인 후 있으면 내리기'''
    leave_idx = N-1

    if self.is_occupied(leave_idx):
      self.leave(leave_idx)

N, K = input_n(int)
A = input_n(int)
belts = Belts(A)
turn = 0

while belts.zero_cnt < K:
  turn += 1

  # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
  belts.move()

  # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
  # belts를 거꾸로 순회한다.
  for idx in range(N*2-1, -1, -1):
    if belts.is_occupied(idx) and belts.can_be_occupied(idx+1):
      # 이동할 수 있음 -> 이동
      belts.leave(idx)
      belts.occupy(idx+1)
        
  # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
  if belts.can_be_occupied(0):
    belts.occupy(0)

print(turn)