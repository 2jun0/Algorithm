import sys

def input(type_=str):
	return type_(sys.stdin.readline().rstrip())
def input_n(type_):
	return list(map(type_, input().split()))


PLUS = 0
MINUS = 1
TIMES = 2
DIV = 3


def calc(a, b, t):
  '''
  a와 b에 대한 연산 t의 결과를 구함
  '''
  if t == PLUS:
    return a + b
  if t == MINUS:
    return a - b
  if t == TIMES:
    return a * b
  if t == DIV:
    if (a < 0) ^ (b < 0):
      return - (abs(a) // abs(b))
    else:
      return abs(a) // abs(b)
  
  raise Exception('잘못된 연산자', t)


def dfs(A, idx, cnts, y):
  '''
  A : A
  idx : 연산자가 들어갈 위치
  cnts : 남은 연산자의 수
  y : 지금까지의 계산결과
  
  return : (min 최종, max 최종)
  '''
  if len(A)-1 == idx:
    # 더 이상 연산할 수 없다. -> 결과 반환
    return y, y
  
  total_max_v = -10**8
  total_min_v = 10**8
  
  for t in [PLUS, MINUS, TIMES, DIV]:
    if cnts[t] <= 0:
      # 남은 연산자가 없으면 사용할 수 없다.
      continue
    
    # 연산자를 하나 사용하고 다음 결과로 ㄱㄱ
    cnts[t] -= 1
    nxt_y = calc(y, A[idx+1], t)
    min_v, max_v = dfs(A, idx+1, cnts, nxt_y)
    cnts[t] += 1
  
    total_max_v = max(total_max_v, max_v)
    total_min_v = min(total_min_v, min_v)
    
  return total_min_v, total_max_v


N = input(int)
A = input_n(int)
cnts = input_n(int)
min_v, max_v = dfs(A, 0, cnts, A[0])
print(max_v)
print(min_v)