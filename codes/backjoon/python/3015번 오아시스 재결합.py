import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]
def avg(l): return sum(l)/len(l)
def getLRUD(i,j): return [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

N = input(int)
A = [input(int) for _ in range(N)]

class Node:
  def __init__(self, num, count=1):
    self.num = num
    self.count = count
  def __repr__(self):
    return f'{self.num} x {self.count}'

pair = 0
front = []
# front는 항상 내림차순 이여야 한다.
# 8, 6, 3 이런순, 내 앞에 있는 사람이기 때문.
for x in A:
  # 앞에 보이는 사람 명수 다 더함 X
  # 서로 보여야 하니까 내가 앞 사람보다 작으면 안됨
  # 고로, 제일 가까이 있는 사람부터 나보다 큰 사람 나올때까지 돌림
  for fx in reversed(front):
    if fx.num <= x:
      pair += fx.count
    elif fx.num > x: # 날 보는 마지막 사람은 내가 보이겠지
      # (근데 같은 것에 가려지면 안 보인다. 그래서 1)
      # ex) 3 3 1
      pair += 1
      break

  # 나보다 작으면 pop
  while len(front) > 0 and front[-1].num < x:
    front.pop()

  # 나를 front에 넣기
  if len(front) > 0 and front[-1].num == x:
    front[-1].count += 1
  else:
    front.append(Node(x))

print(pair)