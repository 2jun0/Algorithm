import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

def factorial(x, div):
	result = 1
	for i in range(2, x+1):
		result = (result * (i % div)) % div
	return result

DIV = 1000000007

N = input(int)
names = []
for _ in range(N):
  names.append(input())
names.sort()

def func(idxes, level):
  if len(idxes) == 1: return 1
  
  if len(names[idxes[0]]) <= level: s = ''
  else: s = names[idxes[0]][level]

  group = {s : [idxes[0]]}
  for i in idxes[1:]:
    if len(names[i]) <= level:
      s = ''
      group[''] = [i]
    elif names[i][level] == s:
        group[s].append(i)
    else:
      s = names[i][level]
      group[s] = [i]
  
  result = factorial(len(group.keys()), DIV)
  for key, value in group.items():
    result = (result * func(value, level+1)) % DIV
  return result

print(func(range(0, N), 0))
