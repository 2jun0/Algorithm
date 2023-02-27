import sys
from collections import deque

def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

'''
본 문제는 파이프들의 교차를 찾는 문제로, 시작점은 교차점이 될 수 없고 끝점은 교차점이 될 수 있다.

파이프들이 3개이상 서로 교차 되었을 때, 다각형이 형성된다.
형성된 다각형의 변 중 일부를 선택했을 때, 서로 교차하지 않으면서 모든 꼭짓점을 포함해야 한다.

결국, 다각형의 각 개수가 홀수인지 짝수인지에 따라 답이 나뉜다.
이 풀이에선 그래프 탐색을 이용해 이 답을 구한다.

각 개수가 홀수개라면 아무 시작점에서 탐색해서 다시 시작점으로 돌아올때 홀수번째 탐색으로 끝난다.
반면 각 개수가 짝수개라면 아무 시작점에서 탐색해서 다시 시작점으로 돌아올때 짝수번째 탐색으로 끝난다.

* 아래 코드에선 bfs로 구현했기 때문에 모든 점의 홀 짝수 번호를 구한다.
'''

def ccw(a, b, c):
  return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def is_cross(a, b, c, d):
  a, b = min(a,b), max(a,b)
  c, d = min(c,d), max(c,d)
  
  abc = ccw(a, b, c)
  abd = ccw(a, b, d)
  cda = ccw(c, d, a)
  cdb = ccw(c, d, b)
  
  flag = abc * abd <= 0 and cda * cdb <= 0
  if abc * abd == 0 and cda * cdb == 0:
    # 어느 정점이 다른 *직선*에 속해있음
    if d < a or b < c:
      # can't meet each other (선분안에 있지는 않음)
      flag = False
  
  return flag

def bfs(adjs, src, dists):
  q = deque()
  
  dists[src] = 0
  q.append(src)
  
  while q:
    x = q.popleft()
    
    for nxt in adjs[x]:
      
      if dists[nxt] == -1:
        dists[nxt] = dists[x] + 1
        q.append(nxt)
      elif dists[nxt] % 2 != (dists[x] + 1) % 2:
        return False
        
  return True

def solve(adjs):
  dists = [-1]*len(adjs)
  
  for i in range(len(adjs)):
    if dists[i] == -1:
      if not bfs(adjs, i, dists):
        return False
  return True
  
w, p = input_n(int)
srcs = [None] + [tuple(input_n(int)) for _ in range(w)]
pipes = []
for _ in range(p):
  src_idx, px, py = input_n(int)
  pipes.append((srcs[src_idx], (px,py)))

adjs = [[] for _ in range(p)]
for i in range(p):
  a, b = pipes[i]
  for j in range(i+1, p):
    c, d = pipes[j]
    if a!=c and is_cross(a, b, c, d):
      adjs[i].append(j)
      adjs[j].append(i)

if solve(adjs):
  print('possible')
else:
  print('impossible')