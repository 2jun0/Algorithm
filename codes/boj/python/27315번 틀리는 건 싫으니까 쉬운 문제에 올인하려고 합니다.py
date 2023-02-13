import sys
import heapq

def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

def ceil(x, y):
  if x % y == 0:
    return x // y
  else:
    return (x // y) + 1

N, M = input_n(int)

h_idea = []
h_problem = []

for idx in range(N):
  d,p,t,e = input_n(int)
  if e == 1:
    d = ceil(d, 2)
    p = p//2
  if t == 1:
    p = 0
    
  heapq.heappush(h_idea, (d, p))

def can_solve(d, hd):
  return d <= hd

def solve_cost(p, hp):
  return max(0, p-hp)

hd, hp = input_n(int)
cost = 0
for _ in range(M):
  # problem heapq update
  while h_idea:
    d, p = h_idea[0]
    if can_solve(d, hd):
      heapq.heappop(h_idea)
      heapq.heappush(h_problem, (p, d))
    else:
      break

  # problem
  if h_problem:
    p, d = heapq.heappop(h_problem)
    if can_solve(d, hd):
      cost += solve_cost(p, hp)
      hd += 1
      hp += 1
  else:
    cost = -1
    break

print(cost)