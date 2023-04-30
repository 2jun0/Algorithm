import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())

n = input(int)

A = [input(int) for _ in range(n)]
a_idx = 0

stack = []
log = []

for x in range(1, n+1):
  # 1~n 까지 순회 당장 필요없는 건 스택에 넣어 둔다.
  stack.append(x)
  log.append('+')
  
  while stack and stack[-1] == A[a_idx]:
    # 지금 필요한걸 스택에서 꺼내기
    a_idx += 1
    
    stack.pop()
    log.append('-')
    
if a_idx == n:
  print('\n'.join(log))
else:
  print('NO')