import sys

def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

N = input(int)
D = input_n(int)
C = input_n(int)
  
low_cost_order = sorted([[c, pos] for pos, c in enumerate(C)])
right = N-1
total_cost = 0

for c, pos in low_cost_order:
  if pos < right:
    '''get dist sum (pos ~ right)'''
    diff = 0
    for dpos in range(pos, right):
      diff += D[dpos]
    
    total_cost += c * diff
    right = pos

print(total_cost)